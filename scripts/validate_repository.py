#!/usr/bin/env python3
"""Validate AITIR Version 2 repository consistency without network access."""

from __future__ import annotations

import argparse
import copy
import csv
import hashlib
import json
import re
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []
CHECKS = 0


def check(condition: bool, message: str) -> None:
    global CHECKS
    CHECKS += 1
    if not condition:
        ERRORS.append(message)


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def validate_version() -> None:
    check(read("VERSION").strip() == "2.0.0", "VERSION must be 2.0.0")
    cff = read("CITATION.cff")
    check(
        re.search(r"(?m)^version:\s*2\.0\.0\s*$", cff) is not None,
        "CITATION.cff version mismatch",
    )
    check(
        re.search(r"(?m)^date-released:\s*2026-08-05\s*$", cff) is not None,
        "CITATION.cff release date mismatch",
    )

    versioned_docs = [
        "docs/index.md",
        "docs/technical-overview.md",
        "docs/architecture.md",
        "docs/status-and-limitations.md",
        "docs/roadmap.md",
        "docs/proof-of-concept.md",
        "docs/sample-risk-scoring-model.md",
        "docs/pilot-evaluation-protocol.md",
        "docs/nist-rmf-alignment.md",
        "docs/use-cases.md",
        "docs/research-and-publications.md",
        "docs/public-materials.md",
        "docs/version-2-specification.md",
        "docs/data-contracts.md",
        "docs/response-authority.md",
        "docs/migration-v1-to-v2.md",
        "docs/standards-crosswalk.md",
        "docs/release-process.md",
    ]
    for path in versioned_docs:
        check("2.0.0" in read(path), f"{path} lacks Version 2.0.0 marker")

    required_governance = [
        ".github/ISSUE_TEMPLATE/config.yml",
        ".github/ISSUE_TEMPLATE/defect.yml",
        ".github/ISSUE_TEMPLATE/proposal.yml",
        ".github/PULL_REQUEST_TEMPLATE.md",
        ".github/dependabot.yml",
        ".github/workflows/validate.yml",
        "CODE_OF_CONDUCT.md",
        "CONTRIBUTING.md",
        "SECURITY.md",
        "requirements-dev.txt",
        "scripts/verify_generated_artifacts.py",
    ]
    for path in required_governance:
        check((ROOT / path).is_file(), f"missing governance or automation file: {path}")

    workflow = read(".github/workflows/validate.yml")
    for marker in (
        "permissions:\n  contents: read",
        "requirements-dev.txt",
        "scripts/verify_generated_artifacts.py",
        "sha256sum --check",
    ):
        check(
            marker in workflow, f"validation workflow lacks required marker: {marker}"
        )


def validate_links() -> None:
    markdown_files = (
        list(ROOT.glob("*.md"))
        + list((ROOT / "docs").rglob("*.md"))
        + list((ROOT / "research").rglob("*.md"))
    )
    pattern = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
    for md in markdown_files:
        text = md.read_text(encoding="utf-8")
        for raw in pattern.findall(text):
            target = raw.strip().split()[0].strip("<>")
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target = unquote(target.split("#", 1)[0])
            if not target:
                continue
            check(
                (md.parent / target).resolve().exists(),
                f"broken local link in {md.relative_to(ROOT)}: {raw}",
            )


def calculate_score(row: dict[str, str]) -> int:
    return (
        int(row["failed_authentication"]) * 10
        + int(row["privilege_change"]) * 25
        + (15 if row["resource_sensitivity"] in {"high", "critical"} else 0)
        + int(row["after_hours"]) * 10
        + (15 if row["device_posture"] == "noncompliant" else 0)
        + int(row["high_risk_country"]) * 20
        + int(row["threat_intel_match"]) * 25
    )


def tier(score: int) -> str:
    return "Low" if score < 25 else "Medium" if score < 50 else "High"


def validate_examples() -> None:
    with (ROOT / "examples/synthetic-identity-events.csv").open(
        newline="", encoding="utf-8"
    ) as fh:
        events = list(csv.DictReader(fh))
    with (ROOT / "examples/sample-risk-output.csv").open(
        newline="", encoding="utf-8"
    ) as fh:
        outputs = list(csv.DictReader(fh))

    check(len(events) == 12, "synthetic event row count must be 12")
    check(len(outputs) == 12, "risk output row count must be 12")
    event_ids = [r["event_id"] for r in events]
    output_ids = [r["event_id"] for r in outputs]
    check(len(set(event_ids)) == len(event_ids), "duplicate event IDs")
    check(len(set(output_ids)) == len(output_ids), "duplicate output IDs")
    check(set(event_ids) == set(output_ids), "event/output identifier sets differ")

    by_id = {r["event_id"]: r for r in outputs}
    for event in events:
        expected = calculate_score(event)
        output = by_id[event["event_id"]]
        check(
            int(output["risk_score"]) == expected,
            f"score mismatch for {event['event_id']}",
        )
        check(
            output["risk_level"] == tier(expected),
            f"tier mismatch for {event['event_id']}",
        )
        check(
            output["score_type"] == "heuristic-risk",
            f"score type mismatch for {event['event_id']}",
        )
        check(
            output["calibrated_probability"] == "",
            f"synthetic probability must be blank for {event['event_id']}",
        )
        check(
            output["calibration_status"] == "not-calibrated",
            f"calibration status mismatch for {event['event_id']}",
        )
        check(
            output["authority_status"] == "not-evaluated",
            f"authority must be not-evaluated for {event['event_id']}",
        )

    counts = Counter(r["risk_level"] for r in outputs)
    check(
        counts == Counter({"Medium": 8, "High": 3, "Low": 1}),
        f"unexpected risk counts: {dict(counts)}",
    )
    proof = read("docs/proof-of-concept.md")
    for label, count in (("High", 3), ("Medium", 8), ("Low", 1)):
        check(
            re.search(rf"\| {label} \| {count} \|", proof) is not None,
            f"proof-of-concept lacks {label}={count}",
        )


def validate_json(use_jsonschema: bool) -> None:
    pairs = [
        ("schemas/aitir-event-v2.schema.json", "examples/aitir-event-v2.example.json"),
        (
            "schemas/aitir-evidence-v2.schema.json",
            "examples/aitir-evidence-v2.example.json",
        ),
        (
            "schemas/aitir-decision-v2.schema.json",
            "examples/aitir-decision-v2.example.json",
        ),
    ]
    for schema_path, example_path in pairs:
        schema = json.loads(read(schema_path))
        example = json.loads(read(example_path))
        check(
            schema.get("$schema") == "https://json-schema.org/draft/2020-12/schema",
            f"wrong draft in {schema_path}",
        )
        check(
            example.get("schema_version") == "2.0.0",
            f"wrong example version in {example_path}",
        )
        expected_id = (
            "https://raw.githubusercontent.com/sajjad47/AITIR-Framework/"
            f"v2.0.0/{schema_path}"
        )
        check(
            schema.get("$id") == expected_id, f"non-release schema ID in {schema_path}"
        )
        if use_jsonschema:
            from jsonschema import Draft202012Validator, FormatChecker

            validator = Draft202012Validator(schema, format_checker=FormatChecker())
            errors = sorted(
                validator.iter_errors(example),
                key=lambda e: list(e.path),
            )
            check(
                not errors,
                f"{example_path} schema errors: "
                + "; ".join(e.message for e in errors),
            )

            if schema_path.endswith("aitir-decision-v2.schema.json"):
                negative_cases = []

                missing_mode = copy.deepcopy(example)
                del missing_mode["authority"]["authorization_mode"]
                negative_cases.append(("missing authorization mode", missing_mode))

                failed_guard = copy.deepcopy(example)
                failed_guard["guards"][0]["passed"] = False
                failed_guard["guards"][0]["reason_code"] = "TEST_FAILURE"
                negative_cases.append(("authorized failed guard", failed_guard))

                duplicate_guard = copy.deepcopy(example)
                duplicate_guard["guards"][-1]["guard_id"] = "G1"
                negative_cases.append(("duplicate guard category", duplicate_guard))

                denied_as_authorized = copy.deepcopy(example)
                denied_as_authorized["disposition"] = "deny"
                negative_cases.append(
                    ("denied disposition with authorized state", denied_as_authorized)
                )

                t3_system_mode = copy.deepcopy(example)
                t3_system_mode["decision_tier"] = "T3"
                negative_cases.append(("T3 system-preapproved mode", t3_system_mode))

                dual_control_single_approval = copy.deepcopy(example)
                dual_control_single_approval["authority"]["authorization_mode"] = (
                    "dual-control"
                )
                negative_cases.append(
                    ("dual control with one approval", dual_control_single_approval)
                )

                for name, invalid in negative_cases:
                    check(
                        not validator.is_valid(invalid),
                        f"decision schema accepted negative case: {name}",
                    )


def validate_materials() -> None:
    for path in (
        "public-materials/AITIR-Technical-Exhibit.pdf",
        "public-materials/AITIR-Future-Development-Plan.pdf",
        "docs/assets/aitir-framework-architecture.png",
    ):
        p = ROOT / path
        check(p.exists(), f"missing generated artifact: {path}")
        if p.exists():
            check(
                p.stat().st_size > 1000,
                f"generated artifact is unexpectedly small: {path}",
            )


def hashes() -> dict[str, str]:
    paths = [
        "examples/synthetic-identity-events.csv",
        "examples/sample-risk-output.csv",
        "schemas/aitir-event-v2.schema.json",
        "schemas/aitir-evidence-v2.schema.json",
        "schemas/aitir-decision-v2.schema.json",
        "public-materials/AITIR-Technical-Exhibit.pdf",
        "public-materials/AITIR-Future-Development-Plan.pdf",
        "docs/assets/aitir-framework-architecture.png",
    ]
    return {
        p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest()
        for p in paths
        if (ROOT / p).exists()
    }


def validate_manifest() -> None:
    manifest_path = ROOT / "ARTIFACTS.sha256"
    check(manifest_path.exists(), "missing ARTIFACTS.sha256")
    if not manifest_path.exists():
        return

    declared: dict[str, str] = {}
    for line in manifest_path.read_text(encoding="utf-8").splitlines():
        if not line or line.startswith("#"):
            continue
        parts = line.split(maxsplit=1)
        check(len(parts) == 2, f"malformed artifact manifest line: {line}")
        if len(parts) != 2:
            continue
        digest, path = parts
        declared[path] = digest

    actual = hashes()
    check(set(declared) == set(actual), "artifact manifest path set is stale")
    for path, digest in actual.items():
        check(
            declared.get(path) == digest, f"artifact manifest digest mismatch: {path}"
        )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--jsonschema",
        action="store_true",
        help="validate examples with the jsonschema package",
    )
    parser.add_argument("--hashes", action="store_true", help="print artifact hashes")
    args = parser.parse_args()
    validate_version()
    validate_links()
    validate_examples()
    validate_json(args.jsonschema)
    validate_materials()
    validate_manifest()
    if ERRORS:
        print(f"FAIL: {len(ERRORS)} error(s) across {CHECKS} checks")
        for error in ERRORS:
            print(f"- {error}")
        return 1
    print(f"PASS: {CHECKS} repository checks")
    if args.hashes:
        print(json.dumps(hashes(), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
