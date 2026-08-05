# AITIR Version 2 Response Authority

**Version:** 2.0.0
**Status:** Reference guard model; local policy is required

AITIR separates a technically executable action from an authorized action. This document specifies a reference decision-tier model, state machine, and guard categories. It is not legal advice, an agency authorization, or a universally sufficient policy.

## Decision tiers

| Tier | Description | Automation ceiling |
|---|---|---|
| T0 Observe | non-invasive enrichment, logging, watch conditions | preapproved automation |
| T1 Verify | step-up authentication, device check, user confirmation | preapproved deterministic playbook with accessible fallback |
| T2 Contain | session/token revocation, device isolation, temporary pathway suspension | named responder or narrowly preapproved deterministic conditions |
| T3 Consequential | identity disablement, privilege change, essential-service block, disciplinary/legal initiation | named human authority; dual control where policy requires |

Risk tier and action tier are separate. A high-risk score can lead to T0/T1, abstention, or denial when evidence or authority is insufficient.

## Reference states

```text
proposed -> denied
proposed -> authorized -> executing -> succeeded
                              |          |
                              v          v
                            failed --> rolled_back
proposed/authorized ------------------> expired
failed --(new evidence + new decision)--> proposed
```

### State requirements

- `proposed`: evidence and requested action are immutable and hash bound.
- `denied`: one or more stable reason codes explain the failed guards.
- `authorized`: authority, approvals, scope, effective time, and expiration are recorded.
- `executing`: idempotency and preconditions were rechecked at the connector boundary.
- `succeeded`: connector evidence and, where feasible, independent state verification agree.
- `failed`: no success is implied; retry requires refreshed state and a new decision.
- `rolled_back`: compensating action was separately authorized and verified.
- `expired`: execution is permanently blocked for that decision ID.

## Twelve reference guard categories

| ID | Guard | Reference rule |
|---|---|---|
| G1 | Risk floor | Each action tier has a policy-defined minimum evidence/risk condition. Monitor has no score floor. |
| G2 | Evidence freshness | Stale evidence blocks state-changing action except a narrowly defined break-glass session action. |
| G3 | Corroboration | T2/T3 actions require policy-defined independent sources; source duplication is not independence. |
| G4 | Approval | Approval level is proportional to action tier, target criticality, and blast radius. |
| G5 | Separation of duty | The requester cannot satisfy independent approval where separation is required. |
| G6 | Rollback | State-changing action requires a tested compensating or recovery plan unless impossibility is explicitly accepted. |
| G7 | Critical target | Critical identities, workloads, and services raise approval and continuity requirements. |
| G8 | Blast radius | Enterprise-scope destructive action is denied by default; exceptional scope needs explicit authority and staged execution. |
| G9 | Legal/privacy/evidence hold | Actions that would violate a hold or destroy required evidence are denied or redirected. |
| G10 | Refresh after failure | A failed or partial execution blocks retry until evidence and target state are refreshed. |
| G11 | Aging evidence | Aging evidence raises the required authority or lowers the permissible action tier. |
| G12 | Break-glass scope | Break-glass bypasses only enumerated guards, is time bound, and never grants unrestricted scope. |

The submitted AITIR-RV study evaluated one finite instantiation of these categories. Version 2 adopts the categories, not a claim that those exact thresholds are legally or operationally optimal for every environment.

## Required reason codes

Implementations SHOULD provide stable machine-readable codes, including:

- `INSUFFICIENT_RISK_BASIS`
- `EVIDENCE_STALE`
- `EVIDENCE_UNCORROBORATED`
- `APPROVAL_MISSING`
- `SEPARATION_OF_DUTY_FAILED`
- `ROLLBACK_NOT_READY`
- `CRITICAL_TARGET_AUTHORITY_MISSING`
- `BLAST_RADIUS_EXCEEDED`
- `HOLD_CONFLICT`
- `STATE_REFRESH_REQUIRED`
- `AGING_EVIDENCE_REQUIRES_ESCALATION`
- `BREAK_GLASS_SCOPE_INVALID`
- `OUTSIDE_VALIDATED_DOMAIN`
- `REVIEW_CAPACITY_EXCEEDED`
- `DECISION_EXPIRED`
- `PRECONDITION_CHANGED`

A denial may contain multiple reasons. Natural-language explanations MAY accompany reason codes but MUST NOT replace them.

## Abstention and review capacity

Abstention routes a case; it does not solve it. A deployment MUST define:

- queue owner and service objective;
- maximum queue size and age;
- reviewer qualifications and separation requirements;
- fallback when capacity is exceeded;
- disagreement and appeal handling;
- whether deferred cases receive protective T0/T1 controls;
- how selective labels and reviewer uncertainty are recorded.

The system MUST NOT silently convert an overloaded review queue into automatic benign decisions or unrestricted T2/T3 automation.

## Break-glass

Break-glass access or response MUST be:

- triggered for a stated mission need;
- limited to named principals, actions, targets, and duration;
- strongly authenticated where available;
- independently logged and immediately visible;
- reviewed after use;
- revoked automatically at expiration;
- unable to bypass legal/evidence safeguards unless separately authorized under applicable law and policy.

## Enforcement safety

Connectors MUST use least privilege and deny scope expansion. Each operation requires:

- immutable decision reference and idempotency key;
- target and requested-state precondition;
- approval and decision validity check;
- evidence-preservation step where applicable;
- timeout and bounded retry;
- structured connector result;
- compensating action or documented recovery path;
- independent outcome verification where feasible.

## Generative-AI restriction

A generative model MAY summarize evidence or draft an investigation plan. It MUST NOT be the root of response authority. Untrusted telemetry can contain prompt injection, so log and threat-feed text MUST be isolated as data; tool access, retrieval, output schemas, and action scope MUST be independently constrained.

## Policy verification

Before deployment, the guard set SHOULD undergo:

- decision-table review by security, mission, identity, privacy/legal, accessibility, and continuity owners;
- boundary-value and negative tests;
- state-transition tests;
- mutation or fault-injection tests;
- separation-of-duty tests;
- replay, expiration, idempotency, and race-condition tests;
- rollback and degraded-mode exercises;
- independent assessment and documented approval.
