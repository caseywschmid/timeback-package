# Changelog

All notable changes to this project will be documented in this file.

The format is based on Keep a Changelog and adheres to Semantic Versioning.

## [Unreleased]

-

## [0.1.3] - 2025-10-31

### Added
- OneRoster Rostering: `create_user`, `update_user`, `delete_user` endpoints with docs and tests.
- Integration test for user CRUD (net-zero cleanup).
- Timeback error models (BadRequest/Unauthorized/Forbidden/NotFound/Unprocessable/TooMany/Server) with typed exception attachment.

### Changed
- Models aligned with OpenAPI: added `children` to Org, required fields on LineItem, `schoolYear` int on AcademicSession.
- `create_user` request: `sourcedId` optional; auto-generated UUID when omitted.

### Fixed
- Pydantic v2 root model usage in error details (use RootModel).

## [0.1.2] - 2025-10-30

### Changed
- OneRoster Rostering: renamed endpoint `list_users` to `get_all_users` to match OpenAPI key.

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

[Unreleased]: https://github.com/caseywschmid/timeback-package/compare/v0.1.3...HEAD
[0.1.3]: https://github.com/caseywschmid/timeback-package/compare/v0.1.2...v0.1.3
[0.1.2]: https://github.com/caseywschmid/timeback-package/compare/v0.1.1...v0.1.2
[0.1.1]: https://github.com/caseywschmid/timeback-package/compare/v0.1.0...v0.1.1
[0.1.0]: https://github.com/caseywschmid/timeback-package/releases/tag/v0.1.0
