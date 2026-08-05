#!/usr/bin/env python3
"""Render the inline SVG architecture source to the checked-in PNG."""

from __future__ import annotations

import hashlib
import re
from pathlib import Path

import cairosvg

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "docs/assets/aitir-framework-architecture.html"
OUTPUT = ROOT / "docs/assets/aitir-framework-architecture.png"

html = SOURCE.read_text(encoding="utf-8")
match = re.search(r"(<svg\b.*?</svg>)", html, flags=re.DOTALL | re.IGNORECASE)
if not match:
    raise SystemExit("No inline SVG found in architecture source")

cairosvg.svg2png(
    bytestring=match.group(1).encode("utf-8"),
    write_to=str(OUTPUT),
    output_width=1920,
    output_height=1080,
)
digest = hashlib.sha256(OUTPUT.read_bytes()).hexdigest()
print(
    f"built {OUTPUT.relative_to(ROOT)} ({OUTPUT.stat().st_size} bytes, sha256:{digest})"
)
