# AITIR 2.0 Controlled Pilot Evaluation Protocol

**Version:** 2.0.0
**Status:** Planning template; local approval required

## Purpose

This protocol tests whether an implementation is useful, calibrated, bounded, governable, and resilient enough to progress through controlled stages. It does not authorize collection, monitoring, or automated response.

## Required approvals before data access

- system and mission owner;
- security and identity governance;
- privacy, legal, records, civil-rights, labor, and accessibility review as applicable;
- incident response and continuity owner;
- model-risk or analytical validation function;
- independent assessor;
- data owner and authorizing official.

Document purpose, lawful basis, minimization, retention, access, participant/workforce notice where required, contestability, and secure termination.

## Prespecified questions

1. Are source records complete, timely, correctly normalized, and provenance linked?
2. Does identity resolution preserve uncertainty and avoid material false joins?
3. Does detection performance hold on a chronological target-environment test?
4. Are probabilities calibrated, and does calibration decay over time or subgroup?
5. Does abstention concentrate errors at a review burden the organization can handle?
6. Are policy decisions traceable to evidence, version, authority, and reason codes?
7. Do stateful guards prevent stale, unauthorized, overbroad, or unsafe actions?
8. Are actions idempotent, evidence preserving, reversible, and continuity aware?
9. Does the system fail safely under source, model, policy, network, and connector loss?
10. Can independent reviewers reproduce every material claim?

## Progression stages

| Stage | Mode | State-changing action | Minimum evidence |
|---|---|---|---|
| P0 | architecture and policy review | none | threat model, contracts, authority, privacy, continuity |
| P1 | offline historical replay | none | provenance, chronological protocol, leakage tests |
| P2 | live shadow monitoring | none | source health, latency, queue simulation, privacy controls |
| P3 | advisory recommendations | human executes outside AITIR | analyst agreement, burden, explanations, override reasons |
| P4 | narrow T0/T1 | preapproved low-impact automation | guard tests, accessible fallback, rate limit, expiration |
| P5 | restricted T2 consideration | only explicitly authorized deterministic conditions | independent assessment, rollback, fault injection, mission approval |

T3 remains human authorized. Progression is not automatic and may be reversed.

## Data and split design

- Define the decision timestamp before feature construction.
- Fit preprocessing and models on training data only.
- Select model, calibrator, threshold, abstention coverage, and policy on validation data only.
- Evaluate once on a later untouched test period.
- Keep identities clustered in uncertainty estimation.
- Report attack-family, role, resource, and operating-condition concentration.
- Document delayed, missing, selective, or disputed labels.
- Freeze hashes, environment, code, schemas, and decision rules.

## Metrics

### Detection

- precision-recall curve and average precision;
- class/attack-family precision and recall;
- false alerts per 1,000 or 10,000 identities/user-days;
- alert rate, time to detect, and event-to-decision latency;
- uncertainty intervals with clustering appropriate to the unit.

ROC AUC may be reported but not used alone under rare-event imbalance.

### Calibration and selective decisioning

- Brier score, log loss, reliability plot, and calibration error;
- calibration by time and relevant operating group;
- coverage-risk curve and abstention rate;
- automatic errors and reviews per operational unit;
- queue size, age, handling time, and capacity breach;
- cost sensitivity over false positive, false negative, intervention, and review costs;
- sensitivity to fallible and delayed human review.

### Safety and authority

- unauthorized-action count;
- expired/replayed decision blocks;
- guard and reason-code coverage;
- separation-of-duty violations prevented;
- evidence-preservation success;
- rollback readiness and success;
- mission-impact incidents;
- duplicate-action and partial-failure rates;
- break-glass use and post-use review.

### Robustness and security

- missing and delayed sources;
- clock and schema drift;
- identity-resolution ambiguity;
- out-of-distribution and unknown attack behavior;
- evasion, poisoning, feedback manipulation, and threat-feed corruption;
- passive prompt injection in untrusted text if generative AI is used;
- policy-service, connector, network, and identity-provider failure;
- race, replay, idempotency, and stale-precondition tests.

### Privacy, fairness, and human factors

- minimization, retention, access, and secondary-use findings;
- false-positive and false-negative concentration where analysis is lawful and meaningful;
- accessibility of verification and appeal paths;
- analyst disagreement, override, fatigue, automation bias, and reason-code usefulness;
- employee/citizen impact and contestability for consequential decisions.

## Exit criteria

Thresholds are approved before the final holdout. At minimum:

- no unexplained provenance or identifier reconciliation failure;
- no analytics-to-enforcement privilege path;
- zero unauthorized T3 execution;
- all mandatory guard, expiration, replay, idempotency, and rollback tests pass;
- queue burden remains within approved capacity or safe fallback activates;
- source/model failure enters documented degraded mode;
- privacy, legal, records, labor, accessibility, continuity, and security findings are accepted by owners;
- claims remain bounded to observed evidence.

Exact performance thresholds are local risk decisions and must not be copied from the 12-row example.

## Reporting

Publish or retain, as authorized:

- protocol and amendments;
- dataset and label documentation;
- model/data/policy cards;
- code/environment and hashes;
- all primary and sensitivity outcomes;
- exclusions and missing data;
- incidents, overrides, and adverse impacts;
- decision to stop, repeat, rollback, or progress;
- independent assessment and residual risks.
