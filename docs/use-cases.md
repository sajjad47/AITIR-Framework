# AITIR 2.0 Use Cases

**Version:** 2.0.0
**Status:** Illustrative scenarios, not deployment claims

Every use case follows the same boundary: telemetry becomes evidence; policy and named authority decide; connectors execute only a bounded decision; assurance verifies the outcome.

## 1. Privileged session anomaly

**Scenario:** A privileged identity authenticates from a new device and network context, then accesses a sensitive administrative resource outside its normal window.

**AITIR flow:**

- normalize identity, device, session, resource, and timing events;
- check source health, approved exceptions, assurance, and counter-evidence;
- create expiring evidence with score type and uncertainty;
- consider T1 step-up verification before containment;
- require independent corroboration, mission check, and authority for T2 session revocation;
- preserve logs and verify target session state.

**Caution:** New context is not proof of compromise; emergency or approved work can be unusual.

## 2. Service-account and workload identity

**Scenario:** A non-human identity begins using new credentials or resources.

**AITIR flow:**

- distinguish workload identity from a person;
- map owner, dependency, rotation, deployment, and exception context;
- avoid user-behavior assumptions that do not apply;
- require continuity and rollback before credential or privilege change;
- classify broad disablement as consequential when essential services depend on it.

## 3. MFA fatigue or suspicious authentication sequence

**Scenario:** Repeated prompts, failures, and a later successful session appear across one identity.

**AITIR flow:**

- represent the sequence rather than isolated events;
- correlate device, session, authenticator, CAEP/RISC, and help-desk evidence;
- use T1 confirmation with anti-fatigue and accessible fallback;
- abstain when events are stale or identity resolution conflicts;
- escalate only through local incident and authority policy.

## 4. Identity attack-path remediation

**Scenario:** A subject graph shows several routes from ordinary identities to high-value administrative targets, but relationships have unequal confidence and disruption cost.

**AITIR flow:**

- record graph version, provenance, freshness, and relation confidence;
- rank cost-constrained candidate remediations under uncertainty;
- validate that each relationship exists and identify dependencies;
- treat ranking as decision support;
- authorize and stage approved changes with rollback;
- measure residual validated reachability and wasted-action rate.

**Caution:** Synthetic graph-study results do not establish a production confidence model or optimal action cost.

## 5. Insider-threat triage with abstention

**Scenario:** A behavior model ranks user-day activity, but several cases are close to the decision boundary.

**AITIR flow:**

- keep chronological evaluation and held-out calibration;
- route uncertain cases to a measured review queue;
- apply approved protective T0/T1 controls while review is pending;
- monitor queue age, disagreement, and reviewer accuracy;
- prevent queue overload from becoming silent allow/deny.

**Caution:** The submitted CERT study used synthetic data and assumed correct review in its cost model.

## 6. Cross-agency or partner risk signal

**Scenario:** A trusted partner sends an identity-risk event through CAEP/RISC or threat intelligence through STIX/TAXII.

**AITIR flow:**

- authenticate issuer and validate signature, audience, subject, freshness, replay, and schema;
- retain sender confidence and provenance;
- correlate without treating transport or indicator match as proof;
- apply local mission, privacy, and authority policy;
- avoid disclosing protected information beyond authorized purpose.

## 7. Public-service continuity

**Scenario:** Identity controls protect a public-facing benefit, emergency, justice, health, or safety service.

**AITIR flow:**

- include mission state, service dependencies, accessibility, and essential-user paths;
- prefer proportionate verification and narrow session controls;
- require continuity plan for T2/T3;
- preserve due-process and contestability paths;
- use bounded, monitored break-glass and post-use review.

## 8. Generative-AI-assisted investigation

**Scenario:** An LLM summarizes identity evidence or drafts an analyst timeline.

**AITIR flow:**

- treat all log, ticket, email, and threat-feed text as untrusted data;
- isolate prompts and retrieval, restrict tools, and validate structured output;
- cite immutable evidence references;
- expose uncertainty and omit unsupported claims;
- keep the model outside policy authority and connector privileges;
- require human review for material conclusions.

## 9. Research and training

AITIR can support tabletop exercises, schema mapping, policy testing, synthetic replay, academic evaluation, and procurement requirements. Researchers must disclose synthetic data, protocol changes, code and environment, negative findings, and limits to external validity.

## Use-case acceptance checklist

- stated purpose and lawful authority;
- named data and system owners;
- source and identity-resolution quality;
- local T0-T3 catalog and decision rights;
- privacy, records, labor, accessibility, and contestability review;
- abstention and queue-capacity plan;
- evidence preservation, rollback, degraded mode, and recovery;
- independent assessment and bounded claims.
