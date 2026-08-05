# Migrating from AITIR Version 1 to Version 2

**Version:** 2.0.0

## Baseline designation

The repository's only historical Git tag is `v0.1`; no formal `v1.0.0` release existed. For migration purposes, Version 2 retrospectively calls the pre-2.0 four-layer repository the **Version 1 conceptual baseline**. This does not rewrite Git history or claim that a `v1.0.0` artifact was published.

## Architectural changes

| Version 1 baseline | Version 2.0 |
|---|---|
| four-layer linear pipeline | seven interacting governance, telemetry, analytics, decision, response, assurance, and resilience planes |
| AI-Assisted Adaptive Threat Intelligence and Response | canonical name: Adaptive Identity-and-access Threat Intelligence and Response |
| event -> score -> recommended response | event -> evidence -> policy decision -> authorized action -> independently verified outcome |
| heuristic score may appear action-like | score, probability, uncertainty, impact, policy risk, and authority are distinct |
| high/medium/low response mapping | T0-T3 action tiers with abstention, guards, approvals, expiration, and rollback |
| analyst feedback for improvement | quarantined, validated, versioned feedback with release approval |
| generic NIST RMF alignment | explicit current crosswalk to CSF 2.0, RMF, SP 800-53/53A, SP 800-207, SP 800-63-4, SP 800-61r3, AI RMF, CISA ZTMM, and interoperability standards |
| synthetic 12-row illustration | corrected 12-row conformance example plus schemas and automated repository validation |
| no formal version contract | semantic `2.0.0`, `VERSION`, CFF version, changelog, schemas, and migration rules |

## Migration steps

1. **Inventory producers and consumers.** Identify telemetry sources, scoring jobs, policies, queues, connectors, audit stores, and report generators.
2. **Freeze the Version 1 baseline.** Record schemas, model and threshold versions, data windows, hashes, owners, and known limitations.
3. **Adopt the event schema.** Map sources to `aitir-event-v2`; preserve source references and timestamps.
4. **Split scoring from probability.** Label every output as heuristic score, anomaly measure, calibrated probability, graph confidence, impact, or policy risk.
5. **Create evidence objects.** Add provenance, applicability, uncertainty, quality, expiration, and counter-evidence.
6. **Insert the decision boundary.** Remove enforcement credentials from analytics and require a versioned policy decision object.
7. **Classify actions T0-T3.** Define authority, approvals, safeguards, rollback, and continuity for each local action.
8. **Implement stateful guards.** Cover freshness, corroboration, approval, separation, rollback, criticality, blast radius, holds, prior failure, aging, and break-glass.
9. **Make execution idempotent.** Bind each action to an immutable decision and precondition; verify outcomes independently where feasible.
10. **Quarantine feedback.** Separate review outcomes from training and threshold updates.
11. **Build assurance evidence.** Add model/data cards, policy tests, SBOMs, connector inventory, release gates, and decision logs.
12. **Pilot progressively.** Architecture review -> offline replay -> shadow mode -> advisory mode -> narrow T0/T1 -> restricted approved T2. T3 remains human authorized.

## Compatibility

Version 1 CSV examples are not API contracts. Version 2 retains their filenames for continuity but changes their columns and semantics. Consumers MUST explicitly migrate; silent positional parsing is unsafe.

Version 2 JSON schemas use major version `2`. A Version 1 adapter MUST create a new Version 2 object with provenance; it MUST NOT relabel an old record in place.

## Historical citations

Citations to prior publications MUST use the acronym expansion and claims stated in the cited work. New Version 2 documentation uses the canonical expansion. This avoids changing the historical record while providing one forward definition.

## Rollback

Documentation changes can be reverted through Git, but operational migration needs an approved rollback plan. Rollback MUST preserve Version 2 decision and action records already created. An implementation MAY return to a deterministic advisory workflow; it MUST NOT restore direct model-to-enforcement authority.

## Exit criteria

Migration is not complete until:

- schemas and examples validate;
- every state-changing connector requires a decision object;
- no analytics identity can directly enforce;
- local T0-T3 authority is approved;
- expiration, replay, idempotency, failure refresh, and rollback tests pass;
- privacy, continuity, records, evidence, and accessibility reviews are complete;
- operational claims are bounded to evidence actually collected.
