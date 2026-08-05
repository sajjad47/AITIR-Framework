# AITIR Framework 2.0

**Adaptive Identity-and-access Threat Intelligence and Response**

[![Version](https://img.shields.io/badge/version-2.0.0-2563eb)](VERSION)
[![Status](https://img.shields.io/badge/status-reference%20architecture-f59e0b)](docs/status-and-limitations.md)
[![License](https://img.shields.io/badge/license-research%20%26%20educational-64748b)](LICENSE.md)

AITIR Version 2.0 is a vendor-neutral reference architecture for converting identity-centered security telemetry into provenance-linked evidence, a bounded policy decision, an authorized response, and independently reviewable assurance.

> **Evidence in, authority out:** analytics produce evidence; authorized policy decides; enforcement acts; assurance verifies.

A model score, anomaly label, graph rank, indicator match, or generated recommendation never grants itself response authority.

## Version 2 at a glance

Version 2 replaces the early four-layer conceptual pipeline with seven interacting planes:

1. Governance, risk, and policy
2. Identity, asset, and telemetry fabric
3. AITIR analytics
4. Risk decision and authorization
5. Response orchestration and case management
6. Assurance, model risk, and audit
7. Resilience and continuity

It adds:

- explicit trust boundaries and least-privileged interfaces;
- separate event, evidence, decision, action, outcome, and feedback contracts;
- calibrated uncertainty and abstention as first-class decision states;
- T0-T3 response tiers with named authority and mandatory safeguards;
- stateful response guards, expiration, idempotency, failure refresh, and rollback;
- controlled graph-remediation decision support under observation uncertainty;
- protected feedback and model/policy release gates;
- current standards mappings and machine-validatable JSON Schemas;
- corrected, automatically checked synthetic examples;
- a clear evidence boundary between documentation, synthetic research, pilot evidence, and production assurance.

## Status

**AITIR 2.0 is a reference architecture and research preview, not a production product or certification.** This repository supplies Level L0 documentation and selected L1 conformance artifacts. It does not claim agency deployment, legal sufficiency, NIST/CISA approval, model accuracy in a live organization, or authority to automate consequential actions.

The repository's historical tag is `v0.1`; no formal `v1.0.0` tag existed. Version 2 refers to the pre-2.0 four-layer material as the **Version 1 conceptual baseline** for migration purposes without rewriting Git history.

## Start here

- [Version 2 Specification](docs/version-2-specification.md)
- [Technical Overview](docs/technical-overview.md)
- [Architecture](docs/architecture.md)
- [Data Contracts](docs/data-contracts.md)
- [Response Authority](docs/response-authority.md)
- [Standards Crosswalk](docs/standards-crosswalk.md)
- [Migration from Version 1](docs/migration-v1-to-v2.md)
- [Status and Limitations](docs/status-and-limitations.md)
- [Roadmap](docs/roadmap.md)

## Evaluation and examples

- [Synthetic Proof of Concept](docs/proof-of-concept.md)
- [Reference Risk Scoring Model](docs/sample-risk-scoring-model.md)
- [Pilot Evaluation Protocol](docs/pilot-evaluation-protocol.md)
- [`examples/synthetic-identity-events.csv`](examples/synthetic-identity-events.csv)
- [`examples/sample-risk-output.csv`](examples/sample-risk-output.csv)
- JSON Schemas in [`schemas/`](schemas/)
- Release-artifact hashes in [`ARTIFACTS.sha256`](ARTIFACTS.sha256)

The 12-row example demonstrates schema, identifier, score-tier, and workflow consistency only. It has no ground-truth attack labels and cannot support claims about detection accuracy, false positives, calibration, operational safety, or return on investment.

## Research modules

Version 2 integrates four clearly bounded AITIR research streams:

- seven-plane public-sector architecture and governance;
- calibrated selective scoring and abstention under temporal shift;
- uncertainty-aware, cost-constrained identity-graph remediation;
- explicit-state response-authority verification.

See [Research and Publications](docs/research-and-publications.md) and the [Version 2 Research Ledger](research/version-2-research-ledger.md). Submitted manuscripts are labeled as submitted, not accepted.

## Standards and interoperability

AITIR maps to NIST CSF 2.0, RMF, SP 800-53/53A, SP 800-207, SP 800-63-4, SP 800-61 Rev. 3, AI RMF, CISA Zero Trust Maturity Model 2.0, MITRE ATT&CK, OCSF, STIX/TAXII 2.1, CACAO 2.0, and OpenID CAEP/RISC 1.0.

These are mappings, not compliance or endorsement claims.

## Intended users

- public-sector and regulated-environment security architects;
- identity, zero-trust, SOC, incident-response, and governance teams;
- researchers evaluating calibrated, explainable, and bounded response;
- assessors and procurement teams seeking inspectable evidence rather than generic “AI-powered” claims.

## Repository validation

Run:

```bash
python3 scripts/validate_repository.py
```

For full JSON Schema validation:

```bash
uv run --with jsonschema python scripts/validate_repository.py --jsonschema
```

## Citation

> Hossain, M. S. (2026). *AITIR Framework: Adaptive Identity-and-access Threat Intelligence and Response* (Version 2.0.0) [Reference architecture and documentation]. https://github.com/sajjad47/AITIR-Framework

Machine-readable metadata is in [`CITATION.cff`](CITATION.cff).

## Responsible use

Before any operational implementation, obtain local security authorization; privacy, legal, records, labor, accessibility, and continuity review; independent assessment; and tested rollback. Keep analytics outside the enforcement trust root. Do not use synthetic examples or manuscript results as evidence that an implementation is safe for real people or essential services.

## License

See [`LICENSE.md`](LICENSE.md). External standards, publications, datasets, and referenced software retain their own terms.
