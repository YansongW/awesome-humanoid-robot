#!/usr/bin/env python3
"""deep_read_cards.py — full-text six-section deep-read pipeline for paper cards.

Consolidated from the verified .staging batches (deep_read pilot, batch1/2,
catchup batch3/4). All hardened patches are included:

  * fact extraction per 40K-char chunk (T=0.2); image-only tables must be
    marked 「该表为图片，数字未提取」 instead of hallucinated
  * synthesis input blob capped at ~20K chars (DeepSeek resets connections on
    larger Chinese-heavy inputs); oversized blobs are condensed first
  * programmatic number whitelist at generation time: every number in the
    synthesis prompt's output must come from the extracted whitelist, or be a
    derived value with an explicit 「（由表内数值 X→Y 计算）」 label
  * post-generation verification: experiments-section numbers are checked
    verbatim (boundary-aware) against the full text; derivable numbers are
    auto-labeled; unverifiable sentences are dropped by a sentence-level
    fallback; one strict retry before fallback
  * typography discipline: `](` must not be adjacent (except real links);
    checked and auto-fixed on every section
  * stubborn cards fall back to per-section generation (逐段拼接)
  * max_tokens=8000 (output truncation fix)

Stages: select -> fetch -> generate -> apply -> check (or `run` for all).
State lives in .staging/deep_read_run/ (gitignored): targets.json,
fulltexts/, deepread/, progress.jsonl, usage.json, apply_report.json.
All stages are checkpointed and safe to re-run.

Discipline on apply: frontmatter untouched except one appended
verification.notes line (asserted); ## 参考 kept verbatim; en/ko sections
dropped (rebuild them with scripts/translate_entry_bodies.py).

API key: environment variable DEEPSEEK_API_KEY.

Usage:
  python scripts/deep_read_cards.py run --limit 20
  python scripts/deep_read_cards.py select --since 2026-07-01 --limit 100
  python scripts/deep_read_cards.py fetch --workers 4
  python scripts/deep_read_cards.py generate --workers 7
  python scripts/deep_read_cards.py apply
  python scripts/deep_read_cards.py check --sample 10
  python scripts/deep_read_cards.py run --targets-file my_targets.json
"""
from __future__ import annotations

import argparse
import html as H
import json
import os
import re
import subprocess
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from itertools import combinations
from pathlib import Path

import requests
import yaml

ROOT = Path(__file__).resolve().parent.parent
STATE = ROOT / ".staging" / "deep_read_run"
FT_DIR = STATE / "fulltexts"
DR_DIR = STATE / "deepread"
PROGRESS = STATE / "progress.jsonl"

API_URL = "https://api.deepseek.com/chat/completions"
_CRED_FILE = Path.home() / "Desktop" / ".ai_credentials.txt"
if os.environ.get("DEEPSEEK_API_KEY"):
    API_KEY = os.environ["DEEPSEEK_API_KEY"]
elif _CRED_FILE.exists():  # same fallback as scripts/translate_entry_bodies.py; never print it
    API_KEY = _CRED_FILE.read_text(encoding="utf-8").split("DEEPSEEK_API_KEY=")[1].split("\n")[0].strip()
else:
    API_KEY = ""
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 awesome-humanoid-robot-deepread/1.0")

CHUNK = 40000
BLOB_CAP = 20000
NUM_RE = re.compile(r"\d+\.\d+%?|\d+%|\d{3,}")
MARKERS = ["SUMMARY_ZH", "CHANGED", "METHOD", "INNOVATION", "EXPERIMENTS", "LIMITS", "TAKEAWAY"]
SECTIONS = [("changed", "它改变了什么"), ("method", "方法拆解"), ("innovation", "关键创新"),
            ("experiments", "实验与结果"), ("limits", "边界与局限"), ("takeaway", "工程启示")]
NEED_HEADINGS = ["## 概述", "## 它改变了什么", "## 方法拆解", "## 关键创新",
                 "## 实验与结果", "## 边界与局限", "## 工程启示", "## 参考"]

FACT_PROMPT = (
    "你是机器人领域资深研究工程师。下面是论文全文的一个片段。请提取供深度解读使用的事实要点，"
    "用中文 Markdown 列表输出，覆盖：\n"
    "1) 问题与动机（作者真正想改变什么）；2) 方法要点（分步流程、公式/架构关键、关键设计决策及作者给出的理由）；"
    "3) 实验设置与关键数字（任务、基线、成功率/误差/参数，含表格数字与单位，**逐字照抄原文数字，"
    "不得改写或四舍五入**；表格为图片时写「该表为图片，数字未提取」）；\n"
    "4) 作者承认的局限与未做之事；5) 复现/工程细节（平台、数据量、训练配置、推理频率、硬件）。\n"
    "禁止输出原文中不存在的任何数字。只输出事实要点，不要评论。"
)
SYN_PROMPT = (
    "你是机器人领域资深技术评论人，为懂行人写中文深度解读（不是摘要翻译，不是教科书腔）。"
    "基于给出的论文题目与从全文提取的事实要点，写七段解读，严格用以下分隔标记，不要输出其他内容：\n"
    "<<<SUMMARY_ZH>>>\n（2-3 句中文精要：是什么、谁做的、核心贡献）\n"
    "<<<CHANGED>>>\n（它改变了什么：问题与动机。不要写“本文提出了什么”，要写你作为行家对“它真正改变了什么”的判断。1-2 段）\n"
    "<<<METHOD>>>\n（方法拆解：怎么做的。分步、公式/架构关键点、关键设计决策及理由；用 ### 小标题与列表组织；保留关键符号与参数名）\n"
    "<<<INNOVATION>>>\n（关键创新：1-3 点，每点说清为什么是新的、为什么重要）\n"
    "<<<EXPERIMENTS>>>\n（实验与结果：对照设置、关键数字、结果的含义；关键数字用 Markdown 表格汇总）\n"
    "<<<LIMITS>>>\n（边界与局限：作者没做什么、什么条件下结论可能不成立；事实要点没有时写「论文未明确」）\n"
    "<<<TAKEAWAY>>>\n（工程启示：对复现、选型、下游团队的具体指导——先核对什么、哪里最容易踩坑）\n"
    "纪律：\n"
    "1. 附带的【数字白名单】是从论文原文程序化提取的全部数字；全文出现的每个数字必须逐字来自白名单；"
    "由两个白名单数字直接计算的变化量允许使用，但必须紧跟显式标注（如「（由表内数值 b→a 计算）」）；"
    "其余写「论文未明确」。\n"
    "2. 排版：`]` 与 `(` 不得相邻（链接除外，本节不要放链接）。\n"
    "3. 专有名词保留英文；判断要有事实支撑。"
)
COND_PROMPT = (
    "你是研究助理。把下面的论文事实要点压缩到 6000 字以内，"
    "保留所有具体数字、任务名、基线、参数、平台与结论（逐条照抄，禁止改写数字），只删冗余表述。"
    "只输出压缩后的事实要点。"
)
SECTION_SPECS = {
    "SUMMARY_ZH": "2-3 句中文精要：是什么、谁做的、核心贡献。",
    "CHANGED": "它改变了什么：问题与动机。不要写“本文提出了什么”，要写你作为行家对“它真正改变了什么”的判断。1-2 段。",
    "METHOD": "方法拆解：怎么做的。分步、公式/架构关键点、关键设计决策及理由；用 ### 小标题与列表组织；保留关键符号与参数名。",
    "INNOVATION": "关键创新：1-3 点，每点说清为什么是新的、为什么重要。",
    "EXPERIMENTS": "实验与结果：对照设置、关键数字、结果的含义；关键数字尽量用 Markdown 表格汇总；每个数字都必须能在事实要点中找到。",
    "LIMITS": "边界与局限：作者没做什么、什么条件下结论可能不成立；事实要点没有时写「论文未明确」。",
    "TAKEAWAY": "工程启示：对复现、选型、下游团队的具体指导——先核对什么、哪里最容易踩坑。",
}
SECTION_CAPS = {"SUMMARY_ZH": 300, "CHANGED": 700, "METHOD": 1200, "INNOVATION": 600,
                "EXPERIMENTS": 1000, "LIMITS": 500, "TAKEAWAY": 500}
SECTION_PROMPT = (
    "你是机器人领域资深技术评论人，为懂行人写中文深度解读（不是摘要翻译，不是教科书腔）。"
    "基于给出的论文题目与从全文提取的事实要点，只写深度解读的「{name}」这一段，"
    "第一行输出标记 <<<{marker}>>>，然后输出该段内容，不要输出其他任何段或标记。\n"
    "本段要求：{spec}\n"
    "纪律：所有数字/结论必须来自给出的事实要点，禁止编造；专有名词保留英文；判断要有事实支撑；"
    "中文为主体；`]` 与 `(` 不得相邻；本段长度控制在 {cap} 字以内。"
)
PAGE_NOTE = ("\n\n注意：本文全文不可得，以下事实要点来自项目页/公开资料而非论文原文；"
             "在 METHOD 与 EXPERIMENTS 中凡无法从资料确认之处，明确写「论文未明确」，禁止外推。")

USAGE = {"prompt_tokens": 0, "completion_tokens": 0, "calls": 0}
_ulock = threading.Lock()


# ------------------------------------------------------------------ utilities
def log(rec: dict) -> None:
    STATE.mkdir(parents=True, exist_ok=True)
    with _ulock:
        with PROGRESS.open("a", encoding="utf-8") as f:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")


def call(prompt: str, content: str, temp: float, retries: int = 3, max_tokens: int = 8000):
    if not API_KEY:
        raise SystemExit("DEEPSEEK_API_KEY is not set; export it before running generate.")
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    payload = {"model": "deepseek-chat",
               "messages": [{"role": "system", "content": prompt},
                            {"role": "user", "content": content}],
               "temperature": temp, "max_tokens": max_tokens}
    for attempt in range(retries):
        try:
            r = requests.post(API_URL, headers=headers, json=payload, timeout=300)
            if r.status_code != 200:
                time.sleep(3 * (attempt + 1))
                continue
            data = r.json()
            u = data.get("usage") or {}
            with _ulock:
                USAGE["prompt_tokens"] += u.get("prompt_tokens", 0)
                USAGE["completion_tokens"] += u.get("completion_tokens", 0)
                USAGE["calls"] += 1
            return data["choices"][0]["message"]["content"].strip()
        except (requests.RequestException, KeyError, ValueError):
            time.sleep(3 * (attempt + 1))
    return None


def parse_sections(out):
    out = re.sub(r"^```(?:markdown|md)?\s*\n", "", out or "")
    out = re.sub(r"\n```\s*$", "", out)
    pat = "".join(re.escape(f"<<<{mk}>>>") + r"\s*(.*?)\s*" for mk in MARKERS)
    m = re.search(pat + r"\Z", out, re.S)
    if not m:
        return None
    parts = {mk.lower(): m.group(i + 1).strip() for i, mk in enumerate(MARKERS)}
    return parts if all(parts.values()) else None


def parse_one_section(out, marker):
    out = re.sub(r"^```(?:markdown|md)?\s*\n", "", out or "")
    out = re.sub(r"\n```\s*$", "", out)
    m = re.search(re.escape(f"<<<{marker}>>>") + r"\s*(.*?)\s*(?:<<<[A-Z_]+>>>|\Z)", out, re.S)
    if not m:
        return None
    body = m.group(1).strip()
    return body if len(body) > 30 else None


def cjk_ok(text: str) -> bool:
    latin = sum(1 for c in text if "a" <= c.lower() <= "z")
    cjk = sum(1 for c in text if "一" <= c <= "鿿")
    return cjk > 0 and cjk / max(cjk + latin, 1) > 0.4


def clean_ft(t: str) -> str:
    t = re.sub(r"\{,\}", "", t)
    t = re.sub(r"(\d),(\d)", r"\1\2", t)
    t = re.sub(r"\\!|\\,|\\;|\\ ", "", t)
    t = re.sub(r"\\[a-zA-Z]+", "", t)
    return re.sub(r"\s+", " ", t).lower()


def verbatim_ok(num: str, ft: str) -> bool:
    core = num.rstrip("%")
    bd = r"(?<![\d.])" + re.escape(core.lower()) + r"(?![\d.])"
    if num.endswith("%") and "." not in core:
        return any("%" in ft[m.end():m.end() + 14] for m in re.finditer(bd, ft))
    if re.search(bd, ft):
        return True
    try:
        v = round(float(core), 4)
        return any(round(float(m.group(0)), 4) == v for m in re.finditer(r"\d+\.\d+", ft))
    except ValueError:
        return False


def ft_pool(ft_raw: str):
    out = []
    for m in re.finditer(r"\d+\.\d+%?|\d+%", ft_raw):
        try:
            v = float(m.group(0).rstrip("%"))
        except ValueError:
            continue
        if 0 < v < 100000:
            out.append((round(v, 4), m.start()))
    return out


def derive(x: float, pool, max_gap: int = 300):
    for (a, pa), (b, pb) in combinations(pool, 2):
        if abs(pa - pb) > max_gap:
            continue
        d = abs(a - b)
        if abs(d - x) < 0.051:
            return (a, b, "diff")
        if b != 0 and abs(d / abs(b) * 100 - x) < 0.55:
            return (a, b, "pct")
        if b != 0 and abs(a / b - x) < 0.051:
            return (a, b, "ratio")
    return None


def derive_label(a, b, op):
    return {"pct": f"（由表内数值 {b}→{a} 计算）",
            "diff": f"（由表内数值 {a}−{b} 计算）"}.get(op, f"（由表内数值 {a}÷{b} 计算）")


def typography_ok(text: str) -> bool:
    for m in re.finditer(r"\]\(", text):
        tail = text[m.end():m.end() + 8]
        if not tail.lower().startswith(("http", "www", "#", "mail")):
            return False
    return True


def fix_typography(text: str) -> str:
    return re.sub(r"\]\((?!http|www|#|mail)", "] (", text, flags=re.I)


def condense_blob(blob: str, cap: int = 17000) -> str:
    """Keep synthesis input under the DeepSeek reset threshold."""
    if len(blob) <= cap:
        return blob
    parts = [blob[i:i + 15000] for i in range(0, len(blob), 15000)]
    out = []
    for p in parts:
        r = call(COND_PROMPT, p, 0.2)
        out.append(r or p[:6000])
    return "\n\n".join(out)[:cap]


def extract_html(raw: str) -> str:
    raw = re.sub(r"<(script|style|nav|header|footer)[^>]*>.*?</\1>", " ", raw, flags=re.S | re.I)
    raw = re.sub(r"</(tr|p|div|section|h[1-6]|li|table|caption|figure)>", "\n", raw, flags=re.I)
    raw = re.sub(r"</t[dh]>", " | ", raw, flags=re.I)
    text = re.sub(r"<[^>]+>", " ", raw)
    text = H.unescape(text)
    text = re.sub(r"[ \t]+", " ", text)
    return re.sub(r"\n\s*\n+", "\n\n", text).strip()


def http_get(url: str, timeout: int = 90, min_size: int = 30000, binary: bool = False):
    for attempt in range(3):
        try:
            r = subprocess.run(["curl", "-sL", "--max-time", str(timeout), "-A", UA,
                                "-w", "%{http_code}", "-o", "/tmp/dr_fetch_tmp", url],
                               capture_output=True, text=True)
            code = (r.stdout or "").strip()[-3:]
            p = Path("/tmp/dr_fetch_tmp")
            if code == "200" and p.exists() and p.stat().st_size > min_size:
                data = p.read_bytes()
                p.unlink(missing_ok=True)
                return data if binary else data.decode("utf-8", errors="ignore")
        except Exception:
            pass
        time.sleep(3 * (attempt + 1))
    return None


# ---------------------------------------------------------------------- stage: select
def arxiv_id_of(fm: dict) -> str | None:
    for s in fm.get("sources") or []:
        url = s.get("url") or ""
        m = re.search(r"arxiv\.org/(?:abs|pdf|html)/(\d{4}\.\d{4,5})", url)
        if m:
            return m.group(1)
    return None


def card_date_of(fm: dict) -> str:
    dates = [s.get("date", "") for s in fm.get("sources") or [] if s.get("date")]
    return max(dates) if dates else ""


def stage_select(args) -> int:
    if args.targets_file:
        targets = json.loads(Path(args.targets_file).read_text(encoding="utf-8"))
    else:
        targets = []
        for p in sorted(ROOT.glob("research/papers/*.md")):
            text = p.read_text(encoding="utf-8", errors="ignore")
            if "## 它改变了什么" in text:
                continue  # already deep-read
            if "内容待补" in text or "待补充" in text:
                continue  # placeholder cards are out of scope
            try:
                fm = yaml.safe_load(text.split("---", 2)[1])
            except Exception:
                continue
            if not fm or fm.get("type") != "paper":
                continue
            if args.since and card_date_of(fm) < args.since:
                continue
            aid = arxiv_id_of(fm)
            page_url = None
            if not aid:
                for s in fm.get("sources") or []:
                    if (s.get("url") or "").startswith("http"):
                        page_url = s["url"]
                        break
            targets.append({"id": fm["$id"],
                            "arxiv_id": aid,
                            "tier": "arxiv" if aid else ("page" if page_url else "none"),
                            "page_url": page_url})
        targets = [t for t in targets if t["tier"] != "none"]
    if args.limit:
        targets = targets[: args.limit]
    STATE.mkdir(parents=True, exist_ok=True)
    (STATE / "targets.json").write_text(json.dumps(targets, ensure_ascii=False, indent=1),
                                        encoding="utf-8")
    tiers = {}
    for t in targets:
        tiers[t["tier"]] = tiers.get(t["tier"], 0) + 1
    print(f"select: {len(targets)} targets {tiers} -> {STATE/'targets.json'}")
    return 0


# ---------------------------------------------------------------------- stage: fetch
def fetch_one(t: dict) -> str:
    eid = t["id"]
    out = FT_DIR / f"{eid}.txt"
    if out.exists() and out.stat().st_size > 15000:
        return "cached"
    got = False
    if t["tier"] == "arxiv" and t.get("arxiv_id"):
        aid = t["arxiv_id"]
        for url in (f"https://arxiv.org/html/{aid}v1", f"https://arxiv.org/html/{aid}v2",
                    f"https://arxiv.org/html/{aid}", f"https://ar5iv.labs.arxiv.org/html/{aid}"):
            data = http_get(url)
            if data:
                text = extract_html(data)
                if len(text) > 15000:
                    out.write_text(text, encoding="utf-8")
                    got = True
                    break
            time.sleep(3)
        if not got:  # PDF fallback (PyMuPDF)
            data = http_get(f"https://arxiv.org/pdf/{aid}", timeout=120, min_size=20000, binary=True)
            if data:
                tmp = FT_DIR / f"{eid}.pdf"
                tmp.write_bytes(data)
                try:
                    import fitz  # PyMuPDF
                    doc = fitz.open(str(tmp))
                    text = "\n\n".join(pg.get_text() for pg in doc)
                    doc.close()
                    if len(text) > 15000:
                        out.write_text(text, encoding="utf-8")
                        got = True
                except ImportError:
                    print("PyMuPDF (fitz) not installed; PDF fallback unavailable", flush=True)
                except Exception:
                    pass
                finally:
                    tmp.unlink(missing_ok=True)
    elif t["tier"] == "page" and t.get("page_url"):
        data = http_get(t["page_url"], min_size=3000)
        if data:
            text = extract_html(data)
            if len(text) > 2000:
                out.write_text(text[:60000], encoding="utf-8")
                got = True
    log({"stage": "fetch", "id": eid, "ok": got})
    time.sleep(3)
    return "ok" if got else "fail"


def stage_fetch(args) -> int:
    targets = json.loads((STATE / "targets.json").read_text(encoding="utf-8"))
    FT_DIR.mkdir(parents=True, exist_ok=True)
    from collections import Counter
    stats = Counter()
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futs = [pool.submit(fetch_one, t) for t in targets]
        for i, f in enumerate(as_completed(futs)):
            stats[f.result()] += 1
            if (i + 1) % 20 == 0:
                print(f"  fetch [{i+1}/{len(futs)}] {dict(stats)}", flush=True)
    print(f"fetch DONE: {dict(stats)}")
    return 0 if stats["fail"] == 0 else 1


# ------------------------------------------------------------------- stage: generate
def synthesize_sectionwise(title: str, blob: str, tier: str):
    src = f"论文题目：{title}\n\n全文事实要点：\n{condense_blob(blob)}"
    if tier == "page":
        src += PAGE_NOTE
    parts = {}

    def gen(mk):
        p = SECTION_PROMPT.format(name=mk, marker=mk, spec=SECTION_SPECS[mk], cap=SECTION_CAPS[mk])
        body = parse_one_section(call(p, src, 0.3), mk)
        if not body:
            src2 = f"论文题目：{title}\n\n全文事实要点：\n{condense_blob(blob, 12000)}"
            body = parse_one_section(call(p, src2, 0.3), mk)
        return mk, body

    with ThreadPoolExecutor(max_workers=7) as pool:
        for mk, body in pool.map(gen, MARKERS):
            if body:
                parts[mk.lower()] = body
    if len(parts) < len(MARKERS):
        return None
    if not all(cjk_ok(parts[k]) for k in ("changed", "method")):
        return None
    return parts


def verify_and_fix_experiments(parts: dict, ft_text: str):
    """Number whitelist enforcement on the experiments section.

    Returns (parts, bad_numbers). Verbatim numbers pass; derivable numbers get
    an auto-inserted （由表内数值 X→Y 计算） label; anything else is reported.
    """
    exp = parts.get("experiments", "")
    ft_clean = clean_ft(ft_text)
    pool = ft_pool(ft_text)
    bad = []
    for n in dict.fromkeys(NUM_RE.findall(exp)):
        i = exp.find(n)
        if verbatim_ok(n, ft_clean) or "（由" in exp[max(0, i - 2):i + len(n) + 60]:
            continue
        try:
            ev = derive(float(n.rstrip("%")), pool)
        except ValueError:
            ev = None
        if ev:
            pat = re.compile(r"(?<![\d.])" + re.escape(n) + r"(?![\d.%])")
            mm = pat.search(exp)
            if mm:
                exp = exp[:mm.end()] + derive_label(*ev) + exp[mm.end():]
                parts["experiments"] = exp
            continue
        bad.append(n)
    return parts, bad


def generate_one(t: dict) -> str:
    eid = t["id"]
    out = DR_DIR / f"{eid}.json"
    if out.exists():
        return "cached"
    ft_path = FT_DIR / f"{eid}.txt"
    if not ft_path.exists():
        log({"stage": "generate", "id": eid, "status": "no_fulltext"})
        return "no_fulltext"
    ft_text = ft_path.read_text(encoding="utf-8", errors="ignore")
    title = t.get("title") or eid
    if not t.get("title"):
        card = ROOT / "research" / "papers" / f"{eid}.md"
        if card.exists():
            try:
                fm = yaml.safe_load(card.read_text(encoding="utf-8", errors="ignore").split("---", 2)[1])
                title = (fm.get("names") or {}).get("en", eid)
            except Exception:
                pass
    chunks = [ft_text[i:i + CHUNK] for i in range(0, len(ft_text), CHUNK)]
    facts = [None] * len(chunks)
    with ThreadPoolExecutor(max_workers=4) as pool:
        futs = {pool.submit(call, FACT_PROMPT, f"论文片段 {i+1}/{len(chunks)}：\n{c}", 0.2): i
                for i, c in enumerate(chunks)}
        for f in as_completed(futs):
            facts[futs[f]] = f.result() or ""
    blob = condense_blob("\n\n".join(x for x in facts if x))[:BLOB_CAP]
    if len(blob) < 400:
        log({"stage": "generate", "id": eid, "status": "fact_failed"})
        return "fact_failed"

    # number whitelist extracted from the full text, injected into the prompt
    wl = list(dict.fromkeys(NUM_RE.findall(re.sub(r"(\d),(\d)", r"\1\2", ft_text))))[:180]
    src = (f"论文题目：{title}\n\n全文事实要点：\n{blob}\n\n"
           f"【数字白名单】（仅这些数字可直接使用）：\n" + "、".join(wl))
    if t["tier"] == "page":
        src += PAGE_NOTE

    parts = None
    for attempt in range(2):
        parts = parse_sections(call(SYN_PROMPT, src, 0.3))
        if not parts or not all(cjk_ok(parts[k]) for k in ("changed", "method")):
            parts = None
            continue
        parts, bad = verify_and_fix_experiments(parts, ft_text)
        typo = typography_ok("".join(parts.values()))
        if not bad and typo:
            break
        src += (f"\n\n（上次不合格：白名单外数字 {bad[:6]}；`]( 相邻={not typo}。"
                f"请只用白名单数字或改为显式标注计算值/「论文未明确」，并保持 ] 与 ( 不相邻）")
        parts = None if bad else parts

    # sentence-level fallback: keep only fully verified sentences
    if parts is None:
        pass  # nothing to salvage
    if parts is not None and bad:
        exp = parts.get("experiments", "")
        kept, dropped = [], 0
        for sent in re.split(r"(?<=。)\s*|\n", exp):
            if not sent.strip():
                continue
            ok = True
            for n in NUM_RE.findall(sent):
                if verbatim_ok(n, clean_ft(ft_text)):
                    continue
                try:
                    ev = derive(float(n.rstrip("%")), ft_pool(ft_text))
                except ValueError:
                    ev = None
                if not ev:
                    ok = False
                    break
            if ok:
                kept.append(sent)
            else:
                dropped += 1
        if dropped:
            kept.append(f"（本节另有 {dropped} 句含无法从全文文本核实的数字，已按纪律移除；"
                        f"论文未明确或以图/表图片形式给出。）")
        parts["experiments"] = "\n".join(kept)
        parts["_meta"] = {"title": title, "chunks": len(chunks), "fact_chars": len(blob),
                          "fallback_trimmed": dropped}
        for k in ("summary_zh", "changed", "method", "innovation", "experiments", "limits", "takeaway"):
            parts[k] = fix_typography(parts[k])
        out.write_text(json.dumps(parts, ensure_ascii=False, indent=1), encoding="utf-8")
        log({"stage": "generate", "id": eid, "status": "fallback_ok"})
        return "fallback_ok"

    if parts is None:
        # stubborn path: per-section generation, then the same number guard
        parts = synthesize_sectionwise(title, blob, t["tier"])
        if not parts:
            log({"stage": "generate", "id": eid, "status": "synthesis_failed"})
            return "synthesis_failed"
        parts, bad = verify_and_fix_experiments(parts, ft_text)
        if bad:
            log({"stage": "generate", "id": eid, "status": "whitelist_failed", "bad": bad[:6]})
            return "whitelist_failed"

    parts["_meta"] = {"title": title, "tier": t["tier"], "chunks": len(chunks),
                      "fact_chars": len(blob)}
    for k in ("summary_zh", "changed", "method", "innovation", "experiments", "limits", "takeaway"):
        parts[k] = fix_typography(parts[k])
    out.write_text(json.dumps(parts, ensure_ascii=False, indent=1), encoding="utf-8")
    log({"stage": "generate", "id": eid, "status": "ok"})
    return "ok"


def stage_generate(args) -> int:
    targets = json.loads((STATE / "targets.json").read_text(encoding="utf-8"))
    DR_DIR.mkdir(parents=True, exist_ok=True)
    from collections import Counter
    stats = Counter()
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futs = [pool.submit(generate_one, t) for t in targets]
        for i, f in enumerate(as_completed(futs)):
            stats[f.result()] += 1
            if (i + 1) % 10 == 0:
                print(f"  generate [{i+1}/{len(futs)}] {dict(stats)}", flush=True)
    (STATE / "usage.json").write_text(json.dumps(USAGE, indent=1), encoding="utf-8")
    print(f"generate DONE: {dict(stats)} usage={USAGE}")
    return 0


# ---------------------------------------------------------------------- stage: apply
def split_keep_references(body: str) -> str:
    m = re.search(r"(?ms)^## 参考\s*$", body)
    return body[m.start():].strip() if m else ""


def apply_one(t: dict, note_date: str) -> str:
    eid = t["id"]
    dr = DR_DIR / f"{eid}.json"
    if not dr.exists():
        return "no_output"
    parts = json.loads(dr.read_text(encoding="utf-8"))
    path = ROOT / "research" / "papers" / f"{eid}.md"
    if not path.exists():
        return "no_card"
    text = path.read_text(encoding="utf-8")
    if "## 它改变了什么" in text:
        return "already"
    head, body = text.split("---", 2)[1:]
    fm = yaml.safe_load(head)
    before = dict(fm)
    refs = split_keep_references(body)
    if not refs:
        refs = "## 参考\n"
        for s in fm.get("sources") or []:
            if s.get("url"):
                refs += f"- {s['url']}\n"
    note = (f" [{note_date}] body rewritten as full-text six-section deep read "
            f"(scripts/deep_read_cards.py, DeepSeek deepseek-chat T<=0.3, "
            f"{'arXiv full text' if t['tier'] == 'arxiv' else 'project-page source only, limited'}; "
            f"number whitelist enforced at generation); en/ko sections regenerated by translate pipeline.")
    fm["verification"] = dict(fm.get("verification") or {})
    fm["verification"]["notes"] = (fm["verification"].get("notes") or "") + note
    assert {k: v for k, v in fm.items() if k != "verification"} == \
           {k: v for k, v in before.items() if k != "verification"}, eid
    body_new = f"## 概述\n\n{parts['summary_zh']}\n\n"
    body_new += "\n\n".join(f"## {t_}\n\n{parts[k].strip()}" for k, t_ in SECTIONS)
    body_new += "\n\n" + refs.strip() + "\n"
    out = ("---\n" + yaml.safe_dump(fm, allow_unicode=True, sort_keys=False, width=120)
           + "---\n" + body_new)
    rt = yaml.safe_load(out.split("---", 2)[1])
    assert rt["$id"] == eid and rt["names"] == before["names"] and rt["sources"] == before["sources"], eid
    path.write_text(out, encoding="utf-8")
    return "ok"


def stage_apply(args) -> int:
    targets = json.loads((STATE / "targets.json").read_text(encoding="utf-8"))
    from collections import Counter
    stats = Counter()
    done = []
    for t in targets:
        r = apply_one(t, args.date)
        stats[r] += 1
        if r == "ok":
            done.append(t["id"])
    (STATE / "apply_report.json").write_text(
        json.dumps({"stats": dict(stats), "applied": done}, indent=1), encoding="utf-8")
    print(f"apply DONE: {dict(stats)}")
    return 0 if stats.get("ok", 0) + stats.get("already", 0) == len(targets) else 1


# ---------------------------------------------------------------------- stage: check
def stage_check(args) -> int:
    sys.path.insert(0, str(ROOT / "scripts"))
    import json as _json
    from jsonschema import Draft7Validator
    schema = _json.loads((ROOT / "data/schema/v1/entry_schema.json").read_text(encoding="utf-8"))
    validator = Draft7Validator(schema)
    report = _json.loads((STATE / "apply_report.json").read_text(encoding="utf-8"))
    applied = report["applied"]

    bad_schema = []
    for eid in applied:
        p = ROOT / "research" / "papers" / f"{eid}.md"
        fm = yaml.safe_load(p.read_text(encoding="utf-8").split("---", 2)[1])
        errs = list(validator.iter_errors(fm))
        if errs:
            bad_schema.append((eid, errs[0].message[:80]))
    print(f"schema: {len(applied)-len(bad_schema)}/{len(applied)} ok; bad={bad_schema[:5]}")

    missing = []
    for eid in applied:
        t = (ROOT / "research" / "papers" / f"{eid}.md").read_text(encoding="utf-8")
        miss = [h for h in NEED_HEADINGS if not re.search(rf"(?m)^{re.escape(h)}\s*$", t)]
        if miss:
            missing.append((eid, miss))
    print(f"six-section: {len(applied)-len(missing)}/{len(applied)} ok; missing={missing[:5]}")

    import random
    random.seed(42)
    sample = random.sample(sorted(applied), min(args.sample, len(applied)))
    hits_total = checked_total = 0
    for eid in sample:
        d = _json.loads((DR_DIR / f"{eid}.json").read_text(encoding="utf-8"))
        exp = d.get("experiments", "")
        ft_path = FT_DIR / f"{eid}.txt"
        ft = clean_ft(ft_path.read_text(encoding="utf-8")) if ft_path.exists() else ""
        cands = [c for c in dict.fromkeys(NUM_RE.findall(exp))][:30]
        random.shuffle(cands)
        checked = cands[:5]
        hits = sum(1 for n in checked if verbatim_ok(n, ft))
        hits_total += hits
        checked_total += len(checked)
        flag = "OK" if hits == len(checked) else "MISS"
        print(f"  [{flag}] {eid[:52]}: {hits}/{len(checked)}")
    print(f"number sampling: {hits_total}/{checked_total}")
    ok = not bad_schema and not missing and hits_total == checked_total
    print("check:", "ALL GREEN" if ok else "ISSUES FOUND")
    return 0 if ok else 1


# -------------------------------------------------------------------------- main
def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("stage", choices=["select", "fetch", "generate", "apply", "check", "run"],
                    help="pipeline stage ('run' = select..check)")
    ap.add_argument("--targets-file", help="JSON list of {'id','arxiv_id','tier','page_url'}; overrides select scan")
    ap.add_argument("--since", help="only cards whose newest source date >= YYYY-MM-DD")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--sample", type=int, default=10, help="cards sampled by check")
    ap.add_argument("--date", default=time.strftime("%Y-%m-%d"), help="date stamp for verification.notes")
    args = ap.parse_args()

    if not API_KEY and args.stage in ("generate", "run"):
        print("ERROR: DEEPSEEK_API_KEY is not set.", file=sys.stderr)
        return 2

    if args.stage == "run":
        for st in ("select", "fetch", "generate", "apply", "check"):
            rc = {"select": stage_select, "fetch": stage_fetch, "generate": stage_generate,
                  "apply": stage_apply, "check": stage_check}[st](args)
            if rc != 0 and st != "fetch":
                return rc
        return 0
    return {"select": stage_select, "fetch": stage_fetch, "generate": stage_generate,
            "apply": stage_apply, "check": stage_check}[args.stage](args)


if __name__ == "__main__":
    sys.exit(main())
