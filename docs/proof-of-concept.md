# AITIR 2.0 Synthetic Proof of Concept

**Version:** 2.0.0
**Evidence class:** Reproduced artifact finding
**Data:** Synthetic; no personal, production, or classified information

## Purpose

The proof of concept demonstrates Version 2 object separation and repository conformance on 12 synthetic identity events. It is not a threat-detection experiment.

The files are:

- [`../examples/synthetic-identity-events.csv`](../examples/synthetic-identity-events.csv)
- [`../examples/sample-risk-output.csv`](../examples/sample-risk-output.csv)

## Questions it can answer

- Do input and output identifiers reconcile one to one?
- Are risk scores calculated from the published illustration?
- Do scores map to the stated risk tiers?
- Are heuristic scores clearly distinguished from calibrated probabilities?
- Does every row route to observation or review rather than self-authorizing an action?
- Do narrative counts match generated CSV counts?

## Questions it cannot answer

- Is an event malicious?
- Is the scoring function accurate or calibrated?
- What is the false-positive or false-negative rate?
- Will an analyst agree with a recommendation?
- Is any state-changing action authorized or safe?
- Will AITIR reduce incidents, cost, or workload?

There are no ground-truth attack labels, no trained model, and no measured reviewer outcomes.

## Data fields

The event CSV is a flattened teaching representation of the Version 2 event contract. It includes source, event/ingest times, subject, resource, activity, context, integrity, data quality, purpose, classification, and retention.

The output CSV includes:

- a deterministic `risk_score` and `risk_level`;
- `score_type=heuristic-risk`;
- blank calibrated probability and `calibration_status=not-calibrated`;
- explicit uncertainty method and review disposition;
- a non-authorizing recommended tier/action;
- `authority_status=not-evaluated`;
- evidence and decision schema versions.

## Deterministic scoring illustration

The scoring function is:

| Feature | Points |
|---|---:|
| failed authentication | 10 |
| privilege change | 25 |
| sensitive resource | 15 |
| after-hours activity | 10 |
| unmanaged or noncompliant device | 15 |
| high-risk country flag | 20 |
| recent threat-intelligence match | 25 |

Tiers:

- Low: 0-24
- Medium: 25-49
- High: 50 or more

The function is deliberately simple and uncalibrated. Point values are design assumptions, not learned probabilities.

## Verified output

The checked output has:

| Risk level | Count |
|---|---:|
| High | 3 |
| Medium | 8 |
| Low | 1 |
| **Total** | **12** |

The Version 1 narrative incorrectly reported 4 High, 5 Medium, and 3 Low. Version 2 corrects that discrepancy and validates the counts programmatically.

## Workflow

1. Validate the event schema and required flattened fields.
2. Calculate the deterministic risk score.
3. Assign the score tier.
4. Create an evidence record with `not-calibrated` status.
5. Recommend a bounded T0/T1 action or analyst investigation.
6. Record `abstain` or `review`; do not authorize state change.
7. Require a separate policy and authority decision for any real response.

## Run validation

```bash
python3 scripts/validate_repository.py
```

For JSON Schema checks:

```bash
uv run --with-requirements requirements-dev.txt python scripts/validate_repository.py --jsonschema
```

## Extension requirements

A research extension that adds labels or models should publish:

- data provenance and license;
- label definition and uncertainty;
- chronological train/validation/test boundaries;
- leakage controls;
- model and calibration versions;
- precision-recall and calibration evidence;
- uncertainty intervals;
- abstention workload and reviewer assumptions;
- privacy and subgroup analysis where lawful;
- full claim limitations.
