# AITIR Framework 2.0

**Adaptive Identity-and-access Threat Intelligence and Response**

[![Release](https://img.shields.io/github/v/release/sajjad47/AITIR-Framework?display_name=tag&sort=semver)](https://github.com/sajjad47/AITIR-Framework/releases/latest)
[![Repository validation](https://github.com/sajjad47/AITIR-Framework/actions/workflows/validate.yml/badge.svg)](https://github.com/sajjad47/AITIR-Framework/actions/workflows/validate.yml)
[![Documentation](https://img.shields.io/badge/docs-GitHub%20Pages-0f766e)](https://sajjad47.github.io/AITIR-Framework/)
[![Status](https://img.shields.io/badge/status-reference%20architecture-f59e0b)](docs/status-and-limitations.md)
[![License](https://img.shields.io/badge/license-research%20%26%20educational-64748b)](LICENSE.md)

AITIR Version 2.0 is a vendor-neutral reference architecture for converting identity-centered security telemetry into provenance-linked evidence, a bounded policy decision, an authorized response, and independently reviewable assurance.

> **Evidence in, authority out:** analytics produce evidence; authorized policy decides; enforcement acts; assurance verifies.

A model score, anomaly label, graph rank, indicator match, or generated recommendation never grants itself response authority.

## Release status

**AITIR 2.0 is a reference architecture and research preview, not a production product or certification.** This repository supplies Level L0 documentation and selected L1 conformance artifacts. It does not claim agency deployment, legal sufficiency, NIST/CISA approval, model accuracy in a live organization, or authority to automate consequential actions.

- **Current version:** [`2.0.0`](VERSION)
- **Latest release:** [`v2.0.0`](https://github.com/sajjad47/AITIR-Framework/releases/tag/v2.0.0)
- **Documentation:** [sajjad47.github.io/AITIR-Framework](https://sajjad47.github.io/AITIR-Framework/)
- **Changelog:** [`CHANGELOG.md`](CHANGELOG.md)
- **Release procedure:** [`docs/release-process.md`](docs/release-process.md)

The repository's historical tag is `v0.1`; no formal `v1.0.0` tag existed. Version 2 refers to the pre-2.0 four-layer material as the **Version 1 conceptual baseline** for migration purposes without rewriting Git history.

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

![AITIR Framework 2.0 seven-plane architecture](docs/assets/aitir-framework-architecture.png)

## Quick start

AITIR is documentation and conformance tooling, not an installable security service. To evaluate the framework:

1. Read the [Version 2 Specification](docs/version-2-specification.md) and [Status and Limitations](docs/status-and-limitations.md).
2. Compare the [event](schemas/aitir-event-v2.schema.json), [evidence](schemas/aitir-evidence-v2.schema.json), and [decision](schemas/aitir-decision-v2.schema.json) contracts with their JSON examples.
3. Inspect the corrected [synthetic events](examples/synthetic-identity-events.csv) and [risk output](examples/sample-risk-output.csv).
4. Run the offline validator:

   ```bash
   python3 scripts/validate_repository.py
   ```

5. Run the complete pinned validation toolchain with [uv](https://docs.astral.sh/uv/):

   ```bash
   uv run --with-requirements requirements-dev.txt python scripts/validate_repository.py --jsonschema
   uv run --with-requirements requirements-dev.txt python scripts/verify_generated_artifacts.py
   ```

These checks establish repository conformance, not detection effectiveness or deployment safety.

## Documentation map

| Area | Primary references |
|---|---|
| Normative architecture | [Specification](docs/version-2-specification.md), [Technical Overview](docs/technical-overview.md), [Architecture](docs/architecture.md) |
| Contracts and authority | [Data Contracts](docs/data-contracts.md), [Response Authority](docs/response-authority.md), [`schemas/`](schemas/) |
| Standards | [Standards Crosswalk](docs/standards-crosswalk.md), [NIST RMF Alignment](docs/nist-rmf-alignment.md) |
| Evaluation | [Proof of Concept](docs/proof-of-concept.md), [Risk Model](docs/sample-risk-scoring-model.md), [Pilot Protocol](docs/pilot-evaluation-protocol.md) |
| Evidence and maturity | [Status and Limitations](docs/status-and-limitations.md), [Research and Publications](docs/research-and-publications.md), [Research Ledger](research/version-2-research-ledger.md) |
| Adoption | [Use Cases](docs/use-cases.md), [Migration Guide](docs/migration-v1-to-v2.md), [Roadmap](docs/roadmap.md) |
| Governance | [Contributing](CONTRIBUTING.md), [Security](SECURITY.md), [Code of Conduct](CODE_OF_CONDUCT.md), [Release Process](docs/release-process.md) |

## Repository structure

```text
.github/              CI, dependency updates, issue forms, and PR template
docs/                 Specification, architecture, governance, and Pages site
examples/             Synthetic CSV and JSON conformance examples
public-materials/     Generated review PDFs and their HTML sources
research/             Version 2 standards and literature provenance ledger
schemas/              Draft 2020-12 event, evidence, and decision schemas
scripts/              Deterministic build and validation tools
ARTIFACTS.sha256      Release-artifact integrity manifest
CITATION.cff          Machine-readable citation metadata
VERSION               Canonical semantic version
```

## Public review materials

- [AITIR Technical Exhibit](public-materials/AITIR-Technical-Exhibit.pdf)
- [AITIR Future Development Plan](public-materials/AITIR-Future-Development-Plan.pdf)
- [Architecture diagram](docs/assets/aitir-framework-architecture.png)
- [Artifact hashes](ARTIFACTS.sha256)

Generated materials have source-controlled HTML and pinned build instructions. See [Public Materials](docs/public-materials.md).

## Evaluation boundary

The 12-row example demonstrates schema, identifier, score-tier, and workflow consistency only. It has no ground-truth attack labels and cannot support claims about detection accuracy, false positives, calibration, operational safety, or return on investment.

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

## Contributing and security

Use the structured issue forms and follow [`CONTRIBUTING.md`](CONTRIBUTING.md). Pull requests must pass the repository-validation workflow and preserve the evidence, authority, privacy, and publication-status boundaries.

Do not open a public issue for credentials, privacy exposure, unsafe response paths, or exploitable implementation details. Use [private vulnerability reporting](https://github.com/sajjad47/AITIR-Framework/security/advisories/new) and read [`SECURITY.md`](SECURITY.md).

## Citation

> Hossain, M. S. (2026). *AITIR Framework: Adaptive Identity-and-access Threat Intelligence and Response* (Version 2.0.0) [Reference architecture and documentation]. https://github.com/sajjad47/AITIR-Framework

Machine-readable metadata is in [`CITATION.cff`](CITATION.cff).

## Responsible use

Before any operational implementation, obtain local security authorization; privacy, legal, records, labor, accessibility, and continuity review; independent assessment; and tested rollback. Keep analytics outside the enforcement trust root. Do not use synthetic examples or manuscript results as evidence that an implementation is safe for real people or essential services.

## License

See [`LICENSE.md`](LICENSE.md). External standards, publications, datasets, and referenced software retain their own terms.
