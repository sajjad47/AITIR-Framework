# AITIR 2.0 Status and Limitations

**Version:** 2.0.0
**Release status:** Reference architecture and research preview

## What exists

This repository currently provides:

- a seven-plane identity-risk decision architecture;
- normative Version 2 event, evidence, and decision contracts;
- T0-T3 response tiers, state transitions, and guard categories;
- standards and interoperability mappings;
- a corrected 12-row synthetic conformance illustration;
- a repository validator;
- a pilot evaluation protocol;
- migration, security, contribution, and research-provenance documentation;
- public technical and development-plan PDFs.

## Conformance level

The repository supports **L0 Document** and selected **L1 Artifact** evidence under the Version 2 specification. It does not claim:

- L2 controlled-pilot completion;
- L3 restricted operational authorization;
- L4 sustained operational assurance;
- conformance by any external product or organization.

## What does not exist here

- production implementation or hosted service;
- trained or downloadable detection model;
- real-time event pipeline or enforcement connector;
- production identity, employee, citizen, law-enforcement, classified, or agency data;
- independently reproduced corpus behind all earlier published simulations;
- external security assessment, accreditation, or certification;
- measured legal, civil-rights, labor, accessibility, records, or mission impact;
- validated real-world cost savings or return on investment.

## Evidence classes

| Class | Meaning | Current repository examples |
|---|---|---|
| Normative source | external standard/specification requirement | NIST, CISA, OASIS, OpenID mappings |
| Architectural proposition | Version 2 design choice requiring implementation validation | seven planes, contracts, T0-T3, guard set |
| Reported prior finding | published or submitted result not reproduced here | AITIR papers and submitted manuscripts |
| Reproduced artifact finding | result regenerated from checked-in files/scripts | CSV identifier and score-tier consistency |
| Operational evidence | evidence from an authorized real environment | none |

## Synthetic example boundary

The example has 12 synthetic events and no ground-truth attack label. It demonstrates:

- one-to-one identifier reconciliation;
- deterministic score calculation;
- score-to-tier consistency;
- separation of score, uncertainty status, review, and authority;
- generated count consistency.

It cannot estimate accuracy, precision, recall, false-positive rate, calibration, drift, fairness, safety, operational latency, analyst workload, incident reduction, or financial benefit.

## Research status

Two AITIR-related works are recorded as published. Four additional manuscripts were verified as submitted as of 2026-08-05. Submission IDs and status are documented in the research ledger and external publication register. Submitted studies are not represented as accepted, peer-reviewed, or journal-endorsed.

Research modules remain bounded to their actual evidence:

- government architecture: analytical/design-science evaluation and repository conformance audit;
- calibrated abstention: synthetic CERT r4.2 user-day experiment;
- graph remediation: synthetic ADSynth Active Directory graphs and experimental confidence/cost assumptions;
- response verification: exhaustive conformance to a finite proposed guard policy.

## Technical limitations

- identity resolution can silently merge or split subjects;
- source loss, clock drift, schema change, delayed data, and duplicated telemetry can distort evidence;
- anomaly scores are not probabilities or proof of maliciousness;
- probabilities can decay under temporal and organizational shift;
- attack graphs omit relationships and may contain spurious ones;
- explanations can be unstable, incomplete, or non-causal;
- analysts provide selective and fallible labels;
- feedback can be poisoned;
- playbooks can be valid but locally unauthorized or unsafe;
- connectors can partially fail, race, duplicate actions, or report success before state convergence;
- generative-AI components can be manipulated by untrusted log or threat-feed text;
- aggregate metrics can hide rare-event and subgroup failures.

## Governance limitations

AITIR does not determine lawful authority, due process, records obligations, evidence rules, employment action, accessibility requirements, procurement terms, or mission risk. Organizations must conduct local review and maintain appeal or contestability paths for consequential decisions.

## Appropriate use now

- architecture and governance review;
- schema and interface design;
- tabletop and synthetic exercises;
- offline replay planning;
- policy and state-machine testing;
- research replication and critique;
- controlled pilot design.

## Inappropriate claims

Do not claim that Version 2 is autonomous, self-healing, NIST-certified, CISA-approved, production-proven, unbiased, legally sufficient, zero-false-positive, or able to replace accountable human authority.
