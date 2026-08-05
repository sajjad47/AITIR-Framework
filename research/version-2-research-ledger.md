# AITIR Version 2 Research Ledger

**Research cutoff:** 2026-08-05T20:24:45Z
**Purpose:** Source provenance for AITIR Version 2.0 documentation
**Baseline audited:** Git commit `90a0a8561cdcc95038b262c710aa6e6ea02d7785` (`v0.1`, retrospectively designated the Version 1 conceptual baseline)

## Method

The update used an evidence hierarchy:

1. current government standards and official specifications for normative requirements;
2. peer-reviewed or primary research for analytical design and known limitations;
3. published AITIR papers for framework lineage and reported prior findings;
4. submitted AITIR manuscripts for explicitly labeled research modules;
5. the checked-in repository for reproducible artifact claims.

A source being cited does not make AITIR certified against it. A manuscript being submitted does not make its findings accepted. Repository examples establish only the properties reproduced by repository validation.

The hosted search/extraction backend was unavailable because its account reported insufficient balance. Official documents were therefore fetched directly over HTTPS, DOI links were resolved, and source titles and metadata were checked against publisher pages. This limitation affected convenience, not the source hierarchy.

## Authoritative standards and specifications

| Source | Version/date | AITIR Version 2 use | Stable source |
|---|---|---|---|
| NIST Cybersecurity Framework | CSF 2.0, 2024 | Govern/Identify/Protect/Detect/Respond/Recover outcomes | https://doi.org/10.6028/NIST.CSWP.29 |
| NIST Risk Management Framework | SP 800-37 Rev. 2, 2018 | authorization lifecycle and continuous monitoring | https://doi.org/10.6028/NIST.SP.800-37r2 |
| NIST Zero Trust Architecture | SP 800-207, 2020 | policy decision/enforcement separation; no implicit trust | https://doi.org/10.6028/NIST.SP.800-207 |
| NIST security/privacy controls | SP 800-53 Rev. 5 and Update 1 | AC, AU, CA, CM, CP, IA, IR, PM, RA, SA, SC, SI, SR families | https://doi.org/10.6028/NIST.SP.800-53r5 |
| NIST control assessment | SP 800-53A Rev. 5, 2022 | inspectable control evidence and assessment | https://doi.org/10.6028/NIST.SP.800-53Ar5 |
| NIST Digital Identity Guidelines | SP 800-63-4, final July 2025 | identity proofing, authentication, federation, assurance distinctions | https://doi.org/10.6028/NIST.SP.800-63-4 |
| NIST incident response | SP 800-61 Rev. 3, 2025 | incident response integrated with CSF 2.0 risk management | https://doi.org/10.6028/NIST.SP.800-61r3 |
| NIST continuous monitoring | SP 800-137, 2011 | monitoring strategy, collection, analysis, reporting, response | https://doi.org/10.6028/NIST.SP.800-137 |
| NIST AI Risk Management Framework | AI 100-1, 2023 | govern/map/measure/manage model risk | https://doi.org/10.6028/NIST.AI.100-1 |
| NIST adversarial ML taxonomy | AI 100-2e2025, 2025 | evasion, poisoning, privacy, and misuse threat categories | https://doi.org/10.6028/NIST.AI.100-2e2025 |
| NIST Secure Software Development Framework | SP 800-218, 2022 | secure development, release, dependency, and vulnerability practices | https://doi.org/10.6028/NIST.SP.800-218 |
| NIST cyber supply-chain guidance | SP 800-161 Rev. 1 Update 1, 2024 | supplier, dependency, model, data, and connector risk | https://doi.org/10.6028/NIST.SP.800-161r1-upd1 |
| CISA Zero Trust Maturity Model | 2.0, 2023 | identity, devices, networks, applications/workloads, data, and cross-cutting maturity | https://www.cisa.gov/resources-tools/resources/zero-trust-maturity-model |
| MITRE ATT&CK | live knowledge base, accessed 2026-08-05 | behavior, technique, detection, mitigation vocabulary | https://attack.mitre.org/ |
| OASIS STIX | 2.1 | structured threat-intelligence objects | https://docs.oasis-open.org/cti/stix/v2.1/stix-v2.1.html |
| OASIS TAXII | 2.1 | threat-intelligence exchange API | https://docs.oasis-open.org/cti/taxii/v2.1/taxii-v2.1.html |
| OASIS CACAO Security Playbooks | 2.0 CS01, 2023 | playbook schema and taxonomy, not local execution authority | https://docs.oasis-open.org/cacao/security-playbooks/v2.0/security-playbooks-v2.0.html |
| OpenID Continuous Access Evaluation Profile | final 1.0, 2025 | continuous session, credential, device, and assurance signals | https://openid.net/specs/openid-caep-1_0-final.html |
| OpenID RISC Profile | final 1.0, 2025 | identity-risk incident signals | https://openid.net/specs/openid-risc-1_0-final.html |
| Open Cybersecurity Schema Framework | 1.9 current stable in accessed schema browser | optional event normalization mapping | https://schema.ocsf.io/ |

## Research foundation

The following sources directly inform Version 2 design or limitations. They are not an exhaustive systematic review.

| Topic | Source | Relevance |
|---|---|---|
| open-world ML limits | Sommer & Paxson, 2010, https://doi.org/10.1109/SP.2010.25 | security data violate closed-world assumptions; deployment context matters |
| anomaly detection | Chandola et al., 2009, https://doi.org/10.1145/1541880.1541882 | anomalies are not synonymous with attacks |
| probability calibration | Niculescu-Mizil & Caruana, 2005, https://doi.org/10.1145/1102351.1102430 | ranking and probability quality are different properties |
| concept drift | Gama et al., 2014, https://doi.org/10.1145/2523813 | temporal change requires deployment-aware evaluation |
| insider-threat review | Alzaabi & Mehmood, 2024, https://doi.org/10.1109/ACCESS.2024.3369906 | imbalance, generalization, and practical validation remain open issues |
| deployed insider detection | Erola et al., 2022, https://doi.org/10.1016/j.jisa.2022.103167 | organizational integration and analyst workflow are part of effectiveness |
| uncertainty in intrusion detection | Talpini et al., 2024, https://doi.org/10.1007/s40860-024-00238-8 | overconfidence and unknown attacks motivate explicit uncertainty handling |
| contextual security events | DeepCASE, 2022, https://doi.org/10.1109/SP46214.2022.9833671 | context-aware event triage at operational scale |
| explainable AI | Ali et al., 2023, https://doi.org/10.1016/j.inffus.2023.101805 | explanation fidelity, stability, usability, and non-causality cautions |
| AD edge blocking | Guo et al., 2023, https://doi.org/10.1609/aaai.v37i5.25701 | budgeted attack-graph hardening foundation |
| scalable AD hardening | Zhang et al., 2023, https://doi.org/10.1145/3579856.3590343 | weighted large-graph optimization foundation |
| uncertainty in security decisions | Zhang & Malacaria, 2024, https://doi.org/10.1016/j.cose.2024.104153 | uncertainty must be propagated into control decisions |
| synthetic AD graphs | ADSynth, 2024, https://doi.org/10.1109/DSN58291.2024.00021 | reproducible synthetic graph benchmark with field-validity limits |
| runtime verification | Bartocci et al., 2018, https://doi.org/10.1007/978-3-319-75632-5_1 | execution behavior can be checked against explicit specification |
| policy verification | NIST IR 8360, 2021, https://doi.org/10.6028/NIST.IR.8360-draft | privilege leakage/blocking and policy-test methods |
| mutation testing | Jia & Harman, 2011, https://doi.org/10.1109/TSE.2010.62 | injected faults assess sensitivity of a policy test suite |

Preprints discovered during the cutoff search are not treated as normative evidence. Of particular relevance, Carbon Filter (arXiv:2405.04691v1) describes scalable alert reduction, and 2025-2026 preprints explore SOC human-AI collaboration and trust calibration. They indicate active research directions but do not replace standards or peer-reviewed evidence.

## AITIR lineage and module map

### Published works

1. Hossain & Reddy (2024), “AI-Enhanced Identity Threat Detection and Automated Response: An AITIR Framework for Optimized Cybersecurity Operations,” https://doi.org/10.71097/IJSAT.v15.i2.11300. This is prior conceptual/simulation evidence, not reproduced by the Version 2 repository.
2. Hossain et al. (2025), “AI-Assisted Identity and Access Threat Detection Using the AITIR Framework for Public-Sector Cybersecurity Environments,” https://doi.org/10.32996/jcsts.2025.7.12.62. This is published framework lineage with synthetic/simulated evaluation, not a production deployment.

### Submitted, not accepted as of the cutoff

| Submission | Module used in Version 2 | Evidence boundary |
|---|---|---|
| JIDMIS 1402 | seven-plane government architecture, design requirements, standards crosswalk, pilot scorecard | design-science architecture and 12-row repository conformance audit; no field deployment |
| IJCISIM 4189 | calibrated probability, abstention, coverage-risk and review-cost model | synthetic CERT r4.2 user-day experiment; no real employee data or measured reviewer performance |
| JCP jcp-4513665 | uncertain identity-graph remediation and cost-constrained ranking | synthetic ADSynth graphs; confidence distributions and cost proxies are experimental assumptions |
| J.UCS 210531 | explicit-state response-authority verifier and 12 guard categories | exhaustive conformance to a finite proposed policy; not legal sufficiency or production safety |

The repository describes these modules and their interfaces. It does not copy their headline findings into a generic performance claim.

## Reproduced baseline findings

The Version 1 baseline contained 12 synthetic input rows and 12 output rows. Identifier sets reconciled and numeric scores matched the documented tier thresholds. The output distribution was **High 3, Medium 8, Low 1**, while the narrative claimed **High 4, Medium 5, Low 3**. Version 2 corrects the narrative and adds an automated validation gate. This establishes artifact consistency only, not accuracy, calibration, safety, or efficacy.

## Research gaps retained in Version 2

- prospective evaluation on lawful, organization-representative telemetry;
- external validation across organizations, roles, threat families, and technology stacks;
- calibrated identity and graph confidence from field evidence;
- measured analyst accuracy, latency, workload, and disagreement under abstention;
- privacy, civil-rights, labor, accessibility, due-process, and records review;
- adversarial evaluation of telemetry, models, identity resolution, threat feeds, and generative-AI components;
- connector fault injection, rollback rehearsal, and continuity validation;
- independent control assessment and system authorization;
- reproducible publication of implementation code and permissible data artifacts.
