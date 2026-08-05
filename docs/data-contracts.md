# AITIR Version 2 Data Contracts

**Version:** 2.0.0
**Status:** Normative repository contract

AITIR uses explicit objects so telemetry, analytical evidence, policy decisions, and enforcement results cannot be collapsed into one opaque score or command.

## Contract rules

1. Every object MUST have a stable identifier, schema version, creation time, producer, classification, and integrity/provenance metadata.
2. Event time and ingestion time MUST remain distinct.
3. A heuristic `risk_score` MUST NOT be represented as a probability.
4. `calibrated_probability` MUST be absent unless calibration was evaluated on held-out target-domain data and the calibrator is identified.
5. `uncertainty` MUST state its meaning and method. Entropy, margin, variance, data quality, and observation confidence are not interchangeable.
6. `risk_level` is a policy label, not response authority.
7. Evidence MUST expire. Policy re-evaluates expired evidence rather than reusing it silently.
8. Missing, stale, conflicting, or out-of-domain data MUST be explicit.
9. Identifiers SHOULD be pseudonymous outside the source security domain.
10. Sensitive evidence MUST use classification, purpose, retention, and access labels.

## Event object

Normative schema: [`../schemas/aitir-event-v2.schema.json`](../schemas/aitir-event-v2.schema.json)

Required semantic fields:

- `event_id`, `schema_version`, `event_time`, `ingest_time`;
- `source.system`, `source.event_type`, `source.integrity`;
- `subject.id`, `subject.type`;
- `resource.id`, `resource.type`, `resource.sensitivity` where applicable;
- `activity.type`, `activity.outcome`;
- `context` for device, network, location, privilege, mission, and exception facts;
- `data_quality.flags` and `data_quality.completeness`;
- `governance.classification`, `purpose`, `retention_until`.

Raw source records SHOULD be retained by hash or immutable reference when policy permits. Normalization MUST preserve enough provenance to reproduce material decisions.

## Evidence object

Normative schema: [`../schemas/aitir-evidence-v2.schema.json`](../schemas/aitir-evidence-v2.schema.json)

Evidence contains:

- referenced event identifiers and analysis window;
- feature-schema, feature-pipeline, model, calibration, rule, graph, and threat-intelligence versions as applicable;
- source health and identity-resolution confidence;
- score values with explicit `score_type`;
- calibrated probability only when justified;
- uncertainty fields with method and applicability;
- risk drivers and counter-evidence;
- data-quality and out-of-distribution flags;
- ATT&CK mappings where evidence supports them;
- expiration and integrity signature/hash.

`recommended_action` MAY appear as advice. It MUST NOT be serialized as an authorization.

## Decision object

Normative schema: [`../schemas/aitir-decision-v2.schema.json`](../schemas/aitir-decision-v2.schema.json)

The decision object binds evidence to policy and authority. It includes:

- evidence IDs and immutable hashes;
- policy and guard-set versions;
- subject, resource, mission, and target criticality;
- requested action and T0-T3 tier;
- disposition: `deny`, `abstain`, `authorize`, or `expire`;
- explicit authorization mode (`system-preapproved`, `named-human`, or `dual-control`), named authority role, and approval references;
- guard results and stable reason codes;
- legal/privacy hold, evidence preservation, rollback, blast radius, and continuity checks;
- effective and expiration times.

An `authorize` disposition is necessary but not sufficient for execution. Connector preconditions and idempotency are checked again at the enforcement boundary.

## Action/outcome object

The action object SHOULD contain:

```json
{
  "action_id": "act-...",
  "decision_id": "dec-...",
  "idempotency_key": "...",
  "connector": {"id": "idp-prod", "version": "..."},
  "target": {"type": "session", "id": "..."},
  "requested_operation": "revoke-session",
  "precondition_hash": "sha256:...",
  "state": "executing",
  "evidence_preservation": {"required": true, "record_id": "..."},
  "compensating_action": {"available": true, "operation": "restore-session-policy"},
  "started_at": "...",
  "completed_at": null,
  "result": null
}
```

Allowed states are defined in [Response Authority](response-authority.md). Connector output and independent verification SHOULD both be retained. A successful API response alone does not prove the intended security state.

## Feedback object

Feedback MUST NOT update models or thresholds directly. It records:

- case and decision reference;
- reviewer role, review time, and conflict-of-interest/separation metadata where required;
- outcome category and structured rationale;
- evidence available at review time;
- label uncertainty and adjudication state;
- quarantine, validation, approval, and release status.

## Schema evolution

AITIR uses semantic versioning:

- patch: clarification or validation fix that does not change required fields or meaning;
- minor: backward-compatible optional fields or mappings;
- major: required-field, semantic, authority, or state-machine incompatibility.

Producers MUST declare their exact schema version. Consumers MUST reject unknown major versions unless a tested translator is approved. Translations create new provenance records and MUST NOT overwrite source objects.

## Interoperability mapping

- OCSF mappings SHOULD preserve the original class and source record reference.
- STIX objects and ATT&CK mappings are threat context, not proof that an identity performed an action.
- TAXII transport does not establish source trust.
- CAEP and RISC events are external evidence subject to issuer validation, replay protection, freshness, and policy.
- CACAO can represent the response workflow; the AITIR decision object remains the local authorization record.

## Privacy and retention

Identity telemetry can create workforce-surveillance and civil-liberties risks. Implementations MUST document lawful purpose, minimization, access, retention, secondary-use restrictions, and a contestability path for consequential decisions. Protected-attribute collection for fairness analysis requires separate legal and privacy review; neither collection nor omission is automatically safe.
