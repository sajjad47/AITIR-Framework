# AITIR 2.0 Public Materials

**Version:** 2.0.0

The `public-materials/` directory contains generated PDFs intended for external technical or planning review.

## Current files

- [`AITIR-Technical-Exhibit.pdf`](../public-materials/AITIR-Technical-Exhibit.pdf)
  Version 2 architecture, contracts, trust boundaries, decision tiers, evidence limits, and standards mapping.

- [`AITIR-Future-Development-Plan.pdf`](../public-materials/AITIR-Future-Development-Plan.pdf)
  Evidence-gated development plan from documentation hardening through a reference implementation and controlled pilot package.

## Source and reproducibility

The PDFs are generated from:

- [`../public-materials/src/AITIR-Technical-Exhibit.html`](../public-materials/src/AITIR-Technical-Exhibit.html)
- [`../public-materials/src/AITIR-Future-Development-Plan.html`](../public-materials/src/AITIR-Future-Development-Plan.html)
- [`../scripts/build_public_materials.py`](../scripts/build_public_materials.py)

Rebuild with:

```bash
uv run --with-requirements requirements-dev.txt python scripts/build_architecture.py
uv run --with-requirements requirements-dev.txt python scripts/build_public_materials.py
```

The repository validator checks that the PDFs contain Version 2.0 markers and verifies their hashes against [`../ARTIFACTS.sha256`](../ARTIFACTS.sha256).

## Use boundary

These materials may support architecture review, research discussion, grant or professional-development evidence, and controlled-pilot planning. They are not proof of implementation, field performance, agency endorsement, compliance, legal sufficiency, or employment/immigration eligibility.

## External submission caution

Before using a PDF externally:

- check the receiving organization's current rules;
- verify that claims and publication statuses remain current;
- preserve exact filenames and hashes where evidence integrity matters;
- avoid presenting standards alignment as certification;
- do not include secrets, personal telemetry, protected records, or restricted agency information.
