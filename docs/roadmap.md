# AITIR 2.0 Roadmap

**Version:** 2.0.0

The roadmap advances evidence maturity rather than feature volume. Progression is gated by safety, reproducibility, privacy, authority, continuity, and independent review.

## Completed for Version 2.0

- formal semantic version and canonical acronym expansion;
- seven-plane architecture and trust boundaries;
- event, evidence, and decision JSON Schemas;
- T0-T3 decision tiers and explicit abstention;
- stateful response-authority model and twelve guard categories;
- standards and interoperability crosswalk;
- Version 1 migration guide;
- corrected synthetic example and automated consistency validation;
- research ledger with evidence hierarchy and publication status;
- updated public technical and future-development materials.

## 2.0.x: Documentation hardening

- collect external architecture and policy review;
- resolve reported documentation and schema issues;
- publish machine-readable crosswalk tables;
- add schema examples for CAEP/RISC, STIX/TAXII, OCSF, and CACAO mappings;
- add decision-table and state-machine conformance vectors;
- establish release signing and provenance for generated PDFs and diagrams.

**Exit gate:** all examples validate; no unresolved high-severity documentation ambiguity; release artifacts reproduce from source.

## 2.1: Reference implementation

- build a local-only reference pipeline with synthetic data;
- implement event -> evidence -> decision interfaces as separate services or privilege domains;
- add deterministic rules, simple anomaly baseline, and explicit out-of-domain behavior;
- implement policy-as-code tests without production connectors;
- add immutable decision records, idempotency, and simulated rollback;
- publish SBOM, threat model, and model/data cards.

**Exit gate:** full automated tests; independent code review; no analytics principal has enforcement credentials.

## 2.2: Offline research harness

- support chronological replay and leakage-safe partitioning;
- implement calibration, coverage-risk, abstention, and queue-cost analysis;
- add identity-graph relation confidence and remediation ranking;
- test source loss, clock drift, schema drift, identity ambiguity, poisoning, evasion, and prompt injection;
- add uncertainty intervals and attack-family reporting.

**Exit gate:** reproducible benchmark outputs with frozen protocol and evidence boundaries.

## 2.3: Controlled pilot package

- develop privacy impact, civil-rights, records, labor, accessibility, and continuity templates;
- define local decision-rights and T0-T3 action catalog;
- provide tabletop, offline replay, and shadow-mode procedures;
- instrument analyst queue, disagreement, override, aging, and burden;
- add connector simulators and fault injection;
- define independent assessment and pilot exit criteria.

**Exit gate:** architecture review and authorized shadow mode; no live state-changing automation.

## 3.0 consideration

Version 3 will be considered only after evidence from controlled pilots identifies stable requirements that cannot be added compatibly. A major release would require demonstrated need for contract, authority, or state-machine incompatibility, not marketing cadence.

## Non-goals

The roadmap does not target:

- unrestricted autonomous response;
- elimination of human responsibility;
- silent continuous self-training;
- replacing identity providers, SIEM, SOAR, case management, or RMF authorization;
- collecting real personal or classified data in this public repository;
- claiming compliance or operational benefit without assessment evidence.

## Contribution priorities

1. contradictory or unsafe requirements;
2. schema and example conformance;
3. threat-model and trust-boundary gaps;
4. policy/state-machine tests;
5. reproducibility and measurement quality;
6. interoperability mappings;
7. implementation convenience.
