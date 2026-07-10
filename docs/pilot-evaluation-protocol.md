# Pilot Evaluation Protocol

This protocol describes how AITIR can be evaluated in a non-confidential pilot or tabletop review. It is intended for public-sector cybersecurity professionals, academic reviewers, and practitioners who want to assess the framework without exposing sensitive systems.

## Pilot Goal

Evaluate whether AITIR can help analysts prioritize identity-centered cybersecurity events in a way that is explainable, auditable, and operationally useful.

## Pilot Type

Recommended first pilot:

- tabletop evaluation;
- synthetic data review;
- historical-data replay after anonymization and agency approval;
- analyst scoring comparison;
- policy/workflow mapping exercise.

## Evaluation Questions

1. Does the framework identify the highest-risk events consistently?
2. Are the risk drivers understandable to analysts and managers?
3. Does the response recommendation match operational practice?
4. Can the review decision be documented for audit purposes?
5. Does the workflow align with access control, authentication, audit, monitoring, and incident-response expectations?

## Suggested Pilot Steps

1. Select 20 to 50 synthetic or approved anonymized identity/access events.
2. Label each event with system sensitivity, role, time context, location context, authentication signal, endpoint signal, and threat-intelligence signal.
3. Apply AITIR scoring logic.
4. Ask one or more reviewers to assess whether the priority ranking is reasonable.
5. Compare AITIR output to reviewer judgment.
6. Record disagreements and refine scoring weights.
7. Produce a short pilot report summarizing findings and limitations.

## Suggested Metrics

| Metric | Description |
|---|---|
| High-risk agreement rate | Percent of high-risk AITIR events reviewers also consider high priority. |
| Explanation clarity | Reviewer assessment of whether risk drivers are understandable. |
| Escalation appropriateness | Whether recommended response matches operational expectations. |
| False-positive review rate | Number of events scored too high after review. |
| Missed-priority rate | Number of events reviewers believe should have been higher priority. |
| Documentation completeness | Whether output provides enough information for audit or after-action review. |

## Pilot Output

A completed pilot should produce:

- event set description;
- scoring table;
- reviewer comments;
- summary of agreement/disagreement;
- recommended scoring revisions;
- limitations and next steps.

## Ethical and Security Constraints

Any real-world pilot must protect:

- sensitive agency data;
- personally identifiable information;
- law-enforcement information;
- credentials and access methods;
- nonpublic system architecture;
- incident-response procedures.

## Current Status

This protocol is available for review. It is not a claim that a live external pilot has already been completed.

