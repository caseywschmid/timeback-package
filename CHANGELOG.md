# Changelog

All notable changes to this project will be documented in this file.

The format is based on Keep a Changelog and adheres to Semantic Versioning.

## [Unreleased]

-

## [0.1.5] - 2025-11-10

### Added
- OneRoster Rostering: `add_agent` endpoint (`client.oneroster.rostering.add_agent(request)`) with docs and tests
- OneRoster Rostering: `get_agent_for` endpoint (`client.oneroster.rostering.get_agent_for(user_id)`) with docs and tests
- OneRoster Rostering: `get_agents` endpoint (`client.oneroster.rostering.get_agents(user_id)`) with docs and tests
- Request/response models for all endpoints: `TimebackGetUserRequest`, `TimebackGetAllUsersRequest`, `TimebackUpdateUserRequest`, `TimebackAddAgentRequest`, `TimebackDeleteAgentRequest`, and corresponding response models
- `TimebackAgent` model for agent data
- `TimebackSourcedIdPairs` model for sourced ID pair relationships
- `TimebackQueryParams` model for standardized query parameter handling

### Changed
- `get_user`, `get_all_users`, `update_user`, `delete_agent` now use request models instead of individual parameters
- Consistent request/response model pattern across all endpoints

### Removed
- `parse_user_response` utility (functionality moved to response models)

## [0.1.4] - 2025-01-XX

### Added
- OneRoster Rostering: `delete_agent` endpoint (`client.oneroster.rostering.delete_agent(user_id, agent_sourced_id)`) with docs and tests.

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

[Unreleased]: https://github.com/caseywschmid/timeback-package/compare/v0.1.5...HEAD
[0.1.5]: https://github.com/caseywschmid/timeback-package/compare/v0.1.4...v0.1.5
[0.1.4]: https://github.com/caseywschmid/timeback-package/compare/v0.1.3...v0.1.4
[0.1.3]: https://github.com/caseywschmid/timeback-package/compare/v0.1.2...v0.1.3
[0.1.2]: https://github.com/caseywschmid/timeback-package/compare/v0.1.1...v0.1.2
[0.1.1]: https://github.com/caseywschmid/timeback-package/compare/v0.1.0...v0.1.1
[0.1.0]: https://github.com/caseywschmid/timeback-package/releases/tag/v0.1.0
