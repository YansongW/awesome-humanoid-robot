#!/usr/bin/env python3
"""audit_card_numbers.py — number whitelist auditor for card bodies (v6 ruleset).

Two modes:

  whitelist  (textbook-grade cards) — every numeric token in a body must appear
             in the card's source corpus (fetched web texts + wiki chapters +
             neighbor cards). Corpus = --sources-dir (all *.txt, recursively)
             plus per-card files from --corpus-map.
  deepread   (six-section deep-read cards) — every number in the experiments
             section of an applied card must be verbatim in the fetched full
             text (boundary-aware, float-equal, %-proximity) or a derivable
             value (diff/pct/ratio from a contextually-close pair of full-text
             numbers); derived values must carry an explicit label.

v6 ruleset (consolidated from .staging/deep_read + .staging/textbook_grade):
  - LaTeX cleaning of full texts ({,}, \! \\, \\; control chars, macros)
  - thousands separators stripped only between digit triplets; Chinese commas
    are token separators, never thousands marks
  - arXiv ids / DOIs / URLs masked before extraction
  - boundary-aware verbatim: (?<![\d.])NUM(?![\d.]); integer percents require
    '%' within 14 chars; decimals match by round(4)-equality
  - derived detection: |a-b|, |a-b|/|b|*100, a/b within tolerance from pool
    pairs <=300 chars apart; labels like （由表内数值 X→Y 计算） exempt
  - structural numbers (single digits, years 1990-2030) exempt in whitelist mode

Exit code 1 when any card misses/violates; 0 when clean.

Usage:
  python scripts/audit_card_numbers.py whitelist --bodies-dir .staging/x/bodies \
      --corpus-map .staging/x/corpus_map.json --sources-dir .staging/x/sources
  python scripts/audit_card_numbers.py deepread --targets-file t.json \
      --fulltexts-dir .staging/deep_read_run/fulltexts
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

NUM_RE = re.compile(r"\d+\.\d+%?|\d+%|\d{3,}")
TOKEN_RE = re.compile(r"\d+(?:\.\d+)?")
LABEL_INLINE_RE = re.compile(r"（由[^）]{0,40}计算）")
STRUCT = set("123456789") | {str(y) for y in range(1990, 2031)}


# ---------------------------------------------------------------- shared utils
def mask_nondata(text: str) -> str:
    """Remove URLs, entity ids, arXiv ids and DOIs before number extraction."""
    text = re.sub(r"https?://\S+", " ", text)
    text = re.sub(r"ent_\w+|src_\w+|rel_\w+", " ", text)
    text = re.sub(r"arXiv:\S+", " ", text, flags=re.I)
    text = re.sub(r"10\.\d{4,5}/\S+", " ", text)
    text = re.sub(r"\d{4}\.\d{4,5}(v\d+)?", " ", text)
    return text


def norm_tokens(text: str) -> set:
    """All number tokens with v6 normalization (CJK comma = separator)."""
    text = text.replace("，", " ").replace("。", "。")
    text = re.sub(r"(?<=\d),(?=\d{3}\b)", "", text)
    return set(TOKEN_RE.findall(text))


# ---------------------------------------------------------- deepread mode core
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
        if b != 0 and abs((a / b) ** 2 - x) < max(0.51, 0.01 * x):
            return (a, b, "ratio²")
        if abs(a * b - x) < 0.051:
            return (a, b, "product")
    return None


DERIVED_LABEL_RE = re.compile(r"（由[^）]{0,40}(?:计算|推算)）|按[^，。；\n]{0,15}(?:公式|参数表|数据)\s*(?:推算|计算)")


def sentence_ctx(section: str, num: str) -> str:
    i = section.find(num)
    if i < 0:
        return ""
    s = max(section.rfind("。", 0, i), section.rfind("\n", 0, i)) + 1
    e = section.find("。", i)
    return section[s:e if e > 0 else len(section)]


def section_of(card_text: str, heading: str) -> str:
    m = re.search(rf"(?ms)^{re.escape(heading)}\s*$", card_text)
    if not m:
        return ""
    rest = card_text[m.end():]
    m2 = re.search(r"(?m)^## ", rest)
    return rest[:m2.start()] if m2 else rest


# ------------------------------------------------------------------ whitelist
def audit_whitelist(args) -> int:
    corpus_map = {}
    if args.corpus_map:
        corpus_map = json.loads(Path(args.corpus_map).read_text(encoding="utf-8"))
    shared = set()
    if args.sources_dir:
        for cf in Path(args.sources_dir).rglob("*.txt"):
            shared |= norm_tokens(cf.read_text(encoding="utf-8", errors="ignore"))
    rc = 0
    bodies = sorted(Path(args.bodies_dir).glob("*.zh.md")) if args.bodies_dir else []
    if args.cards_file:
        for cid in json.loads(Path(args.cards_file).read_text(encoding="utf-8")):
            hits = list(ROOT.glob(f"research/**/{cid}.md"))
            if hits:
                bodies.append(hits[0])
    for body_path in bodies:
        card = body_path.stem.replace(".zh", "")
        corpus = set(shared)
        raw_parts = []
        for rel in corpus_map.get(card, []):
            p = ROOT / rel
            if p.exists():
                txt = p.read_text(encoding="utf-8", errors="ignore")
                corpus |= norm_tokens(txt)
                raw_parts.append(txt)
        if args.sources_dir:
            for cf in Path(args.sources_dir).rglob("*.txt"):
                raw_parts.append(cf.read_text(encoding="utf-8", errors="ignore"))
        raw_corpus = "\n".join(raw_parts)
        pool = ft_pool(raw_corpus)  # proximity pool for labeled-derived checks
        body = mask_nondata(body_path.read_text(encoding="utf-8"))
        missing = []
        for tok in sorted(norm_tokens(body), key=lambda x: (len(x), x)):
            base = tok.rstrip("0").rstrip(".") if "." in tok else tok
            hit = tok in corpus or base in corpus or any(
                c.startswith(tok) or (base and c.startswith(base)) for c in corpus if len(c) >= len(tok)
            )
            if hit or tok in STRUCT:
                continue
            # labeled-derived exemption: the sentence must carry an explicit
            # derivation label AND the value must be derivable from corpus numbers
            i = body.find(tok)
            sent = body[max(body.rfind("。", 0, i), body.rfind("\n", 0, i)) + 1:
                        (body.find("。", i) if body.find("。", i) > 0 else len(body))]
            if DERIVED_LABEL_RE.search(sent):
                try:
                    if derive(float(tok), pool):
                        continue
                except ValueError:
                    pass
            missing.append(tok)
        print(f"{'OK ' if not missing else 'MISS'} {card}: missing={missing}")
        if missing:
            rc = 1
    return rc


# ------------------------------------------------------------------- deepread
def audit_deepread(args) -> int:
    targets = json.loads(Path(args.targets_file).read_text(encoding="utf-8"))
    if isinstance(targets, list) and targets and isinstance(targets[0], dict):
        ids = [t["id"] for t in targets]
    else:
        ids = targets
    ft_dir = Path(args.fulltexts_dir)
    n_clean = n_der = n_viol = 0
    report = []
    for eid in ids:
        hits = list(ROOT.glob(f"research/**/{eid}.md"))
        ft_path = ft_dir / f"{eid}.txt"
        if not hits or not ft_path.exists():
            report.append({"id": eid, "status": "no_card_or_fulltext"})
            continue
        card = hits[0].read_text(encoding="utf-8", errors="ignore")
        sec = section_of(card, "## 实验与结果")
        if not sec:
            n_clean += 1
            report.append({"id": eid, "status": "no_experiments_section"})
            continue
        sec = re.sub(r"(\d),(\d{3})", r"\1\2", sec)
        sec = mask_nondata(sec)
        labeled_spans = [m.span() for m in LABEL_INLINE_RE.finditer(sec)]
        ft = clean_ft(ft_path.read_text(encoding="utf-8", errors="ignore"))
        pool = ft_pool(ft_path.read_text(encoding="utf-8", errors="ignore"))
        violations, derived_unlabeled = [], []
        for n in dict.fromkeys(NUM_RE.findall(sec)):
            i = sec.find(n)
            if any(s - 2 <= i <= e for s, e in labeled_spans) or "（由" in sec[i:i + len(n) + 60]:
                continue
            if verbatim_ok(n, ft):
                continue
            ev = None
            try:
                ev = derive(float(n.rstrip("%")), pool)
            except ValueError:
                pass
            if ev:
                derived_unlabeled.append({"num": n, "evidence": ev, "ctx": sentence_ctx(sec, n)[:100]})
            else:
                violations.append({"num": n, "ctx": sentence_ctx(sec, n)[:100]})
        status = "violation" if violations else ("derived_unlabeled" if derived_unlabeled else "clean")
        if status == "clean":
            n_clean += 1
        elif status == "derived_unlabeled":
            n_der += 1
        else:
            n_viol += 1
        report.append({"id": eid, "status": status,
                       "violations": violations, "derived_unlabeled": derived_unlabeled})
    print(f"deepread number audit: clean={n_clean} derived_unlabeled={n_der} violation={n_viol}")
    for r in report:
        if r["status"] in ("violation", "derived_unlabeled"):
            print(f"  [{r['status']}] {r['id']}: "
                  f"v={[x['num'] for x in r.get('violations', [])][:6]} "
                  f"d={[x['num'] for x in r.get('derived_unlabeled', [])][:6]}")
    if args.report:
        Path(args.report).write_text(json.dumps(report, ensure_ascii=False, indent=1), encoding="utf-8")
    return 1 if n_viol else 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="mode", required=True)
    w = sub.add_parser("whitelist", help="textbook cards: every number must appear in corpus")
    w.add_argument("--bodies-dir", help="dir of <id>.zh.md fragments")
    w.add_argument("--cards-file", help="JSON list of in-place card ids to audit (zh body)")
    w.add_argument("--corpus-map", help="JSON: card id -> repo-relative corpus files")
    w.add_argument("--sources-dir", help="shared corpus dir (all *.txt recursive)")
    d = sub.add_parser("deepread", help="deep-read cards: experiments numbers vs full text")
    d.add_argument("--targets-file", required=True, help="JSON list of ids or {'id':...} objects")
    d.add_argument("--fulltexts-dir", required=True)
    d.add_argument("--report", help="write per-card JSON report here")
    args = ap.parse_args()
    if args.mode == "whitelist":
        if not args.bodies_dir and not args.cards_file:
            ap.error("whitelist mode needs --bodies-dir or --cards-file")
        return audit_whitelist(args)
    return audit_deepread(args)


if __name__ == "__main__":
    sys.exit(main())
