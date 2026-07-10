# Framework Architecture

AITIR organizes identity-centered cybersecurity operations into a repeatable workflow.

![AITIR Framework Architecture](assets/aitir-framework-architecture.png)

## 1. Data Inputs

Potential inputs include:

- identity and access management logs;
- authentication and multifactor authentication records;
- remote-access and VPN events;
- endpoint and device security indicators;
- ticketing and change-management records;
- privileged access data;
- system and asset sensitivity classifications;
- threat intelligence indicators;
- policy and control requirements.

AITIR does not require every input to be present at the same maturity level. The framework can start with available evidence and improve as data quality increases.

## 2. Normalization and Context Mapping

Raw events are normalized into a common structure. The framework maps each event to:

- user or service account;
- role or access category;
- system or application;
- data sensitivity;
- time and location context;
- authentication method;
- event type;
- prior related activity.

## 3. Risk Feature Analysis

AITIR evaluates risk features such as:

- unusual access timing;
- repeated failed authentication;
- remote-access anomalies;
- high-privilege access to sensitive systems;
- access outside expected role boundaries;
- endpoint or device irregularities;
- policy exceptions;
- linked events across systems.

## 4. Adaptive Risk Prioritization

The framework prioritizes events based on both technical indicators and operational consequence. Scoring should consider:

- likelihood of misuse or compromise;
- impact if the event is malicious;
- sensitivity of the affected system;
- user's privilege level;
- urgency of response;
- confidence in the available evidence;
- prior related activity.

## 5. Response Workflow

AITIR is intended to support a response queue with:

- analyst review;
- escalation triggers;
- account or access review;
- verification with system owners;
- containment recommendation;
- documentation;
- feedback to improve future scoring.

## 6. Feedback Loop

Completed reviews feed back into the model. False positives, confirmed events, analyst notes, and closure decisions can improve scoring rules and future prioritization.

