# Security Policy

**Applies to:** AITIR Framework Version 2 documentation, schemas, examples, and build/validation scripts

## Project status

AITIR is a reference architecture and research preview, not a hosted service or production security product. The repository should never contain live credentials, personal telemetry, classified information, protected agency records, or production connector secrets.

## Reporting a security issue

Do not open a public issue if a report would expose a credential, unsafe response path, privacy vulnerability, or exploitable implementation detail. Use [GitHub private vulnerability reporting](https://github.com/sajjad47/AITIR-Framework/security/advisories/new). Include:

- affected version, file, schema, or script;
- impact and plausible misuse;
- minimum reproduction without sensitive data;
- whether the issue could bypass decision authority, expiration, idempotency, rollback, or privacy controls;
- suggested mitigation if known.

Do not include real identities or telemetry.

## High-priority classes

- analytics-to-enforcement authority bypass;
- guard, approval, separation-of-duty, expiration, or replay bypass;
- duplicate, partial, or overbroad connector action;
- evidence or audit destruction;
- feedback poisoning or model/policy release bypass;
- identity-resolution collision or cross-tenant disclosure;
- prompt injection through log, ticket, email, or threat-feed content;
- schema ambiguity that turns advisory evidence into authorization;
- generated artifact that materially misstates its source data;
- repository secret or protected data exposure.

## Safe implementation requirements

- isolate analytics from production enforcement credentials;
- authenticate and authorize every interface;
- treat all external and log text as untrusted data;
- bind actions to immutable decisions and idempotency keys;
- recheck target preconditions at execution;
- expire decisions and block replay;
- preserve evidence and test rollback;
- quarantine feedback and control model/policy promotion;
- use least privilege, dependency inventory, SBOMs, signed releases, and independent assessment;
- maintain safe degraded modes.

## Supported versions

Version 2.0.x documentation receives corrections. Historical `v0.1` is retained for research provenance and is not maintained as a safe operational specification.

## Disclosure boundary

A report and fix do not certify a deployment. Implementers remain responsible for threat modeling, testing, privacy/legal review, authorization, monitoring, incident response, and secure operations.
