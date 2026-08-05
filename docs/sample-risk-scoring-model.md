# AITIR 2.0 Reference Risk Scoring Model

**Version:** 2.0.0
**Status:** Synthetic teaching illustration; not a production model

## Semantic rule

AITIR distinguishes:

- anomaly score;
- heuristic risk score;
- calibrated probability;
- uncertainty;
- impact;
- policy risk;
- response authority.

The example implements only a heuristic risk score. It MUST NOT be described as a probability, confidence, calibrated threat likelihood, or authorization.

## Feature table

| Feature | Points | Synthetic rationale |
|---|---:|---|
| failed authentication | 10 | repeated failure may merit context review |
| privilege change | 25 | entitlement changes can increase exposure |
| sensitive resource | 15 | potential impact is higher |
| after-hours activity | 10 | temporal deviation may require explanation |
| unmanaged/noncompliant device | 15 | posture can weaken assurance |
| high-risk country flag | 20 | policy-defined context flag, not nationality inference |
| recent threat-intelligence match | 25 | corroborating external evidence may raise priority |

`risk_score` is the sum of present feature points.

## Tier mapping

```text
0-24  -> Low
25-49 -> Medium
50+   -> High
```

No upper bound is implied by the formula, although the synthetic file uses values below 100.

## Version 2 response mapping

Risk tier does not determine response tier automatically.

| Risk level | Default synthetic disposition | Maximum recommendation without separate authority |
|---|---|---|
| Low | observe | T0 enrichment or watch condition |
| Medium | abstain to analyst review | T0 investigation support or T1 verification proposal |
| High | urgent abstention to authorized review | T1 verification proposal; T2/T3 require independent policy and authority |

A real policy may choose a lower-impact control or no action. It must consider evidence freshness, data quality, calibration, counter-evidence, mission impact, target criticality, blast radius, holds, rollback, and authority.

## Example results

The checked-in output contains 3 High, 8 Medium, and 1 Low event. The validator recomputes scores and tiers from the event flags and rejects inconsistent counts.

## Why this is not calibration

Calibration asks whether stated probabilities correspond to observed frequencies on held-out data. This example has no labels and does not output probabilities. A production probability requires:

1. a defined prediction target and timestamp;
2. representative training data;
3. a held-out calibration period;
4. a later untouched test period;
5. Brier score, reliability analysis, and uncertainty;
6. monitoring for calibration decay and domain shift.

## Selective prediction

If a model later provides a calibrated probability, Version 2 still permits abstention. Coverage is chosen from validation data with explicit error and review costs. Required reporting includes:

- accepted-set error or risk;
- abstention/review rate;
- false alerts and reviews per operational unit;
- queue capacity and aging;
- sensitivity to reviewer accuracy and cost;
- behavior under temporal and attack-family shift.

## Threats to validity

- feature weights are subjective;
- binary flags discard magnitude and sequence;
- country flags can be crude, discriminatory, or operationally misleading;
- an after-hours event can be mission necessary;
- threat feeds contain false, stale, or low-context indicators;
- additive points ignore interactions and missingness;
- static thresholds drift;
- high impact is not proof of malicious intent.

Use this model only to test documentation, schema, and workflow logic.
