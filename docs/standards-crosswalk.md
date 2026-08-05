# AITIR Version 2 Standards Crosswalk

**Version:** 2.0.0
**Status:** Informative mapping; not certification or legal advice

AITIR maps to established outcomes and formats rather than replacing them. Control selection, tailoring, implementation, assessment, authorization, and compliance remain organization specific.

## Capability crosswalk

| AITIR capability | CSF 2.0 | SP 800-53 families | RMF/lifecycle | Other principal alignment | Evidence |
|---|---|---|---|---|---|
| governance and decision rights | Govern | PM, PL, RA, CA | Prepare, Categorize, Authorize | AI RMF Govern; IR 8286r1 | policy, risk register, authority matrix |
| identity and entitlement context | Identify, Protect | AC, IA, PS, PM | Select, Implement | SP 800-63-4; CISA ZTMM Identity | inventory, assurance, entitlement graph |
| telemetry and provenance | Identify, Detect | AU, CM, SI, SC | Monitor | SP 800-137; OCSF | source health, event lineage, retention |
| AITIR analytics | Detect | AU, RA, SI, CA | Assess, Monitor | AI RMF Measure; ATT&CK | model/data card, validation, evidence object |
| calibrated risk and abstention | Govern, Detect, Respond | RA, IR, PM, AC | Assess, Authorize | AI RMF Manage | calibration, coverage-risk, queue evidence |
| policy decision and authority | Govern, Respond | AC, IA, IR, PM, PL | Authorize | SP 800-207 policy decision | decision object, guard trace, approval |
| response orchestration | Respond | IR, AC, AU, CP, CM | Respond | SP 800-61r3; CACAO | playbook, action, rollback record |
| identity-risk signal exchange | Detect, Respond | AU, IA, IR, SC | Monitor | CAEP 1.0; RISC 1.0 | issuer, event, freshness, replay evidence |
| threat-intelligence exchange | Identify, Detect | PM, RA, SI, SC | Monitor | STIX/TAXII 2.1 | indicator/behavior provenance |
| assurance and model risk | Govern, Identify | CA, SA, SR, SI, CM | Assess, Authorize, Monitor | AI RMF; SSDF; SP 800-161r1 | SBOM, tests, release approval |
| resilience and recovery | Respond, Recover | CP, IR, SC, SI | Monitor | SP 800-61r3 | degraded mode, recovery/rollback test |

## NIST CSF 2.0

Version 2 adds governance as a first-class plane and treats AITIR evidence as input to enterprise risk management. The architecture supports outcomes across all six functions but does not claim to satisfy a CSF profile by itself.

Official source: https://doi.org/10.6028/NIST.CSWP.29

## NIST RMF and controls

AITIR supports RMF activities by producing inspectable evidence for categorization context, control implementation, assessment, authorization, and monitoring. It does not select a control baseline or authorize a system.

Principal sources:

- https://doi.org/10.6028/NIST.SP.800-37r2
- https://doi.org/10.6028/NIST.SP.800-53r5
- https://doi.org/10.6028/NIST.SP.800-53Ar5
- https://doi.org/10.6028/NIST.SP.800-137

## Zero trust and digital identity

SP 800-207 informs separation of policy information, policy decision, and policy enforcement. AITIR analytics are an evidence source, not an alternate authorization authority. SP 800-63-4 keeps proofing, authenticator, federation, and assurance risks distinct from behavioral anomaly.

Sources:

- https://doi.org/10.6028/NIST.SP.800-207
- https://doi.org/10.6028/NIST.SP.800-63-4
- https://www.cisa.gov/resources-tools/resources/zero-trust-maturity-model

## Incident response

SP 800-61 Rev. 3 integrates incident response across cybersecurity risk management. AITIR Version 2 therefore links preparation, detection, response, recovery, continuity, evidence preservation, and lessons learned rather than treating response as a terminal model output.

Source: https://doi.org/10.6028/NIST.SP.800-61r3

## AI and model risk

AI RMF functions inform governance, context mapping, measurement, and management. NIST AI 100-2e2025 informs evasion, poisoning, privacy, misuse, and other adversarial-ML concerns. An AI component remains optional; deterministic rules, statistics, graph methods, and human review are valid AITIR analytics.

Sources:

- https://doi.org/10.6028/NIST.AI.100-1
- https://doi.org/10.6028/NIST.AI.100-2e2025

## Interoperability

| Standard | Permitted role | Boundary |
|---|---|---|
| OCSF 1.9 | normalize/match event classes | mapping does not prove source integrity or completeness |
| MITRE ATT&CK | technique and behavior vocabulary | mapping does not prove attribution or malicious intent |
| STIX 2.1 | represent cyber threat intelligence | object confidence is not response authority |
| TAXII 2.1 | transport collections | transport does not establish trust or relevance |
| CACAO 2.0 | represent and exchange playbooks | valid syntax does not authorize local execution |
| OpenID CAEP 1.0 | continuous access-evaluation events | issuer, replay, freshness, subject, and local policy checks remain required |
| OpenID RISC 1.0 | identity-risk incident events | received incident signal is evidence, not final adjudication |

## Claim discipline

Use “aligned with,” “maps to,” or “supports evidence for.” Do not use “NIST certified,” “NIST compliant,” “CISA approved,” “ATT&CK compliant,” or equivalent unless a separate valid basis exists. Conformance to AITIR Version 2 does not establish conformance to any external framework.
