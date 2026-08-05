# AITIR Version 2.0 Specification

**Version:** 2.0.0
**Status:** Reference architecture and research preview
**Released:** 2026-08-05
**Canonical name:** Adaptive Identity-and-access Threat Intelligence and Response (AITIR)

## 1. Scope and evidence boundary

AITIR Version 2.0 specifies how identity-centered security telemetry becomes governed evidence, a bounded decision, an authorized response, and auditable assurance. It is a vendor-neutral reference architecture. It is not software, a trained model, a compliance certification, a legal determination, or evidence of production effectiveness.

Earlier AITIR publications and repository material used several acronym expansions and linear four- or six-layer descriptions. Version 2 standardizes the name above and replaces the linear pipeline with seven interacting planes. Historical names remain valid when citing those works.

The key rule is:

> **Evidence in, authority out:** analytical components produce evidence; authorized policy components decide; enforcement components act; assurance components verify.

A model score, anomaly label, indicator match, graph rank, or natural-language recommendation MUST NOT grant itself response authority.

The key words **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY** express conformance requirements.

## 2. Design requirements

| ID | Version 2 requirement |
|---|---|
| DR1 | Every decision MUST identify an accountable owner, policy basis, authorization boundary, and expiration. |
| DR2 | Decisions MUST keep subject, device, resource, environment, mission, and identity-assurance context distinct. |
| DR3 | Events, transformations, features, models, policies, explanations, decisions, actions, and outcomes MUST be provenance linked. |
| DR4 | Analytical evidence, policy decision, and policy enforcement MUST be separate interfaces and privileges. |
| DR5 | T3 consequential actions MUST require a named human authority; T2 automation MUST be narrowly preapproved and deterministic. |
| DR6 | Responses MUST be proportionate, evidence preserving, continuity aware, and reversible where technically possible. |
| DR7 | Feedback and retraining data MUST be quarantined, validated, versioned, and protected against poisoning. |
| DR8 | Telemetry processing MUST apply purpose limitation, minimization, retention, access, privacy, and contestability controls. |
| DR9 | Components, models, data, policies, dependencies, and connectors MUST have inventory, integrity, release, and rollback evidence. |
| DR10 | Operational claims MUST be supported by chronological, target-environment, independently reviewable evaluation. |

## 3. Seven-plane architecture

### Plane 1: Governance, risk, and policy

Defines risk appetite, mission priorities, system categorization, lawful purpose, privacy constraints, decision rights, model-risk ownership, playbook approval, emergency authority, and independent assessment. Machine-readable policies remain subordinate to approved governance. Every policy release has an owner, scope, effective period, tests, control mapping, and rollback target.

### Plane 2: Identity, asset, and telemetry fabric

Collects identity-provider, directory, MFA, privileged-access, endpoint, network, cloud, application, data-access, vulnerability, threat-intelligence, service-account, workload-identity, mission, and dependency evidence. Events use a versioned schema and retain source, event time, collection time, integrity state, classification, tenancy, and retention metadata.

A subject graph MAY connect people, roles, credentials, devices, workloads, sessions, resources, entitlements, and cases. Uncertain identity joins MUST be marked rather than silently merged. Source loss, clock drift, schema drift, and integrity failure are health events.

### Plane 3: AITIR analytics

Provides six model-agnostic functions:

1. schema, quality, integrity, and deterministic-rule checks;
2. role, peer, resource, device, time, exception, and mission context;
3. point anomaly analysis;
4. sequence and temporal analysis;
5. relational and identity-graph analysis;
6. calibrated supervised classification for label-supported threats.

Fusion occurs only after target-environment validation. Missing output remains missing; one failed component MUST NOT increase another component's confidence. Outputs distinguish anomaly, score, calibrated probability, epistemic or data uncertainty, confidence, impact, and policy risk. Explanations MUST be labeled as evidence or rationale, not causal proof.

### Plane 4: Risk decision and authorization

Combines analytical evidence with policy, mission impact, resource criticality, evidence quality, uncertainty, alternatives, intervention cost, and reversibility. Abstention is a valid decision when evidence is incomplete, stale, conflicting, outside the validated domain, or too consequential for available authority.

This plane produces a versioned decision object, never a direct connector command.

### Plane 5: Response orchestration and case management

Translates an authorized decision into idempotent, least-privileged actions. Each action records its approval, target, preconditions, timeout, result, evidence-preservation step, compensating action, and case. Partial or failed enforcement is an incident, not success. Connectors MUST NOT broaden scope.

CACAO playbooks MAY represent workflows; STIX/TAXII MAY exchange threat intelligence; CAEP/RISC MAY exchange identity-risk events. Structural conformance to those formats does not establish local execution authority.

### Plane 6: Assurance, model risk, and audit

Maintains immutable decision records, model cards, data documentation, validation reports, policy tests, control evidence, SBOMs, dependency inventories, access reviews, incidents, and release approvals. It monitors calibration, precision-recall behavior, queue burden, error cost, latency, drift, subgroup errors where lawful, explanation stability, rollback, source health, and unauthorized-action count.

### Plane 7: Resilience and continuity

Defines degraded operation for loss of telemetry, models, policy services, identity providers, networks, or connectors. Model failure MUST NOT default to unrestricted access or mass denial. Degraded modes use approved deterministic policy, stronger verification, bounded break-glass access, and mission-specific recovery objectives.

## 4. Trust boundaries

AITIR separates at least five trust zones:

1. **External/untrusted evidence:** devices, users, partner feeds, threat intelligence, and log fields may be attacker controlled.
2. **Collection and normalization:** parsers and identity resolution validate but do not authorize.
3. **Analytics:** models read governed features and emit signed evidence without enforcement credentials.
4. **Decision authority:** policy services and authorized humans evaluate evidence and issue scoped decisions.
5. **Enforcement and assurance:** least-privileged connectors execute; independent records verify the result.

Untrusted text, including log content, MUST be treated as data rather than instructions. Any generative-AI component MUST isolate retrieved content, restrict tools, validate structured output, and remain outside the authorization root.

## 5. Core contracts

### 5.1 Event object

An event identifies its schema version, source, subject, resource, event and ingestion times, event type, outcome, integrity, classification, retention, and data-quality flags. The JSON Schema in `schemas/aitir-event-v2.schema.json` is the normative repository contract.

### 5.2 Evidence object

An evidence object links one or more events to feature, model, and threat-intelligence provenance. It records score type, calibrated probability when available, uncertainty, data quality, applicability domain, risk drivers, and expiration. A heuristic score MUST NOT be serialized as a probability.

### 5.3 Decision object

A decision object records evidence references, policy version, requested tier and action, disposition, authority, approval, guard results, mission-impact check, rollback readiness, legal or privacy holds, expiration, and reason codes.

### 5.4 Action and outcome object

An action records the immutable decision reference, connector and target, idempotency key, preconditions, execution state, evidence preservation, result, and compensating action. Outcome evidence returns to assurance, not directly into a training set.

### 5.5 Feedback object

Feedback records reviewer role, decision, rationale category, uncertainty, provenance, and quality status. It enters a quarantine store. Model or policy promotion requires a separately approved release process.

## 6. Decision and automation tiers

| Tier | Typical action | Authority | Required safeguards |
|---|---|---|---|
| T0 Observe | enrich, increase logging, open watch condition | preapproved policy | expiration, rate limit, audit |
| T1 Verify | step-up authentication, device check, user confirmation | preapproved deterministic playbook | accessible fallback, anti-fatigue, no permanent entitlement change |
| T2 Contain | revoke token/session, isolate device, temporarily suspend pathway | authorized responder; automation only in narrow approved conditions | corroboration, evidence preservation, mission check, rollback, notification |
| T3 Consequential | disable identity, alter privilege, block essential service, disciplinary/legal initiation | named human authority; dual control where required | documented basis, legal/privacy path, continuity, contestability, rollback where possible |

A higher risk score does not automatically select a higher action tier. Policy may choose a lower-impact control, request more evidence, or abstain.

## 7. Response state machine

Permitted states are `proposed`, `denied`, `authorized`, `executing`, `succeeded`, `failed`, `rolled_back`, and `expired`.

- `proposed -> denied` when any mandatory guard fails.
- `proposed -> authorized` only when policy, authority, evidence, mission, and rollback guards pass.
- `authorized -> executing` only with an idempotency key and unchanged preconditions.
- `executing -> succeeded|failed` only with connector evidence.
- `failed -> proposed` requires refreshed evidence and a new decision identifier.
- `succeeded|failed -> rolled_back` requires an authorized compensating action.
- stale `proposed|authorized` decisions become `expired` and cannot execute.

Reference guard categories include risk floor, evidence freshness, corroboration, approval, separation of duty, rollback, critical target, blast radius, legal hold, refresh after failure, aging evidence, and break-glass scope. See [Response Authority](response-authority.md).

## 8. Safety invariants

A conforming implementation MUST demonstrate that:

1. no analytics principal holds production enforcement authority;
2. every enforcement attempt has one immutable decision and idempotency key;
3. expired or superseded decisions cannot execute;
4. T3 requires named human authority;
5. failed execution cannot retry without refreshed state;
6. break-glass is scoped, time bound, logged, and reviewed;
7. evidence and audit records survive containment where feasible;
8. feedback cannot enter training without quarantine and approval;
9. source or model failure enters an explicit degraded mode;
10. generated reports reconcile to source artifacts and hashes.

## 9. Interoperability profile

Version 2 uses mappings rather than claiming certification:

- NIST CSF 2.0 for risk outcomes and governance;
- NIST RMF and SP 800-53/53A for lifecycle, controls, assessment, authorization, and monitoring;
- NIST SP 800-207 for policy-decision and enforcement separation;
- NIST SP 800-63-4 for identity proofing, authentication, federation, and assurance distinctions;
- NIST SP 800-61 Rev. 3 for incident-response integration;
- NIST AI RMF and NIST AI 100-2e2025 for model risk and adversarial-ML concerns;
- CISA Zero Trust Maturity Model 2.0 for identity-centered maturity;
- MITRE ATT&CK for behavior vocabulary;
- OCSF 1.9 for event-schema mapping;
- STIX/TAXII 2.1 for threat-intelligence exchange;
- CACAO 2.0 for playbook representation;
- OpenID CAEP 1.0 and RISC 1.0 for continuous identity-risk signals.

See [Standards Crosswalk](standards-crosswalk.md). Alignment does not establish compliance.

## 10. Conformance levels

| Level | Evidence |
|---|---|
| L0 Document | versioned architecture, contracts, threat model, governance, and limitations |
| L1 Artifact | schemas validate; examples reconcile; policy and state-machine tests pass |
| L2 Controlled pilot | chronological/offline and shadow-mode evaluation; approved exit criteria; no unrestricted enforcement |
| L3 Restricted operations | authorized environment; control assessment; narrow T0/T1 and approved T2; monitored rollback |
| L4 Operational assurance | sustained multi-period evidence, independent assessment, incident learning, reauthorization |

This repository release provides **L0** and selected **L1 documentation artifacts**. It does not claim L2-L4.

## 11. Evaluation minimums

A pilot reports:

- precision-recall curves, attack-family recall, false alerts per operational unit, and time to detect;
- Brier score, reliability plots, calibration error, abstention rate, coverage-risk curve, and queue burden;
- chronological holdout, leakage controls, delayed/selective-label handling, and uncertainty intervals;
- source loss, clock drift, schema change, out-of-distribution, evasion, poisoning, and prompt-injection stress tests;
- unauthorized action count, rollback success, evidence preservation, mission impact, duplicate-action rate, and connector recovery;
- analyst handling time, disagreement, override reasons, queue aging, accessibility, and contestability;
- privacy, retention, access, subgroup-error, and civil-rights review where lawful and meaningful;
- policy, model, feature, schema, connector, and decision-record traceability.

Thresholds MUST be fixed from risk tolerance before inspecting the final holdout.

## 12. Maturity and limitations

Version 2 is technically specified but not production certified. The checked-in example remains a 12-event synthetic conformance illustration without attack ground truth. Submitted AITIR studies provide bounded research evidence for architecture, abstention, graph remediation, and response verification; their submission status does not equal peer-reviewed acceptance. Published simulation results have not all been independently reproduced from this repository.

Implementers remain responsible for legal authority, privacy, labor, accessibility, records, evidence, procurement, continuity, accreditation, and local policy.
