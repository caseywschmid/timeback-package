# Changelog

All notable changes to this project will be documented in this file.

The format is based on Keep a Changelog and adheres to Semantic Versioning.

## [Unreleased]

-

## [0.2.0] - 2025-12-09

### Added

**OneRoster Rostering API - 70+ new endpoints:**

- **Classes**: `get_all_classes`, `create_class`, `get_class`, `update_class`, `delete_class`, `get_classes_for_school`, `get_classes_for_user`, `get_classes_for_course`
- **Users**: `create_user`, `get_user`, `update_user`, `delete_user`, `get_all_users`, `get_users_for_class`, `get_users_for_class_in_school`, `get_users_for_school`
- **Students**: `get_all_students`, `get_student`, `get_students_for_class`, `get_students_for_class_in_school`, `get_students_for_school`, `register_student_credentials`
- **Teachers**: `get_all_teachers`, `get_teacher`, `get_teachers_for_class`, `get_teachers_for_class_in_school`, `get_teachers_for_school`
- **Terms**: `get_all_terms`, `create_term`, `get_term`, `update_term`, `delete_term`, `get_terms_for_school`
- **Grading Periods**: `get_all_grading_periods`, `create_grading_period`, `get_grading_period`, `update_grading_period`, `delete_grading_period`, `get_grading_periods_for_term`, `create_grading_period_for_term`
- **Enrollments**: `get_all_enrollments`, `create_enrollment`, `get_enrollment`, `update_enrollment`, `patch_enrollment`, `delete_enrollment`, `get_enrollments_for_class_in_school`, `get_enrollments_for_school`
- **Demographics**: `get_all_demographics`, `create_demographic`, `get_demographic`, `update_demographic`, `delete_demographic`
- **Courses**: `get_all_courses`, `create_course`, `get_course`, `update_course`, `delete_course`, `get_courses_for_school`
- **Course Components**: `get_all_course_components`, `create_course_component`, `get_course_component`, `update_course_component`, `delete_course_component`
- **Component Resources**: `get_all_component_resources`, `create_component_resource`, `get_component_resource`, `update_component_resource`, `delete_component_resource`
- **Academic Sessions**: `get_all_academic_sessions`, `create_academic_session`, `get_academic_session`, `update_academic_session`, `delete_academic_session`
- **Organizations**: `get_all_orgs`, `create_org`, `get_org`, `update_org`, `delete_org`
- **Schools**: `get_all_schools`, `create_school`, `get_school`, `update_school`, `delete_school`

**OneRoster Gradebook API - Full CRUD:**

- **Categories**: `get_all_categories`, `create_category`, `get_category`, `put_category`, `delete_category`
- **Assessment Results**: `get_all_assessment_results`, `create_assessment_result`, `get_assessment_result`, `put_assessment_result`, `patch_assessment_result`, `delete_assessment_result`
- **Assessment Line Items**: `get_all_assessment_line_items`, `create_assessment_line_item`, `get_assessment_line_item`, `put_assessment_line_item`, `patch_assessment_line_item`, `delete_assessment_line_item`

**OneRoster Resources API - Full CRUD:**

- **Resources**: `get_all_resources`, `create_resource`, `get_resource`, `update_resource`, `delete_resource`, `get_resources_for_class`, `get_resources_for_course`, `get_resources_for_user`

**New Models:**

- `TimebackClass`, `TimebackCourse`, `TimebackCourseComponent`, `TimebackEnrollment`, `TimebackDemographic`, `TimebackGradingPeriod`, `TimebackCategory`, `TimebackAssessmentResult`, `TimebackAssessmentLineItem`, `TimebackResource`
- Request/response models for all new endpoints

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

[Unreleased]: https://github.com/caseywschmid/timeback-package/compare/v0.2.0...HEAD
[0.2.0]: https://github.com/caseywschmid/timeback-package/compare/v0.1.5...v0.2.0
[0.1.5]: https://github.com/caseywschmid/timeback-package/compare/v0.1.4...v0.1.5
[0.1.4]: https://github.com/caseywschmid/timeback-package/compare/v0.1.3...v0.1.4
[0.1.3]: https://github.com/caseywschmid/timeback-package/compare/v0.1.2...v0.1.3
[0.1.2]: https://github.com/caseywschmid/timeback-package/compare/v0.1.1...v0.1.2
[0.1.1]: https://github.com/caseywschmid/timeback-package/compare/v0.1.0...v0.1.1
[0.1.0]: https://github.com/caseywschmid/timeback-package/releases/tag/v0.1.0
