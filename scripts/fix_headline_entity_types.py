#!/usr/bin/env python3
"""Fix mis-typed headline entities (company/component -> report) and re-link.

Eight zero-degree entities are news articles whose type was mis-classified
(e.g. a company card named "DexRobot Unveils Full Dexterous Hand Series...").
Report-type cards legitimately carry headline names, so the factual fix is
re-typing, not renaming. Everything else about the files is left untouched.

Usage:
    python scripts/fix_headline_entity_types.py            # dry-run
    python scripts/fix_headline_entity_types.py --write
"""
from __future__ import annotations

import argparse
import json
import re
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TODAY = date.today().isoformat()

# entity_id -> (current wrong type, correct type)
RETYPES = {
    "ent_company_carnegie_mellon_university_sel_2026": ("company", "report"),
    "ent_company_danish_robotics_startup_enters_2026": ("company", "report"),
    "ent_company_deepx_and_sixfab_launch_deepx_2026": ("company", "report"),
    "ent_company_dexrobot_unveils_full_dexterou_2026": ("company", "report"),
    "ent_company_hippo_harvest_closes_30_millio_2026": ("company", "report"),
    "ent_company_indro_robotics_launches_axiom_2026": ("company", "report"),
    "ent_company_x_square_robot_secures_four_co_2026": ("company", "report"),
    "ent_component_harmonic_drive_advances_surgic_2026": ("component", "report"),
}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()

    changed = []
    for eid, (wrong, right) in RETYPES.items():
        matches = list(ROOT.glob(f"research/**/{eid}.md"))
        if not matches:
            print(f"MISSING: {eid}")
            continue
        path = matches[0]
        text = path.read_text(encoding="utf-8")
        if f"type: {right}\n" in text.split("---")[1] if text.startswith("---") else False:
            print(f"already {right}: {eid}")
            continue
        m = re.match(r"(\A---\n.*?\n)(---\n.*\Z)", text, re.S)
        if not m:
            print(f"NO FRONTMATTER: {eid}")
            continue
        fm_text, rest = m.group(1), m.group(2)
        if f"type: {wrong}" not in fm_text:
            print(f"UNEXPECTED TYPE in {eid}: {re.search(r'type: (.*)', fm_text).group(1)}")
            continue
        new_fm = fm_text.replace(f"type: {wrong}", f"type: {right}", 1)
        # annotate the verification notes additively for traceability
        if "notes:" in new_fm:
            new_fm = re.sub(
                r"(notes:.*?)(\n(?=\S))", r"\1" + f" [retyped {wrong}->{right} on {TODAY} by fix_headline_entity_types.py]" + r"\2",
                new_fm, count=1, flags=re.S,
            )
        if args.write:
            path.write_text(new_fm + rest, encoding="utf-8")
        changed.append({"id": eid, "from": wrong, "to": right, "path": str(path)})
        print(f"{'retyped' if args.write else 'would retype'}: {eid} ({wrong} -> {right})")

    manifest = ROOT / ".staging" / f"retype_manifest_{TODAY}.json"
    if args.write and changed:
        manifest.parent.mkdir(exist_ok=True)
        manifest.write_text(json.dumps(changed, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"manifest: {manifest}")


if __name__ == "__main__":
    main()
