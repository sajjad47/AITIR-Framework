# Sample Risk Scoring Model

This page describes a sample scoring model for AITIR using synthetic events. The model is intentionally simple and explainable so public-sector reviewers can evaluate the logic.

## Risk Score Components

Each event can receive points from the following categories:

| Feature | Example Condition | Points |
|---|---:|---:|
| Sensitive system | Criminal justice, public-service portal, financial, identity platform | 15 |
| Privileged role | Administrator, security analyst, database operator | 15 |
| Abnormal timing | Outside normal business hours or unusual access window | 10 |
| Remote-access anomaly | New VPN location, unusual network, impossible travel indicator | 15 |
| Authentication concern | Failed MFA, repeated failed login, disabled MFA, password reset anomaly | 15 |
| Endpoint concern | Unmanaged device, missing patch, endpoint alert | 10 |
| Threat intelligence match | Known suspicious IP, indicator match, suspicious geolocation | 20 |
| Prior related activity | Multiple related events within review window | 10 |

## Risk Levels

| Score Range | Risk Level | Review Priority |
|---:|---|---|
| 0-24 | Low | Routine review or documentation |
| 25-49 | Medium | Analyst review recommended |
| 50+ | High | Prompt review and escalation consideration |

## Response Mapping

| Risk Level | Example Response |
|---|---|
| Low | Document event; review during routine access monitoring. |
| Medium | Assign analyst review; verify business justification; check related activity. |
| High | Escalate for prompt review; validate user/session; consider containment or access review. |

## Explainability Requirement

Every score should include a plain-language explanation. AITIR should not produce a risk score without showing the main risk drivers.

Example:

> High risk because the event involved privileged access to a sensitive system, abnormal timing, and a threat-intelligence match.

## Limitations

This scoring model is illustrative. It is not a certified algorithm and should not be used as a live security-control decision engine without agency review, validation, tuning, legal review, and operational testing.

