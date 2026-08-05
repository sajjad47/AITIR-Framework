# Changelog

All notable repository changes are documented here. AITIR uses semantic versioning from Version 2 onward.

## [2.0.0] - 2026-08-05

### Added

- formal `VERSION` file and Version 2 specification;
- canonical expansion: Adaptive Identity-and-access Threat Intelligence and Response;
- seven-plane architecture with explicit trust zones;
- Version 2 event, evidence, and decision JSON Schemas;
- T0-T3 action tiers, abstention, response states, and twelve guard categories;
- data contracts, standards crosswalk, and Version 1 migration guide;
- research ledger with evidence hierarchy and verified publication status;
- security and contribution guidance;
- repository validation and reproducible public-material build scripts;
- source-controlled architecture diagram and PDF source files.

### Changed

- updated every existing Markdown documentation page to Version 2;
- replaced the four-layer linear description with evidence/authority/enforcement/assurance separation;
- distinguished anomaly, heuristic score, calibrated probability, uncertainty, impact, policy risk, and authority;
- expanded NIST alignment to current CSF 2.0, SP 800-61 Rev. 3, SP 800-63 Rev. 4, AI RMF, and interoperability specifications;
- rebuilt public technical and future-development PDFs;
- updated citation metadata to Version 2.0.0.

### Fixed

- corrected the synthetic output distribution from the stale narrative to High 3, Medium 8, Low 1;
- made example scores fully reproducible from documented feature points;
- removed implications that a score directly determines or authorizes response;
- labeled submitted manuscripts, synthetic studies, and unreproduced published results accurately.

### Compatibility

The historical repository had only tag `v0.1`; no formal `v1.0.0` tag existed. Version 2 retrospectively designates the pre-2.0 material as the Version 1 conceptual baseline for migration documentation. Existing CSV filenames are retained but their columns and semantics are incompatible with positional Version 1 consumers.

## [0.1] - 2025-12-31

### Added

- initial public AITIR repository;
- README and four-layer architecture overview;
- synthetic event and risk-output examples;
- proof-of-concept and pilot-evaluation documentation;
- NIST RMF alignment, use cases, roadmap, and limitations;
- public technical exhibit and development-plan PDFs.

[2.0.0]: https://github.com/sajjad47/AITIR-Framework/compare/v0.1...HEAD
[0.1]: https://github.com/sajjad47/AITIR-Framework/releases/tag/v0.1
