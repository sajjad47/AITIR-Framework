# Proof-of-Concept Demonstration

This page documents a synthetic proof-of-concept for AITIR. It is designed to show how the framework can organize identity-centered events, calculate risk features, prioritize review, and support response workflow decisions.

## Important Scope Note

This proof-of-concept uses synthetic data only. It does not include real agency records, employer logs, user accounts, sensitive systems, credentials, investigative data, or operational security information.

The purpose is to demonstrate evaluation readiness, not to claim external adoption or completed deployment.

## Demonstration Objective

The proof-of-concept tests whether AITIR can convert identity and access events into a prioritized review queue for public-sector cybersecurity teams.

The demonstration asks:

- Can identity and access events be normalized into a common structure?
- Can risk factors be scored in an explainable way?
- Can events affecting sensitive systems receive higher priority?
- Can response recommendations be mapped to risk level?
- Can the output be documented for analyst review?

## Synthetic Input Dataset

The repository includes a sample synthetic dataset:

- [`examples/synthetic-identity-events.csv`](../examples/synthetic-identity-events.csv)

Each row includes:

- event identifier;
- event type;
- user role;
- system category;
- system sensitivity;
- access context;
- authentication result;
- time context;
- location context;
- endpoint signal;
- threat intelligence signal.

## Sample Output

The repository includes an example output file:

- [`examples/sample-risk-output.csv`](../examples/sample-risk-output.csv)

The sample output includes:

- risk score;
- risk level;
- main risk drivers;
- recommended review action;
- documentation note.

## Demonstration Results

In the synthetic demonstration:

- 12 sample identity/access events were evaluated;
- 4 events were categorized as high priority;
- 5 events were categorized as medium priority;
- 3 events were categorized as low priority;
- all high-priority events involved at least two risk drivers, such as privileged access, sensitive systems, abnormal timing, failed authentication, remote-access anomaly, or threat-intelligence match.

These results do not prove operational effectiveness in a live environment. They show that the framework can produce explainable, auditable prioritization logic suitable for further testing.

## Example Analyst Workflow

1. Import identity and access events.
2. Map each event to role, system category, and sensitivity.
3. Apply feature scoring.
4. Produce risk level and review queue.
5. Assign recommended response.
6. Document review decision.
7. Feed analyst outcome back into future scoring.

## Evidence Value

This proof-of-concept helps show that AITIR is not only a written idea. It has a demonstrable structure, sample evaluation method, and reproducible test format. It remains early-stage, but it is now easier for outside practitioners to review, test, critique, and adapt.

