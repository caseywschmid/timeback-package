## OneRoster — Gradebook - Put Assessment Result

### PUT /ims/oneroster/gradebook/v1p2/assessmentResults/{sourcedId}

- Method: PUT
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Update or create an assessment result by `sourcedId`.

Path params:

- `sourcedId` (string, required): The assessment result's sourcedId

Request body:

- `assessmentResult` (AssessmentResult, required): The assessment result object
  - Required fields: `assessmentLineItem`, `student`, `scoreStatus`, `scoreDate`
  - Optional fields: `sourcedId`, `status`, `metadata`, `score`, `textScore`, `scoreScale`, `scorePercentile`, `comment`, `learningObjectiveSet`, `inProgress`, `incomplete`, `late`, `missing`

Successful response (HTTP 201):

- Body: `{ "assessmentResult": AssessmentResult }`

Error responses:

- 400/422: Request/validation → raises `RequestError`
- 401: Unauthorized → raises `AuthError`
- 403: Forbidden → raises `RequestError`
- 429: Too Many Requests → raises `RateLimitError`
- 5xx: Server errors → raises `ServerError`

Python usage:

```python
from timeback import Timeback
from timeback.models.request import TimebackPutAssessmentResultRequest, TimebackPutAssessmentResultBody
from timeback.models.timeback_assessment_line_item_ref import TimebackAssessmentLineItemRef
from timeback.models.timeback_student_ref import TimebackStudentRef
from timeback.enums import TimebackScoreStatus

client = Timeback()

body = TimebackPutAssessmentResultBody(
    assessmentLineItem=TimebackAssessmentLineItemRef(sourcedId="<ali-id>"),
    student=TimebackStudentRef(sourcedId="<student-id>"),
    scoreStatus=TimebackScoreStatus.FULLY_GRADED,
    scoreDate="2024-01-15",
    score=92.5,
)

request = TimebackPutAssessmentResultRequest(
    sourced_id="<sourcedId>",
    assessmentResult=body
)
response = client.oneroster.gradebook.put_assessment_result(request)
print(f"Updated: {response.assessmentResult.sourcedId}")
```

Notes:

- Uses upsert semantics: creates if doesn't exist, updates if it does.
- The `sourcedId` in the path and body should match.

