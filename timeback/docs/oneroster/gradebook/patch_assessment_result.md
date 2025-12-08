## OneRoster — Gradebook - Patch Assessment Result

### PATCH /ims/oneroster/gradebook/v1p2/assessmentResults/{sourcedId}

- Method: PATCH
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Partially update an assessment result with metadata merging support.

Path params:

- `sourcedId` (string, required): The assessment result's sourcedId

Request body:

- `assessmentResult` (object, required): Partial assessment result object
  - All fields are optional; only provided fields will be updated
  - `metadata` is merged with existing metadata (not replaced)

Successful response (HTTP 200):

- Body: `{ "assessmentResult": AssessmentResult }`

Error responses:

- 400/422: Request/validation → raises `RequestError`
- 401: Unauthorized → raises `AuthError`
- 403: Forbidden → raises `RequestError`
- 404: Assessment result not found → raises `NotFoundError`
- 429: Too Many Requests → raises `RateLimitError`
- 5xx: Server errors → raises `ServerError`

Python usage:

```python
from timeback import Timeback
from timeback.models.request import TimebackPatchAssessmentResultRequest, TimebackPatchAssessmentResultBody

client = Timeback()

# Partial update - only update score and comment
body = TimebackPatchAssessmentResultBody(
    score=95.0,
    comment="Updated via PATCH",
)

request = TimebackPatchAssessmentResultRequest(
    sourced_id="<sourcedId>",
    assessmentResult=body
)
response = client.oneroster.gradebook.patch_assessment_result(request)
print(f"Updated: {response.assessmentResult.sourcedId}")
```

Notes:

- Only provided fields are updated; others remain unchanged.
- Metadata is merged with existing metadata, not replaced.
- Use PUT for full replacement, PATCH for partial updates.

