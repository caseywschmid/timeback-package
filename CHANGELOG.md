# Changelog

All notable changes to this project will be documented in this file.

The format is based on Keep a Changelog and adheres to Semantic Versioning.

## [Unreleased]

-

## [0.1.1] - 2025-10-30

### Added
- OneRoster Rostering: `list_users` endpoint (`client.oneroster.rostering.list_users(...)`).

## [0.1.0] - 2025-10-30

### Added
- Initial public release to PyPI.
- Top-level `Timeback` client with environment-aware configuration and OAuth2 Client Credentials.
- Separate base URLs and `HttpClient` instances for OneRoster, QTI, and Caliper; exposed `qti_http` and `caliper_http`.
- OneRoster service container with `RosteringService` and endpoint:
  - `get_user(sourced_id, fields=None)`
- Pydantic models and enums for OneRoster and QTI primitives referenced by the client.
- Documentation:
  - `timeback/docs/oneroster/rostering/get_user.md`
  - `timeback/docs/package_setup.md` (client setup)
- Testing setup with unit tests (and integration tests marked with `@pytest.mark.integration`).

[Unreleased]: https://github.com/caseywschmid/timeback-package/compare/v0.1.1...HEAD
[0.1.1]: https://github.com/caseywschmid/timeback-package/compare/v0.1.0...v0.1.1
[0.1.0]: https://github.com/caseywschmid/timeback-package/releases/tag/v0.1.0
