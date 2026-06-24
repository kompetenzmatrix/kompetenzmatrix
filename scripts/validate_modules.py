#!/usr/bin/env python3
"""CI validation gate for competency-module bundles.

Enforces the EHB rules on every content/<cluster>/<module>/_index.md:
  - non-ÜK modules must have at least one Kompetenzband
  - every band needs id (uppercase) + titel + at least one Kompetenz
  - every Kompetenz needs nr, hz, and all three levels (Grundlagen/Fortgeschritten/Erweitert)
  - every level text must start with "Ich kann"
Exits non-zero on any violation (fails the PR check).
"""
import glob, os, re, sys
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LEVELS = ('grundlagen', 'fortgeschritten', 'erweitert')

def load_frontmatter(path):
    text = open(path, encoding='utf-8').read()
    if not text.startswith('---'):
        return None
    end = text.find('\n---', 3)
    if end == -1:
        return None
    return yaml.safe_load(text[3:end])

def check(path):
    errs = []
    fm = load_frontmatter(path)
    rel = os.path.relpath(path, ROOT)
    if fm is None:
        return [f"{rel}: no YAML frontmatter"]
    if fm.get('uek'):
        return []  # ÜK modules legitimately have no matrix
    baender = fm.get('kompetenzbaender')
    if not baender:
        return [f"{rel}: no kompetenzbaender (set uek: true if this is an ÜK module)"]
    for b in baender:
        bid = b.get('id', '?')
        if not re.match(r'^[A-Z]+$', str(b.get('id', ''))):
            errs.append(f"{rel}: band id {bid!r} must be uppercase letters")
        if not b.get('titel'):
            errs.append(f"{rel}: band {bid} missing titel")
        komps = b.get('kompetenzen') or []
        if not komps:
            errs.append(f"{rel}: band {bid} has no kompetenzen")
        for k in komps:
            nr = k.get('nr')
            if not isinstance(nr, int):
                errs.append(f"{rel}: band {bid} kompetenz nr {nr!r} must be an integer")
            # hz (Handlungsziele) may legitimately be empty for some rows — not required
            for lvl in LEVELS:
                txt = (k.get(lvl) or '').strip()
                if not txt:
                    errs.append(f"{rel}: band {bid}{nr} missing {lvl}")
                elif not txt.startswith('Ich kann'):
                    errs.append(f"{rel}: band {bid}{nr} {lvl} must start with 'Ich kann': {txt[:40]!r}")
    return errs

def main():
    files = glob.glob(os.path.join(ROOT, 'content', '*', '*', '_index.md'))
    all_errs = []
    for f in sorted(files):
        all_errs += check(f)
    if all_errs:
        print(f"VALIDATION FAILED ({len(all_errs)} issue(s)):")
        for e in all_errs:
            print("  -", e)
        sys.exit(1)
    print(f"OK: {len(files)} module bundles valid.")

if __name__ == '__main__':
    main()
