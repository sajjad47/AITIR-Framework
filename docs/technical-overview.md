# AITIR 2.0 Technical Overview

**Version:** 2.0.0

## Purpose

Adaptive Identity-and-access Threat Intelligence and Response (AITIR) is an identity-risk decision architecture. It links telemetry, contextual analysis, uncertainty, policy, response authority, execution, assurance, and resilience without allowing analytics to authorize their own actions.

AITIR addresses a practical gap: zero trust and identity systems generate continuous decisions and evidence, while SOC and incident-response systems generate alerts and playbooks. Organizations still need an inspectable boundary that answers:

- What happened, to which subject and resource, and how reliable is the evidence?
- Is the behavior anomalous, malicious, risky, or merely unusual?
- Is the analytical output calibrated and inside its validated domain?
- What mission, privacy, continuity, and intervention harms matter?
- Which response is proportionate, and who is allowed to authorize it?
- Did the connector produce the intended state, and can it be reversed?
- What evidence supports model, policy, and system reauthorization?

## Architectural principle

```text
telemetry -> normalized event -> analytical evidence
          -> policy decision -> authorized action
          -> verified outcome -> assurance and controlled learning
```

This is not a single autonomous loop. Governance, assurance, and resilience constrain every stage.

## Seven planes

| Plane | Purpose | Primary outputs |
|---|---|---|
| Governance, risk, policy | risk appetite, lawful purpose, roles, decision rights, policy approval | policy release, authority matrix, risk register |
| Identity, asset, telemetry | normalize source events and identity/resource context | event objects, source health, subject graph |
| AITIR analytics | rules, anomaly, temporal, relational, supervised, and fusion analysis | evidence object, risk drivers, uncertainty |
| Risk decision, authorization | combine evidence with policy, mission, impact, and authority | deny, abstain, authorize, or expire decision |
| Response orchestration | execute bounded idempotent actions and manage cases | action and outcome records, rollback |
| Assurance, model risk, audit | validate, monitor, assess, and approve change | model/data cards, tests, release evidence |
| Resilience, continuity | maintain safe degraded modes and mission recovery | degraded-mode policy, recovery evidence |

## Analytical model

AITIR is model agnostic. Implementations may combine:

1. deterministic data-quality, integrity, and policy indicators;
2. contextual baselines by role, peer group, resource, device, time, and mission state;
3. point anomaly detection;
4. sequence and temporal models;
5. identity and attack-graph analysis;
6. supervised threat classification where labels support it;
7. threat-intelligence correlation.

Outputs must preserve semantic distinctions:

- **anomaly score:** deviation from a reference pattern;
- **risk score:** an ordinal or composite prioritization value;
- **probability:** a frequency-interpretable estimate only when calibrated and validated;
- **confidence:** support for an observation or model output;
- **uncertainty:** what is unknown and by which method it is measured;
- **impact:** potential consequence to people, mission, systems, evidence, or service;
- **policy decision:** authorized disposition based on evidence and governance.

## Selective decisioning

Version 2 makes abstention explicit. A system should abstain when evidence is stale, conflicting, incomplete, outside the validated domain, too close to a decision boundary, or too consequential for the available authority.

Abstention creates a review obligation. Queue capacity, aging, reviewer accuracy, disagreement, and fallback must be measured. An overloaded queue cannot safely become silent allow, silent deny, or unbounded automation.

## Identity-graph remediation

A subject graph may represent people, groups, credentials, sessions, devices, workloads, resources, entitlements, and relationships. Version 2 allows uncertainty-aware ranking of possible remediations but requires validation of relationship existence, dependency, cost, scope, authority, and rollback before enforcement.

A graph optimizer produces decision support, not permission to alter access.

## Response authority

Actions are classified T0-T3. State-changing actions pass explicit guards for evidence, authority, separation of duty, criticality, blast radius, holds, rollback, and workflow history. A failed execution requires refreshed evidence and a new decision.

See [Response Authority](response-authority.md).

## Data and interoperability

AITIR uses separate event, evidence, and decision schemas. It can map events to OCSF, behaviors to MITRE ATT&CK, threat intelligence to STIX/TAXII, playbooks to CACAO, and identity-risk signals to CAEP/RISC. External format validity does not establish source trust, local relevance, or authorization.

## Assurance

Release gates include chronological testing, leakage checks, calibration, precision-recall analysis, cost-weighted error, abstention workload, drift, missing-source stress, adversarial and poisoning tests, explanation stability, privacy and subgroup review where lawful, connector fault injection, idempotency, rollback, and independent control assessment.

## Current maturity

This repository is a Version 2 reference architecture with schemas, examples, and validation. It contains no production service, trained model, live agency telemetry, or enforcement connector. See [Status and Limitations](status-and-limitations.md).
