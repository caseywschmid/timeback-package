# Opinionated Release Process (PyPI)

This is the single source of truth for how we version, tag, and publish the `timeback` package. No pre-releases.

## Versioning policy

- Semantic Versioning: MAJOR.MINOR.PATCH
- Bump rules:
  - MAJOR: breaking API changes
  - MINOR: new features, backward compatible (e.g., new endpoints, optional args)
  - PATCH: bug fixes, internal refactors, docs/tests

## Single place to update the version

- `pyproject.toml` → `[tool.poetry].version` (authoritative for PyPI)
- `timeback/__init__.py` → `__version__` (runtime visibility)

Always keep both in sync in the same commit.

## Branching and PR flow

- Feature work on feature branches → open PR → squash merge to `main` when green.
- Releases are cut from `main` only.
- Hotfixes: branch from `main`, bump PATCH, PR to `main`, release.

## Commit message and tag format

- Version bump commit message: `chore(release): vX.Y.Z`
- Git tag: `vX.Y.Z` matching the package version exactly.

## Changelog

- Maintain `CHANGELOG.md` with sections: Added, Changed, Fixed, Removed, Deprecated, Security.
- Update it in the version bump commit.

## PyPI credentials (one-time)

```bash
poetry config pypi-token.pypi <YOUR_PYPI_TOKEN>
```

## Release checklist (do this in order)

1) Ensure `main` is green

```bash
poetry install
poetry run pytest -q -m "not integration"
# Optional (requires network + env):
poetry run pytest -q -m integration
```

2) Bump version and changelog

```bash
# Edit pyproject.toml and timeback/__init__.py to X.Y.Z
# Edit CHANGELOG.md with entries for X.Y.Z
git add pyproject.toml timeback/__init__.py CHANGELOG.md
git commit -m "chore(release): vX.Y.Z"
```

3) Tag and push

```bash
git tag vX.Y.Z
git push origin main --tags
```

4) Build and publish

```bash
poetry build
poetry publish
```

Artifacts produced:
- `dist/timeback-X.Y.Z.tar.gz`
- `dist/timeback-X.Y.Z-py3-none-any.whl`

5) Verify

```bash
pip install --upgrade pip
pip install timeback==X.Y.Z
python -c "import timeback; print(timeback.__version__)"
```

## What goes where

- Git: hosts source, tags, and changelog. Tag names match package version.
- PyPI: hosts built artifacts for `pip install`.
- README.md: usage and configuration.
- CHANGELOG.md: human-readable changes per version.

## Automation (optional)

- Add a CI job that on pushing a tag `v*`:
  - Verifies version alignment (pyproject.toml == timeback/__init__.py == tag)
  - Runs tests
  - Builds and publishes to PyPI

This keeps local steps minimal while preserving the same policy.