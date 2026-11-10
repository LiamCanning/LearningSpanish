#!/usr/bin/env python3
"""
Aprende pre-deploy validator.
Catches the two classes of bug that have broken the app:
  1. Sparse array holes  (double comma: },  ,{)
  2. Unescaped apostrophes inside single-quoted JS string values
     in data fields (en:', notes:', hint:', titleEn:', setting:', context:', intro:')

Usage: python3 scripts/validate.py [path/to/index.html]
Exits 0 if clean, 1 if issues found.
"""

import re, sys

path = sys.argv[1] if len(sys.argv) > 1 else "index.html"

with open(path, "r", encoding="utf-8") as f:
    content = f.read()
    lines = content.splitlines()

errors = []

# --- Check 1: sparse array holes ---
holes = [(m.start(), m.group()) for m in re.finditer(r'},\s*,\s*{', content)]
for pos, match in holes:
    line_num = content[:pos].count('\n') + 1
    errors.append(f"Line {line_num}: SPARSE ARRAY HOLE — double comma: {match!r}")

# --- Check 2: unescaped apostrophes in single-quoted data fields ---
# Only flag lines where the field uses single quotes (not double quotes or backticks).
# Pattern: field name, colon, optional space, then single-quote opening the value.
# We skip lines where the same field uses a double-quote opener.
field_pat = re.compile(
    r"""\b(en|notes|hint|titleEn|setting|context|intro|answer|question)\s*:\s*'"""
)
contraction = re.compile(r"[a-zA-Z]'[a-zA-Z]")

for i, line in enumerate(lines, 1):
    if not field_pat.search(line):
        continue
    # Mask already-properly-escaped apostrophes so they don't interfere
    check = line.replace("\\'", "##")
    if contraction.search(check):
        # Confirm the field on this line actually uses single quotes
        # (exclude lines where every matching field uses double quotes or backticks)
        has_single_quoted = bool(re.search(
            r'''\b(?:en|notes|hint|titleEn|setting|context|intro|answer|question)\s*:\s*'[^"]*[a-zA-Z]'[a-zA-Z]''',
            check
        ))
        if has_single_quoted:
            matches = contraction.findall(check)
            errors.append(
                f"Line {i}: UNESCAPED APOSTROPHE in single-quoted field — "
                f"patterns {matches} — {line.strip()[:100]}"
            )

# --- Report ---
if errors:
    print(f"VALIDATION FAILED — {len(errors)} issue(s):\n")
    for e in errors:
        print(f"  {e}")
    sys.exit(1)
else:
    print(f"OK — validated {len(lines)} lines, no issues found.")
    sys.exit(0)
