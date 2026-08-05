# Release Process

**Applies from:** AITIR Framework 2.0.0

This process keeps public releases traceable, reproducible, and consistent with the repository's evidence boundary. A release tag records repository state; it does not certify an implementation or convert synthetic evidence into operational evidence.

## 1. Establish scope

1. Classify the change under semantic versioning.
2. Confirm the release status and evidence class.
3. Record breaking changes and migration requirements.
4. Keep submitted work, published work, reproduced findings, and repository artifacts distinct.

## 2. Synchronize version declarations

Update and reconcile:

- `VERSION`;
- `CHANGELOG.md`;
- `CITATION.cff`;
- versioned documentation headers;
- JSON Schema `$id` values and `schema_version` constraints;
- PDF and architecture source metadata;
- release notes and asset names.

Schema `$id` values for a final release must reference its immutable Git tag.

## 3. Build with the pinned toolchain

```bash
uv run --with-requirements requirements-dev.txt python scripts/build_architecture.py
uv run --with-requirements requirements-dev.txt python scripts/build_public_materials.py
```

Rebuild twice when the toolchain or build scripts change and verify byte-identical outputs.

## 4. Validate

```bash
python3 scripts/validate_repository.py
uv run --with-requirements requirements-dev.txt python scripts/validate_repository.py --jsonschema
uv run --with-requirements requirements-dev.txt python scripts/verify_generated_artifacts.py
uv run --with-requirements requirements-dev.txt ruff check scripts
uv run --with-requirements requirements-dev.txt ruff format --check scripts
uvx --from cffconvert==2.0.0 cffconvert --validate -i CITATION.cff
npx --yes markdownlint-cli2@0.23.2 '**/*.md' '#.git'
git diff --check
```

Validate all local links and resolve every external standards/DOI URL. Bot-protected publisher endpoints may be recorded as access-controlled only after a valid DOI redirect is established.

## 5. Inspect generated artifacts

For every architecture image and PDF:

- compare the generated output with its source;
- verify dimensions, page size, page count, titles, version markers, fonts, and extractable text;
- inspect every page visually for clipping, overlap, unreadable text, accidental blank pages, and inconsistent hierarchy;
- verify `ARTIFACTS.sha256` after the final build.

## 6. Review and merge

1. Use a focused release branch and pull request.
2. Require the repository-validation workflow to pass.
3. Review unsupported claims, personal data, secrets, generated diffs, and publication status.
4. Squash-merge to maintain linear release history.

## 7. Tag and publish

1. Create an annotated tag such as `v2.0.0` at the validated `main` commit.
2. Push the tag without rewriting prior tags.
3. Create a non-prerelease GitHub Release with professional notes.
4. Attach the public PDFs, architecture PNG, and `ARTIFACTS.sha256`.
5. Confirm GitHub's source archives point to the tagged commit.

## 8. Post-release verification

Confirm:

- the new release is marked Latest;
- the tag and `main` identify the intended release commit;
- every uploaded asset downloads and matches the manifest;
- the documentation site resolves and links to the release;
- the changelog comparison link resolves;
- repository topics, description, security reporting, and branch protection remain enabled.

Do not move or recreate a published release tag. Corrections require a new semantic version.
