# Pull request

## Summary

<!-- Explain the problem, the bounded change, and why it belongs in AITIR. -->

## Evidence boundary

<!-- Distinguish architecture propositions, standards requirements, published or submitted findings, reproduced results, and operational evidence. -->

## Technical impact

- Affected planes/contracts:
- Compatibility level: patch / minor / major
- Authority or guard impact:
- Privacy, continuity, and rollback impact:

## Validation

- [ ] `python3 scripts/validate_repository.py`
- [ ] `uv run --with-requirements requirements-dev.txt python scripts/validate_repository.py --jsonschema`
- [ ] Python and Markdown lint pass
- [ ] Generated sources and outputs were updated together
- [ ] Diagrams/PDFs were visually inspected when changed
- [ ] `ARTIFACTS.sha256` matches all listed artifacts
- [ ] No credentials, personal telemetry, confidential data, or protected records were added
- [ ] Synthetic or submitted-study findings are not described as production or accepted evidence
- [ ] Standards mappings are not described as certification, compliance, or endorsement

## Sources

<!-- List authoritative URLs, standards versions, DOI records, and access dates. -->
