## QTI API — Create Test Part

### POST /assessment-tests/{assessmentTestIdentifier}/test-parts

- Method: POST
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Create a new test part within an assessment test. Test parts organize sections and define navigation behaviors (linear/nonlinear) and submission modes. The assessment test's XML structure is automatically updated.

Path params:

- `assessmentTestIdentifier` (string, required): Unique identifier of the parent assessment test

Request body:

- `identifier` (string, required): Unique identifier for the test part
- `navigationMode` (string, required): "linear" or "nonlinear"
- `submissionMode` (string, required): "individual" or "simultaneous"
- `qti-assessment-section` (array, required): At least one section

Successful response (HTTP 201):

- Body: Created test part object
- Key fields: Same as search response plus `rawXml` and `content`

Error responses:

- 400/422: Request/validation → raises `RequestError`
- 401: Unauthorized → raises `AuthError`
- 404: Not Found (parent test) → raises `NotFoundError`
- 429: Too Many Requests → raises `RateLimitError`
- 5xx: Server errors → raises `ServerError`

Python usage:

```python
from timeback import Timeback
from timeback.models.request import TimebackCreateTestPartRequest
from timeback.models.timeback_qti_section import TimebackQTISection
from timeback.enums import TimebackQTINavigationMode, TimebackQTISubmissionMode

client = Timeback()

# Create a test part with linear navigation
request = TimebackCreateTestPartRequest(
    identifier="part-001",
    navigation_mode=TimebackQTINavigationMode.LINEAR,
    submission_mode=TimebackQTISubmissionMode.INDIVIDUAL,
    qti_assessment_section=[
        TimebackQTISection(
            identifier="section-001",
            title="Introduction Section"
        )
    ]
)
part = client.qti.create_test_part("test-001", request)

print(f"Created: {part.identifier}")
print(f"Navigation: {part.navigation_mode.value}")

# Create with multiple sections
request = TimebackCreateTestPartRequest(
    identifier="part-002",
    navigation_mode=TimebackQTINavigationMode.NONLINEAR,
    submission_mode=TimebackQTISubmissionMode.SIMULTANEOUS,
    qti_assessment_section=[
        TimebackQTISection(identifier="section-a", title="Section A"),
        TimebackQTISection(identifier="section-b", title="Section B"),
        TimebackQTISection(identifier="section-c", title="Section C"),
    ]
)
part = client.qti.create_test_part("test-001", request)

# Create with hidden section
request = TimebackCreateTestPartRequest(
    identifier="part-003",
    navigation_mode=TimebackQTINavigationMode.LINEAR,
    submission_mode=TimebackQTISubmissionMode.INDIVIDUAL,
    qti_assessment_section=[
        TimebackQTISection(
            identifier="hidden-section",
            title="Hidden Section",
            visible=False
        )
    ]
)
part = client.qti.create_test_part("test-001", request)
```

Notes:

- Navigation modes:
  - `linear`: Items must be answered in sequence
  - `nonlinear`: Items can be answered in any order
- Submission modes:
  - `individual`: Responses submitted per item
  - `simultaneous`: All responses submitted at once
- At least one section is required
- The parent assessment test's XML is automatically updated


