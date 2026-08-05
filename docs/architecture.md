# AITIR 2.0 Architecture

**Version:** 2.0.0

![AITIR Version 2 seven-plane architecture](assets/aitir-framework-architecture.png)

Source diagram: [`assets/aitir-framework-architecture.html`](assets/aitir-framework-architecture.html)

## Architecture rule

**Evidence in, authority out.** Analytics never hold enforcement authority. A valid data object, score, graph edge, model explanation, threat indicator, or playbook is not an authorization.

## Planes and responsibilities

### 1. Governance, risk, and policy

- system and mission context;
- risk appetite and intervention-cost policy;
- lawful purpose, privacy, retention, and contestability;
- named decision authority and separation of duty;
- model, policy, playbook, supplier, and connector approval;
- independent assessment and reauthorization.

### 2. Identity, asset, and telemetry fabric

- identity provider, directory, MFA, PAM, endpoint, network, cloud, application, data, vulnerability, and threat-intelligence events;
- human, service-account, workload, device, session, resource, entitlement, and case identities;
- event normalization, time, provenance, integrity, classification, and retention;
- source health, clock drift, schema drift, and uncertain identity resolution.

### 3. AITIR analytics

- deterministic quality and rule checks;
- role, peer, device, resource, time, mission, and exception context;
- point, temporal, relational, and supervised analysis;
- calibrated fusion and explicit missing-model behavior;
- evidence, counter-evidence, applicability, uncertainty, and expiration.

### 4. Risk decision and authorization

- separates anomaly, probability, impact, policy risk, and authority;
- applies T0-T3 action tiers and reference guards;
- issues `deny`, `abstain`, `authorize`, or `expire`;
- binds evidence hashes, policy version, approvals, safeguards, and validity period.

### 5. Response orchestration and case management

- verifies decision validity and target preconditions;
- uses least-privileged connectors and idempotency;
- preserves evidence and records partial failure;
- executes compensating action and rollback;
- maintains incident and case workflow.

### 6. Assurance, model risk, and audit

- model/data cards and calibration evidence;
- schema, policy, guard, state-machine, and mutation tests;
- SBOM, dependency, supplier, access, and release records;
- performance, queue, drift, privacy, robustness, and safety monitoring;
- independent outcome verification and control assessment.

### 7. Resilience and continuity

- safe degraded modes for source, model, policy, network, identity-provider, or connector loss;
- mission-aware recovery objectives;
- bounded, time-limited break-glass;
- backup and recovery for policies, schemas, models, decisions, and connector state.

## Trust zones

| Zone | Assets | Primary threat | Required boundary |
|---|---|---|---|
| External/untrusted | users, devices, partners, feeds, log text | spoofing, poisoning, prompt injection | authenticate, validate, isolate content |
| Collection | collectors, parsers, identity resolution | loss, replay, drift, false joins | provenance, schema, integrity, source health |
| Analytics | features, models, rules, graphs | evasion, overconfidence, leakage, model compromise | no enforcement credentials; signed evidence |
| Decision | policies, guards, approvals | stale policy, authority bypass, race | immutable evidence refs, separation, expiration |
| Enforcement/assurance | connectors, cases, audit, rollback | overbroad privilege, duplicate or partial action | least privilege, idempotency, independent verification |

## Principal flows

1. Sources emit untrusted records.
2. Collection validates and normalizes Version 2 events.
3. Analytics produces expiring evidence objects.
4. Policy combines evidence, mission context, intervention cost, and authority.
5. Denied or abstained cases enter a controlled queue; authorized cases produce decisions.
6. Connectors recheck preconditions and execute bounded actions.
7. Outcomes are independently recorded and verified.
8. Feedback enters quarantine; assurance controls any policy/model change.
9. Resilience manages loss and degraded operation across all planes.

## Failure behavior

- missing source: mark evidence degraded; do not impute confidence upward;
- model unavailable: use approved deterministic policy or stronger verification;
- decision service unavailable: block state-changing automation rather than bypass authority;
- connector timeout: treat as unknown/failed until target state is verified;
- review overload: apply approved fallback and queue controls, never silent reclassification;
- suspected poisoning: quarantine source and feedback, preserve evidence, initiate incident handling;
- stale authorization: expire; require new evidence and decision.

## Interfaces

Normative object contracts are in [Data Contracts](data-contracts.md) and [`schemas/`](../schemas/). The full requirements are in the [Version 2 Specification](version-2-specification.md).
