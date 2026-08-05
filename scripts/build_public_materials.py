#!/usr/bin/env python3
"""Build AITIR Version 2 public PDFs from source-controlled HTML."""

from __future__ import annotations

import hashlib
from pathlib import Path

from weasyprint import HTML

ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "public-materials/src"
OUTPUT_DIR = ROOT / "public-materials"
NAMES = ["AITIR-Technical-Exhibit", "AITIR-Future-Development-Plan"]

for name in NAMES:
    source = SOURCE_DIR / f"{name}.html"
    output = OUTPUT_DIR / f"{name}.pdf"
    if not source.exists():
        raise SystemExit(f"missing source: {source}")
    HTML(filename=str(source), base_url=str(SOURCE_DIR)).write_pdf(
        str(output),
        full_fonts=True,
        pdf_identifier=f"AITIR-2.0.0-{name}",
    )
    digest = hashlib.sha256(output.read_bytes()).hexdigest()
    print(
        f"built {output.relative_to(ROOT)} ({output.stat().st_size} bytes, sha256:{digest})"
    )
