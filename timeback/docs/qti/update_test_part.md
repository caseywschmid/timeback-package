## QTI API — Update Test Part

### PUT /assessment-tests/{assessmentTestIdentifier}/test-parts/{identifier}

- Method: PUT
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Update an existing test part including its navigation mode, submission mode, and sections. The parent assessment test's XML is regenerated.

Path params:

- `assessmentTestIdentifier` (string, required): Unique identifier of the parent assessment test
- `identifier` (string, required): Unique identifier of the test part to update

Request body:

- `identifier` (string, required): Test part identifier (should match path)
- `navigationMode` (string, required): "linear" or "nonlinear"
- `submissionMode` (string, required): "individual" or "simultaneous"
- `qti-assessment-section` (array, required): At least one section

Successful response (HTTP 200):

- Body: Updated test part object
- Key fields: Same as create response

Error responses:

- 400/422: Request/validation → raises `RequestError`
- 401: Unauthorized → raises `AuthError`
- 404: Not Found → raises `NotFoundError`
- 429: Too Many Requests → raises `RateLimitError`
- 5xx: Server errors → raises `ServerError`

Python usage:

```python
from timeback import Timeback
from timeback.models.request import TimebackUpdateTestPartRequest
from timeback.models.timeback_qti_section import TimebackQTISection
from timeback.enums import TimebackQTINavigationMode, TimebackQTISubmissionMode

client = Timeback()

# Update navigation and submission modes
request = TimebackUpdateTestPartRequest(
    identifier="part-001",
    navigation_mode=TimebackQTINavigationMode.NONLINEAR,
    submission_mode=TimebackQTISubmissionMode.SIMULTANEOUS,
    qti_assessment_section=[
        TimebackQTISection(identifier="section-001", title="Section 1"),
        TimebackQTISection(identifier="section-002", title="Section 2"),
    ]
)
part = client.qti.update_test_part("test-001", "part-001", request)

print(f"Updated: {part.identifier}")
print(f"Navigation: {part.navigation_mode.value}")
print(f"Submission: {part.submission_mode.value}")

# Update sections only
request = TimebackUpdateTestPartRequest(
    identifier="part-001",
    navigation_mode=TimebackQTINavigationMode.LINEAR,
    submission_mode=TimebackQTISubmissionMode.INDIVIDUAL,
    qti_assessment_section=[
        TimebackQTISection(identifier="new-section", title="New Section"),
    ]
)
part = client.qti.update_test_part("test-001", "part-001", request)
```

Notes:

- All required fields must be provided (identifier, navigationMode, submissionMode, qti-assessment-section)
- The entire test part structure is replaced
- At least one section is required
- The parent assessment test's XML is automatically regenerated


