#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Static-site integrity audit for website/dist (trilingual: zh root, /en/, /ko/).

Read-only against dist. Writes report.md next to this script.
Re-runnable:  python3 audit.py  (optionally: python3 audit.py --dist <path>)

Checks:
 1. internal link integrity (href/src/action + data-* attrs with /... values)
 2. per-page asset existence + script load-order deps (ask.js needs search.js;
    graph pages need cytoscape before graph.js)
 3. template residue: {{ {% None undefined [object Object] NaN
 4. empty/duplicate-id <h1>, <html lang> vs path language, empty/None <title>
 5. /ask/ redirect pages (meta refresh target per language)
 6. data files: search-index.json, qa-corpus manifest+shards, legacy
    qa-corpus.json absence, subgraph count vs entry count
 7. sitemap.xml: every <loc> resolves to a file; /ask/ entries reported
 8. favicon / svg references
"""
import json
import os
import re
import sys
from collections import defaultdict
from urllib.parse import unquote, urlsplit

HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.abspath(os.path.join(HERE, ".."))


def _parse_args(argv):
    dist = os.path.join(REPO_ROOT, "website", "dist")
    report = os.path.join(REPO_ROOT, ".staging", "site_audit", "report.md")
    args = list(argv)
    while args:
        a = args.pop(0)
        if a == "--dist" and args:
            dist = os.path.abspath(args.pop(0))
        elif a == "--report" and args:
            report = os.path.abspath(args.pop(0))
        else:
            raise SystemExit(f"unknown argument: {a}")
    return dist, report


DIST, REPORT = _parse_args(sys.argv[1:])

LANGS = ("zh", "en", "ko")
LANG_ROOT = {"zh": "", "en": "en/", "ko": "ko/"}
EXPECTED_REDIRECT = {"zh": "/search/", "en": "/en/search/", "ko": "/ko/search/"}

SKIP_SCHEMES = ("http://", "https://", "//", "mailto:", "tel:", "javascript:",
                "data:", "sms:", "ftp:")

# ---------------------------------------------------------------- findings ---
# severity -> list of (check, message)
findings = {"broken": [], "warn": [], "info": []}


def add(sev, check, msg):
    findings[sev].append((check, msg))


# ------------------------------------------------------------ file helpers ---
def lang_of(rel):
    if rel.startswith("en/"):
        return "en"
    if rel.startswith("ko/"):
        return "ko"
    return "zh"


def resolve_target(page_rel, url):
    """Resolve a site-internal URL to a dist-relative file path, or None."""
    url = url.strip()
    if not url or url.startswith("#"):
        return None
    low = url.lower()
    if low.startswith(SKIP_SCHEMES):
        return None
    url = unquote(url)
    path = urlsplit(url).path
    if not path:
        return None
    if path.startswith("/"):
        cand = path.lstrip("/")
    else:  # relative to the page's directory
        cand = os.path.normpath(os.path.join(os.path.dirname(page_rel), path))
    cand = cand.replace(os.sep, "/")
    if cand.startswith("../"):
        return None
    full = os.path.join(DIST, cand)
    if os.path.isfile(full):
        return cand
    if os.path.isdir(full):
        idx = os.path.join(full, "index.html")
        if os.path.isfile(idx):
            return cand.rstrip("/") + "/index.html"
        return None
    # extension-less path -> try /index.html then .html
    base, ext = os.path.splitext(cand)
    if not ext:
        if os.path.isfile(os.path.join(full, "index.html")):
            return cand + "/index.html"
        if os.path.isfile(full + ".html"):
            return cand + ".html"
    return None


# ------------------------------------------------------------- HTML regexes --
RE_ATTR = re.compile(
    r"""\b(?:href|src|action)\s*=\s*("([^"]*)"|'([^']*)')""", re.I)
RE_DATA_ATTR = re.compile(
    r"""\bdata-[\w-]+\s*=\s*("(/[^"]*)"|'(/[^']*)')""")
RE_SCRIPT_SRC = re.compile(r'<script[^>]*\bsrc\s*=\s*"([^"]+)"', re.I)
RE_INLINE_SCRIPT = re.compile(
    r"<script(?![^>]*\bsrc\s*=)[^>]*>.*?</script>", re.I | re.S)
RE_STYLE = re.compile(r"<style[^>]*>.*?</style>", re.I | re.S)
RE_H1 = re.compile(r"<h1\b([^>]*)>(.*?)</h1>", re.I | re.S)
RE_TAG = re.compile(r"<[^>]+>")
RE_TITLE = re.compile(r"<title[^>]*>(.*?)</title>", re.I | re.S)
RE_LANG = re.compile(r'<html[^>]*\blang\s*=\s*"([^"]*)"', re.I)
RE_REFRESH = re.compile(
    r'<meta[^>]*http-equiv\s*=\s*"refresh"[^>]*content\s*=\s*"[^"]*url\s*=\s*([^"]+)"',
    re.I)

RESIDUE_PATTERNS = [
    ("{{", re.compile(r"\{\{"), "broken"),
    ("{%", re.compile(r"\{%"), "broken"),
    ("[object Object]", re.compile(re.escape("[object Object]")), "broken"),
    (">None<", re.compile(r">\s*None\s*<"), "broken"),
    ('"None" attr', re.compile(r"""[\s(]["']None["'][,)\s]"""), "warn"),
    ("undefined", re.compile(r"\bundefined\b"), "warn"),
    ("NaN", re.compile(r"\bNaN\b"), "warn"),
]


def strip_inline(html):
    html = RE_INLINE_SCRIPT.sub(" ", html)
    return RE_STYLE.sub(" ", html)


# ------------------------------------------------------------------ crawl ----
def collect_html():
    pages = []
    for root, dirs, files in os.walk(DIST):
        dirs.sort()
        for f in files:
            if f.endswith(".html"):
                full = os.path.join(root, f)
                pages.append(os.path.relpath(full, DIST).replace(os.sep, "/"))
    pages.sort()
    return pages


def main():
    if not os.path.isdir(DIST):
        print(f"dist not found: {DIST}")
        sys.exit(2)

    pages = collect_html()
    n_pages = len(pages)
    print(f"[audit] dist={DIST}")
    print(f"[audit] html pages: {n_pages}")

    # aggregated: target -> set(example pages)
    broken_links = defaultdict(set)
    missing_assets = defaultdict(set)
    checked_urls = 0
    script_order_bad = []
    cytoscape_missing = []
    cytoscape_late = []

    for i, rel in enumerate(pages):
        if i % 2000 == 0:
            print(f"[audit] scanning {i}/{n_pages} ...", flush=True)
        with open(os.path.join(DIST, rel), encoding="utf-8") as fh:
            html = fh.read()
        lang = lang_of(rel)

        # ---- 1. links --------------------------------------------------
        urls = []
        for m in RE_ATTR.finditer(html):
            u = m.group(2) if m.group(2) is not None else m.group(3)
            urls.append((u, "attr"))
        for m in RE_DATA_ATTR.finditer(html):
            u = m.group(2) if m.group(2) is not None else m.group(3)
            urls.append((u, "data-attr"))
        for m in RE_REFRESH.finditer(html):
            urls.append((m.group(1), "meta-refresh"))

        for u, kind in urls:
            if u is None:
                continue
            checked_urls += 1
            target = resolve_target(rel, u)
            if target is None:
                # distinguish "external/skipped" from "internal but missing"
                s = u.strip()
                if not s or s.startswith("#") or s.lower().startswith(SKIP_SCHEMES):
                    continue
                path = urlsplit(unquote(s)).path
                if not path:
                    continue
                key = path if path.startswith("/") else \
                    os.path.normpath(os.path.join(os.path.dirname(rel), path))
                if kind == "attr" and re.search(r"\.(js|css|svg|png|jpg|woff2?|ttf|ico)$",
                                                path, re.I):
                    missing_assets[key].add(rel)
                else:
                    broken_links[key].add(rel)

        # ---- 2. script order -------------------------------------------
        srcs = RE_SCRIPT_SRC.findall(html)
        names = [os.path.basename(s) for s in srcs]
        pos = {name: idx for idx, name in enumerate(names)}
        if "ask.js" in pos:
            if "search.js" not in pos:
                script_order_bad.append((rel, "ask.js without search.js"))
            elif pos["search.js"] > pos["ask.js"]:
                script_order_bad.append((rel, "search.js loaded after ask.js"))
        if "graph.js" in pos:
            cyto = [j for j, s in enumerate(srcs) if "cytoscape" in s]
            if not cyto:
                cytoscape_missing.append(rel)
            elif cyto[0] > pos["graph.js"]:
                cytoscape_late.append(rel)
        for s in srcs:
            if s.startswith("/") and resolve_target(rel, s) is None:
                missing_assets[urlsplit(s).path].add(rel)

        # ---- 3. template residue ---------------------------------------
        body = strip_inline(html)
        for label, pat, sev in RESIDUE_PATTERNS:
            for m in pat.finditer(body):
                # ">None<" in an English page is usually a legit table value
                # ("None" = n/a), not a leaked Python None -> downgrade.
                eff = sev
                if label == ">None<" and lang == "en":
                    eff = "warn"
                ctx = body[max(0, m.start() - 40):m.end() + 40]
                ctx = " ".join(ctx.split())
                add(eff, "residue", f"{rel}: `{label}` … {ctx[:140]}")
                break  # one example per page per pattern is enough

        # ---- 4. structure ----------------------------------------------
        h1s = RE_H1.findall(html)
        h1_ids = []
        for attrs, inner in h1s:
            text = RE_TAG.sub("", inner).strip()
            if not text:
                add("broken", "h1", f"{rel}: empty <h1>")
            idm = re.search(r'\bid\s*=\s*"([^"]+)"', attrs)
            if idm:
                h1_ids.append(idm.group(1))
        if not h1s and not rel.endswith("404.html") and "/ask/" not in rel \
                and rel != "ask/index.html":
            add("info", "h1", f"{rel}: no <h1>")
        if len(h1s) > 1:
            add("info", "h1", f"{rel}: {len(h1s)} <h1> elements")
        dup = {x for x in h1_ids if h1_ids.count(x) > 1}
        if dup:
            add("warn", "h1", f"{rel}: duplicate <h1> id(s): {sorted(dup)}")

        lm = RE_LANG.search(html)
        if not lm:
            add("warn", "lang", f"{rel}: missing <html lang>")
        else:
            lv = lm.group(1).lower()
            ok = (lang == "zh" and lv.startswith("zh")) or \
                 (lang == "en" and lv.startswith("en")) or \
                 (lang == "ko" and lv.startswith("ko"))
            if not ok:
                add("broken", "lang",
                    f"{rel}: <html lang=\"{lm.group(1)}\"> but path implies '{lang}'")

        tm = RE_TITLE.search(html)
        if not tm:
            add("broken", "title", f"{rel}: missing <title>")
        else:
            t = tm.group(1).strip()
            if not t:
                add("broken", "title", f"{rel}: empty <title>")
            elif "None" in t:
                add("broken", "title", f"{rel}: <title> contains None: {t[:80]}")

    # ------------------------------------------------ aggregated reports ----
    print(f"[audit] scanning {n_pages}/{n_pages} done")
    print(f"[audit] urls checked: {checked_urls}")

    for target, refs in sorted(broken_links.items()):
        ex = sorted(refs)[:3]
        more = f" (+{len(refs) - 3} more)" if len(refs) > 3 else ""
        sev = "broken"
        # paths only referenced from template-residue pages are still broken
        add(sev, "link404",
            f"{target}  ← {len(refs)} page(s), e.g. {', '.join(ex)}{more}")
    for target, refs in sorted(missing_assets.items()):
        ex = sorted(refs)[:3]
        add("broken", "asset404",
            f"{target}  ← {len(refs)} page(s), e.g. {', '.join(ex)}")
    for rel, why in script_order_bad:
        add("broken", "script-order", f"{rel}: {why}")
    for rel in cytoscape_missing:
        add("broken", "script-order", f"{rel}: graph.js without cytoscape")
    for rel in cytoscape_late:
        add("warn", "script-order", f"{rel}: cytoscape loaded after graph.js")

    # ---- 5. ask redirects ------------------------------------------------
    for lang in LANGS:
        rel = LANG_ROOT[lang] + "ask/index.html"
        full = os.path.join(DIST, rel)
        if not os.path.isfile(full):
            add("broken", "redirect", f"{rel}: missing")
            continue
        html = open(full, encoding="utf-8").read()
        m = RE_REFRESH.search(html)
        want = EXPECTED_REDIRECT[lang]
        if not m:
            add("broken", "redirect", f"{rel}: no meta refresh")
        elif m.group(1).strip() != want:
            add("broken", "redirect",
                f"{rel}: refresh url={m.group(1).strip()} expected {want}")

    # ---- 6. data files ----------------------------------------------------
    for lang in LANGS:
        root = LANG_ROOT[lang]
        entry_dir = os.path.join(DIST, root + "entry")
        n_entries = len([d for d in os.listdir(entry_dir)
                         if os.path.isdir(os.path.join(entry_dir, d))]) \
            if os.path.isdir(entry_dir) else 0

        si = os.path.join(DIST, root + "data/search-index.json")
        if not os.path.isfile(si):
            add("broken", "data", f"{root}data/search-index.json missing")
        else:
            try:
                json.load(open(si, encoding="utf-8"))
            except Exception as e:
                add("broken", "data", f"{root}data/search-index.json: {e}")

        legacy = os.path.join(DIST, root + "data/qa-corpus.json")
        if os.path.isfile(legacy):
            add("warn", "data", f"{root}data/qa-corpus.json still present (legacy)")

        man_path = os.path.join(DIST, root + "data/qa-corpus/manifest.json")
        if not os.path.isfile(man_path):
            add("broken", "data", f"{root}data/qa-corpus/manifest.json missing")
        else:
            try:
                man = json.load(open(man_path, encoding="utf-8"))
                shards = []
                if isinstance(man, dict):
                    for k, v in man.items():
                        if isinstance(v, list):
                            shards += [x for x in v if isinstance(x, str)]
                        elif isinstance(v, str):
                            shards.append(v)
                elif isinstance(man, list):
                    shards = [x for x in man if isinstance(x, str)]
                for sh in sorted(set(shards)):
                    p = os.path.join(DIST, root + "data/qa-corpus", sh)
                    if not os.path.isfile(p):
                        add("broken", "data",
                            f"{root}data/qa-corpus/{sh}: in manifest, missing")
                    else:
                        try:
                            json.load(open(p, encoding="utf-8"))
                        except Exception as e:
                            add("broken", "data",
                                f"{root}data/qa-corpus/{sh}: {e}")
            except Exception as e:
                add("broken", "data", f"{root}data/qa-corpus/manifest.json: {e}")

        sg_dir = os.path.join(DIST, root + "data/subgraphs")
        n_sg = len([f for f in os.listdir(sg_dir) if f.endswith(".json")]) \
            if os.path.isdir(sg_dir) else 0
        if n_entries and n_sg != n_entries:
            add("broken", "data",
                f"{root}data/subgraphs: {n_sg} files vs {n_entries} entries")
        else:
            add("info", "data",
                f"{root}data/subgraphs: {n_sg} files == {n_entries} entries")

        # ---- 8. favicon ---------------------------------------------------
        if not os.path.isfile(os.path.join(DIST, root + "favicon.svg")):
            add("broken", "favicon", f"{root}favicon.svg missing")

    # ---- 7. sitemaps --------------------------------------------------------
    for lang in LANGS:
        rel = LANG_ROOT[lang] + "sitemap.xml"
        full = os.path.join(DIST, rel)
        if not os.path.isfile(full):
            add("warn", "sitemap", f"{rel}: missing")
            continue
        xml = open(full, encoding="utf-8").read()
        locs = re.findall(r"<loc>\s*([^<]+?)\s*</loc>", xml)
        bad, ask_urls = [], []
        for loc in locs:
            path = urlsplit(loc).path
            if re.match(r"^/(en/)?(ko/)?ask/?$", path):
                ask_urls.append(path)
            fake_page = rel  # absolute paths resolve from dist root
            if resolve_target(fake_page, path) is None:
                bad.append(path)
        for p in bad[:20]:
            add("broken", "sitemap", f"{rel}: URL 404 → {p}")
        if len(bad) > 20:
            add("broken", "sitemap", f"{rel}: … and {len(bad) - 20} more 404 URLs")
        if ask_urls:
            add("info", "sitemap",
                f"{rel}: {len(ask_urls)} /ask/ URL(s) kept (redirect pages): "
                + ", ".join(sorted(set(ask_urls))))
        add("info", "sitemap",
            f"{rel}: {len(locs)} URLs, {len(bad)} broken")

    # ------------------------------------------------------------- report ----
    write_report(n_pages, checked_urls)
    b, w, i = (len(findings["broken"]), len(findings["warn"]),
               len(findings["info"]))
    print(f"\n[audit] DONE  broken={b}  warn={w}  info={i}")
    print(f"[audit] report: {REPORT}")
    return 0 if b == 0 else 1


def write_report(n_pages, checked_urls):
    lines = []
    lines.append("# Site Audit Report — website/dist\n")
    lines.append(f"- HTML pages scanned: **{n_pages}**")
    lines.append(f"- URLs/attrs checked: **{checked_urls}**")
    lines.append(f"- broken: **{len(findings['broken'])}** · "
                 f"warn: **{len(findings['warn'])}** · "
                 f"info: **{len(findings['info'])}**\n")
    for sev in ("broken", "warn", "info"):
        lines.append(f"\n## {sev.upper()} ({len(findings[sev])})\n")
        by_check = defaultdict(list)
        for check, msg in findings[sev]:
            by_check[check].append(msg)
        for check in sorted(by_check):
            msgs = by_check[check]
            lines.append(f"### {check} ({len(msgs)})\n")
            limit = len(msgs) if sev == "broken" else min(len(msgs), 30)
            for m in msgs[:limit]:
                lines.append(f"- {m}")
            if len(msgs) > limit:
                lines.append(f"- … and {len(msgs) - limit} more")
            lines.append("")
    with open(REPORT, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))


if __name__ == "__main__":
    sys.exit(main())
