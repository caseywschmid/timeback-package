## Timeback Python Package Setup

This document explains how the client initializes configuration, authentication, and HTTP wiring, and how separate base URLs for OneRoster, QTI, and Caliper are handled.

### Overview

- **Top-level client**: `Timeback` in `timeback/client.py`
- **Configuration**: `Settings` in `timeback/config.py`
- **Auth**: OAuth2 Client Credentials via `OAuth2ClientCredentials` in `timeback/auth.py`
- **HTTP**: `HttpClient` in `timeback/http/http.py`
- **Services**: 
  - `OneRosterService` in `timeback/services/oneroster/oneroster.py` with `RosteringService`, `GradebookService`, and `ResourcesService`
  - `PowerPathService` in `timeback/services/powerpath/powerpath_service.py` for placement, screening, lesson plans, and assessments
  - `QTIService` in `timeback/services/qti/qti_service.py` for stimuli, assessment items, assessment tests, and validation

The client constructs separate `HttpClient` instances for each service family that may use different base URLs:
- OneRoster (uses the primary API base URL)
- PowerPath (shares the primary API base URL with OneRoster)
- QTI (dedicated base URL)
- Caliper (dedicated base URL)

### Environments and Base URLs

Environment is selected via `TIMEBACK_ENVIRONMENT` or passed to `Timeback(...)` as `environment`. Allowed values: `production`, `staging`.

Defaults per environment:
- **production**
  - OneRoster API base: `https://api.alpha-1edtech.ai/`
  - QTI API base: `https://qti.alpha-1edtech.ai/api`
  - Caliper API base: `https://caliper.alpha-1edtech.ai`
- **staging**
  - OneRoster API base: `https://api.staging.alpha-1edtech.ai/`
  - QTI API base: `https://qti-staging.alpha-1edtech.ai/api`
  - Caliper API base: `https://caliper-staging.alpha-1edtech.ai`

These defaults are defined in `timeback/config.py` and normalized (no trailing slash for QTI/Caliper; OneRoster retains trailing slash). You may override them via constructor args or environment variables (see below).

### Settings Configuration

File: `timeback/config.py`

Required environment variables:
- `TIMEBACK_CLIENT_ID`
- `TIMEBACK_CLIENT_SECRET`
- `TIMEBACK_ENVIRONMENT` (one of `production`, `staging`)

Optional per-service overrides:
- `TIMEBACK_QTI_API_BASE_URL`
- `TIMEBACK_CALIPER_API_BASE_URL`

Constructor overrides (take precedence over env):
- `Timeback(qti_api_base_url=..., caliper_api_base_url=...)`

### Authentication

File: `timeback/auth.py`

- Auth uses OAuth2 Client Credentials against the environment-specific IDP base URL defined in `Settings`.
- Tokens are cached in-memory and refreshed automatically before expiry.

IDP base URLs (current):
- production: `https://prod-beyond-timeback-api-2-idp.auth.us-east-1.amazoncognito.com`
- staging: `https://alpha-auth-development-idp.auth.us-west-2.amazoncognito.com`

Note: If QTI/Caliper require distinct IDPs later, the design allows introducing separate token providers without changing the external `Timeback` API.

### HTTP Client Wiring

File: `timeback/client.py`

On initialization, the client creates one token provider and three HTTP clients:
- `self._http_oneroster = HttpClient(base_url=self.settings.api_base_url, ...)`
- `self._http_qti = HttpClient(base_url=self.settings.qti_api_base_url, ...)`
- `self._http_caliper = HttpClient(base_url=self.settings.caliper_api_base_url, ...)`

Exposed properties:
- `self.oneroster` → `OneRosterService(self._http_oneroster)`
- `self.powerpath` → `PowerPathService(self._http_oneroster)` (shares HTTP client with OneRoster)
- `self.qti` → `QTIService(self._http_qti)` (uses dedicated QTI base URL)
- `self.qti_http` → raw `HttpClient` for QTI base URL (for backwards compatibility)
- `self.caliper_http` → raw `HttpClient` for Caliper base URL

`HttpClient` performs bearer auth header injection and basic retry handling for GET requests, and raises typed errors for common failure cases.

### OneRoster Service Exposure

File: `timeback/services/oneroster/oneroster.py`

The OneRoster container currently exposes:
- `self.rostering` → `RosteringService`
- `self.gradebook` → `GradebookService`
- `self.resources` → `ResourcesService`

Available endpoints (examples):
- `client.oneroster.rostering.get_user(request)`
- `client.oneroster.gradebook.get_all_categories(request)`
- `client.oneroster.resources.get_resource(request)`

### PowerPath Service Exposure

File: `timeback/services/powerpath/powerpath_service.py`

The PowerPath service provides methods for:
- **Placement**: `get_all_placement_tests`, `get_current_level`, `get_next_placement_test`, `get_subject_progress`
- **Screening**: `get_results`, `get_session`, `assign_test`
- **Lesson Plans**: `create_lesson_plan`, `get_tree`, `get_operations`, `sync_operations`, `get_course_progress`, etc.
- **Assessments**: `create_new_attempt`, `get_next_question`, `update_student_question_response`, etc.

PowerPath uses the same base URL as OneRoster (`/powerpath/...` on `api.alpha-1edtech.ai`).

Available endpoints (examples - to be implemented):
- `client.powerpath.get_all_placement_tests(request)`
- `client.powerpath.get_lesson_plan(request)`
- `client.powerpath.create_new_attempt(request)`

### QTI Service Exposure

File: `timeback/services/qti/qti_service.py`

The QTI service provides methods for managing Question and Test Interoperability content:
- **Stimuli**: `search_stimuli`, `create_stimulus`, `get_stimulus`, `update_stimulus`, `delete_stimulus`
- **Assessment Items**: `search_assessment_items`, `create_assessment_item`, `get_assessment_item`, `process_response`, etc.
- **Assessment Tests**: `search_assessment_tests`, `create_assessment_test`, `get_assessment_test`, `get_all_questions`, etc.
- **Test Parts**: `search_test_parts`, `create_test_part`, `get_test_part`, etc.
- **Sections**: `search_sections`, `create_section`, `add_assessment_item`, `update_assessment_item_order`, etc.
- **Feedback**: `create_question_feedback`, `create_lesson_feedback`, `get_feedback_by_lesson_id`, `delete_feedback`
- **Validation**: `validate_xml`, `validate_batch`

QTI uses a dedicated base URL separate from OneRoster:
- Production: `https://qti.alpha-1edtech.ai/api`
- Staging: `https://qti-staging.alpha-1edtech.ai/api`

Available endpoints (examples - to be implemented):
- `client.qti.search_assessment_items(request)`
- `client.qti.get_assessment_test(request)`
- `client.qti.validate_xml(request)`

### Caliper Access Point

Caliper is not yet scaffolded as a service. For now, the client exposes the configured HTTP client:
- `client.caliper_http` (use for calls to the Caliper API base)

This lets you start integrating quickly while keeping the codebase modular for future service classes.

### Usage Examples

Basic initialization using environment variables only:

```python
from timeback import Timeback

client = Timeback()

# OneRoster endpoints
user = client.oneroster.rostering.get_user(request)

# PowerPath endpoints (when implemented)
# placement_tests = client.powerpath.get_all_placement_tests(request)
# lesson_plan = client.powerpath.get_lesson_plan(request)

# QTI endpoints (when implemented)
# items = client.qti.search_assessment_items(request)
# test = client.qti.get_assessment_test(request)
```

Override QTI and Caliper base URLs explicitly via constructor:

```python
from timeback import Timeback

client = Timeback(
    environment="staging",
    qti_api_base_url="https://my-qti.example.com/api",
    caliper_api_base_url="https://my-caliper.example.com",
)

# Existing OneRoster endpoint
user = client.oneroster.rostering.get_user("sourced-id")

# QTI service (when endpoints are implemented)
# items = client.qti.search_assessment_items(request)

# Raw HTTP client for Caliper (service class can be added later)
caliper_status = client.caliper_http.get("/status")
```

Override via environment variables:

```bash
export TIMEBACK_ENVIRONMENT=production
export TIMEBACK_CLIENT_ID=...        # required
export TIMEBACK_CLIENT_SECRET=...    # required

export TIMEBACK_QTI_API_BASE_URL=https://qti.custom.example.com/api
export TIMEBACK_CALIPER_API_BASE_URL=https://caliper.custom.example.com
```

### Future Extensions

- Implement remaining PowerPath endpoints (placement, screening, lesson plans, assessments).
- Implement QTI endpoints (stimuli, assessment items, assessment tests, validation).
- Introduce separate token providers if QTI/Caliper require distinct IDPs.
- Add dedicated service class for Caliper.
- Add dedicated service classes for CASE API.
- Extend `HttpClient` with additional HTTP verbs as new write endpoints are added.


