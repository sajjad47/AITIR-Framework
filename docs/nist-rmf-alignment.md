# AITIR 2.0 NIST and Government Risk-Management Alignment

**Version:** 2.0.0
**Status:** Informative alignment, not compliance

AITIR is an identity-risk decision subsystem inside organizational cybersecurity governance. It does not replace the NIST Cybersecurity Framework, Risk Management Framework, Zero Trust Architecture, Digital Identity Guidelines, security/privacy controls, incident-response guidance, or system authorization.

The broader crosswalk is in [Standards Crosswalk](standards-crosswalk.md).

## CSF 2.0

- **Govern:** decision rights, policy, risk appetite, supply chain, model risk, oversight.
- **Identify:** identities, assets, services, dependencies, risks, and data flows.
- **Protect:** authentication, authorization, least privilege, data and platform safeguards.
- **Detect:** source health, identity behavior, anomalies, threat intelligence, and evidence quality.
- **Respond:** bounded decisions, case management, containment, communications, and evidence.
- **Recover:** rollback, service continuity, degraded operation, and lessons learned.

AITIR supplies evidence toward outcomes. It does not itself establish achievement.

## RMF lifecycle

| RMF step | AITIR support |
|---|---|
| Prepare | mission context, stakeholders, risk model, telemetry purpose, decision authority |
| Categorize | resource sensitivity, identity criticality, service and impact context |
| Select | map AITIR capabilities and risks to tailored controls |
| Implement | deploy contracts, trust boundaries, policies, guards, connectors, and safeguards |
| Assess | test controls, schemas, models, policies, states, rollback, and evidence |
| Authorize | provide residual risk, limitations, assessment, and decision-rights evidence |
| Monitor | source health, performance, calibration, drift, policy, incidents, and change |

Only the organization’s authorized process can complete these steps.

## SP 800-53 control families

Principal relevant families include:

- AC Access Control
- AU Audit and Accountability
- CA Assessment, Authorization, and Monitoring
- CM Configuration Management
- CP Contingency Planning
- IA Identification and Authentication
- IR Incident Response
- PL Planning
- PM Program Management
- PS Personnel Security
- RA Risk Assessment
- SA System and Services Acquisition
- SC System and Communications Protection
- SI System and Information Integrity
- SR Supply Chain Risk Management
- privacy control families and privacy risk-management requirements

A crosswalk row is not a control implementation statement. Control evidence must be assessed for the actual system.

## Zero trust

SP 800-207 separates policy information, decision, administration, and enforcement functions. AITIR analytics may provide evidence to a policy decision point but must not become an ungoverned second authority. Subject, device, resource, and environment are evaluated per request; network location is not sufficient trust.

## Digital identity

SP 800-63-4 distinguishes identity proofing, authenticator, and federation assurance. Version 2 therefore does not equate:

- behavioral anomaly with identity fraud;
- authentication failure with malicious intent;
- a valid credential with an authorized session;
- identity confidence with model confidence;
- proofing or authentication assurance with response authority.

## Incident response

SP 800-61 Rev. 3 integrates response throughout cybersecurity risk management. AITIR response records preparation assumptions, detection evidence, policy decision, containment, recovery, communications, evidence preservation, and lessons. A connector call is not the end of the incident lifecycle.

## AI risk

If AI/ML is used, NIST AI RMF informs governance, context mapping, measurement, and management. AITIR also requires adversarial-ML and untrusted-input testing. AI is optional: an implementation can use deterministic policy, statistical baselines, graph algorithms, or human analysis.

## Assessment questions

- What exact system boundary contains AITIR components and data?
- Which principal owns each policy, model, connector, and decision?
- Can analytics reach enforcement credentials directly or indirectly?
- How is evidence provenance reproduced and protected?
- Which T0-T3 actions exist locally and who authorizes each?
- How are privacy, mission, continuity, records, legal holds, and accessibility represented?
- How do abstention and queue overload fail safely?
- How are calibration, drift, robustness, rollback, and incidents monitored?
- What evidence supports every operational claim?

## Sources

- CSF 2.0: https://doi.org/10.6028/NIST.CSWP.29
- RMF: https://doi.org/10.6028/NIST.SP.800-37r2
- SP 800-53 Rev. 5: https://doi.org/10.6028/NIST.SP.800-53r5
- SP 800-53A Rev. 5: https://doi.org/10.6028/NIST.SP.800-53Ar5
- SP 800-207: https://doi.org/10.6028/NIST.SP.800-207
- SP 800-63-4: https://doi.org/10.6028/NIST.SP.800-63-4
- SP 800-61 Rev. 3: https://doi.org/10.6028/NIST.SP.800-61r3
- AI RMF: https://doi.org/10.6028/NIST.AI.100-1
