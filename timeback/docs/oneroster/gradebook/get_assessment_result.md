## OneRoster — Gradebook - Get Assessment Result

### GET /ims/oneroster/gradebook/v1p2/assessmentResults/{sourcedId}

- Method: GET
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Get a specific assessment result by `sourcedId`.

Path params:

- `sourcedId` (string, required): The assessment result's sourcedId

Query params:

- `fields` (string, optional): Comma-separated list of fields to include

Successful response (HTTP 200):

- Body: `{ "assessmentResult": AssessmentResult }`
- The `AssessmentResult` object includes:
  - required: `sourcedId`, `status`, `assessmentLineItem`, `student`, `scoreDate`, `scoreStatus`
  - optional: `dateLastModified`, `metadata`, `score`, `textScore`, `scoreScale`, `scorePercentile`, `comment`, `learningObjectiveSet`, `inProgress`, `incomplete`, `late`, `missing`

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
from timeback.models.request import TimebackGetAssessmentResultRequest, TimebackQueryParams

client = Timeback()

# Basic request
request = TimebackGetAssessmentResultRequest(sourced_id="<sourcedId>")
response = client.oneroster.gradebook.get_assessment_result(request)

print(f"Score: {response.assessmentResult.score}")
print(f"Status: {response.assessmentResult.scoreStatus}")

# With fields filter
query_params = TimebackQueryParams(fields=["sourcedId", "score", "scoreStatus"])
request_with_fields = TimebackGetAssessmentResultRequest(
    sourced_id="<sourcedId>",
    query_params=query_params
)
response_min = client.oneroster.gradebook.get_assessment_result(request_with_fields)
```

Notes:

- The response contains a single assessment result object.
- The `fields` query parameter allows you to request only specific fields, reducing response size.
- If the assessment result does not exist, a `NotFoundError` is raised.
- Assessment results link students to their scores on specific assessment line items.

