#!/usr/bin/env python3
"""Verify the structure and presentation signals of generated AITIR artifacts."""

from __future__ import annotations

from pathlib import Path

import fitz
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
ARCHITECTURE = ROOT / "docs/assets/aitir-framework-architecture.png"
PDFS = {
    ROOT / "public-materials/AITIR-Technical-Exhibit.pdf": {
        "title": "AITIR 2.0 Technical Exhibit",
        "pages": 6,
        "minimum_words": 1100,
    },
    ROOT / "public-materials/AITIR-Future-Development-Plan.pdf": {
        "title": "AITIR 2.0 Future Development Plan",
        "pages": 6,
        "minimum_words": 1300,
    },
}

errors: list[str] = []
checks = 0


def check(condition: bool, message: str) -> None:
    global checks
    checks += 1
    if not condition:
        errors.append(message)


with Image.open(ARCHITECTURE) as image:
    check(image.format == "PNG", "architecture artifact is not PNG")
    check(image.size == (1920, 1080), f"architecture dimensions are {image.size}")
    check(image.mode in {"RGB", "RGBA"}, f"architecture color mode is {image.mode}")

for path, expected in PDFS.items():
    document = fitz.open(path)
    check(
        len(document) == expected["pages"], f"{path.name} page count is {len(document)}"
    )
    check(
        document.metadata.get("title") == expected["title"],
        f"{path.name} title metadata mismatch",
    )
    check(
        document.metadata.get("producer") == "WeasyPrint 69.0",
        f"{path.name} producer is not pinned WeasyPrint 69.0",
    )

    all_text = "\n".join(page.get_text() for page in document)
    check("Version 2.0" in all_text, f"{path.name} lacks Version 2.0 text")
    check(
        len(all_text.split()) >= expected["minimum_words"],
        f"{path.name} text is unexpectedly short",
    )

    for number, page in enumerate(document, start=1):
        check(
            abs(page.rect.width - 612) < 0.5,
            f"{path.name} page {number} is not US Letter width",
        )
        check(
            abs(page.rect.height - 792) < 0.5,
            f"{path.name} page {number} is not US Letter height",
        )
        check(
            len(page.get_text().split()) >= 20,
            f"{path.name} page {number} may be blank",
        )
        check(
            bool(page.get_fonts(full=True)),
            f"{path.name} page {number} has no embedded font resources",
        )

if errors:
    print(f"FAIL: {len(errors)} generated-artifact error(s) across {checks} checks")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print(f"PASS: {checks} generated-artifact checks")
