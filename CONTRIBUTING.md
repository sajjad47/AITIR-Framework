# Contributing to AITIR

AITIR welcomes technically rigorous documentation, schema, validation, evaluation, and reference-implementation contributions.

## Core rules

1. Preserve **evidence in, authority out**. Analytics must not authorize their own response.
2. Distinguish standards requirements, architectural propositions, published findings, submitted findings, reproduced results, and operational evidence.
3. Do not use real credentials, personal telemetry, classified information, protected records, or confidential agency details.
4. Do not describe synthetic or simulated outcomes as field validation.
5. Do not describe submitted manuscripts as accepted.
6. Do not describe standards alignment as certification, compliance, or endorsement.
7. Add or update tests for every schema, scoring, state, guard, count, link, or generated-artifact change.
8. Preserve semantic versioning and document breaking changes.

## Workflow

1. Open or reference an issue that states the problem and evidence boundary.
2. Create a focused branch.
3. Update source documentation and generated artifacts together.
4. Run:

   ```bash
   python3 scripts/validate_repository.py
   uv run --with jsonschema python scripts/validate_repository.py --jsonschema
   ```

5. Rebuild public PDFs if their sources change:

   ```bash
   uv run --with weasyprint python scripts/build_public_materials.py
   ```

6. Review the Git diff for unsupported claims, secrets, personal data, and accidental binary changes.
7. Include source URLs/DOIs and access/version dates for material technical claims.

## Documentation style

- define terms before using acronyms;
- use precise claim verbs: proposes, maps, reports, reproduces, validates, or demonstrates;
- state what a metric or test does not establish;
- keep risk score, probability, uncertainty, impact, and authority distinct;
- use stable reason codes plus human-readable explanation;
- describe failure and degraded behavior, not only the happy path;
- make tables and diagrams traceable to text and machine artifacts.

## Schema changes

Patch versions may clarify validation without changing meaning. Minor versions may add optional backward-compatible fields. Required-field or semantic changes require a major version. Consumers must not silently accept unknown major versions.

## Research contributions

Provide protocol, source selection, data/license provenance, code/environment, hashes, analysis plan, uncertainty, negative findings, and external-validity limits. For human or organizational data, provide evidence of applicable approval and do not commit restricted data.

## Generated files

Generated PDFs and images must have source files and reproducible build instructions. After generation, verify page count, text markers, clipping, fonts, links where supported, and hashes.

## License

By contributing, you agree that your contribution is distributed under the repository license and that external material remains under its original terms.
