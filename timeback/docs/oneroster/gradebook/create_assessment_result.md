## OneRoster — Gradebook - Create Assessment Result

### POST /ims/oneroster/gradebook/v1p2/assessmentResults

- Method: POST
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Create a new assessment result. The responding system returns the set of sourcedIds that have been allocated to the newly created assessmentResult record.

Request body:

- `assessmentResult` (AssessmentResult, required): The assessment result object to create
  - Required fields:
    - `assessmentLineItem` (object): Reference to the assessment line item `{ "sourcedId": "<id>" }`
    - `student` (object): Reference to the student `{ "sourcedId": "<id>" }`
    - `scoreStatus` (string): Status of the score (e.g., "fully graded", "partially graded", "not submitted")
    - `scoreDate` (string): Date when the score was recorded (ISO 8601 format)
  - Optional fields:
    - `sourcedId` (string): Client-supplied sourcedId (auto-generated UUID if omitted)
    - `status` (string): Assessment result status ("active" or "tobedeleted")
    - `metadata` (object): Custom metadata
    - `score` (number): Numeric score value
    - `textScore` (string): Text representation of the score
    - `scoreScale` (object): Reference to score scale
    - `scorePercentile` (number): Percentile rank of the score
    - `comment` (string): Comment about the result
    - `learningObjectiveSet` (array): Learning objective results
    - `inProgress`, `incomplete`, `late`, `missing` (string): Status indicators

Successful response (HTTP 201):

- Body: `{ "sourcedIdPairs": { "suppliedSourcedId": string, "allocatedSourcedId": string } }`

Error responses:

- 400/422: Request/validation → raises `RequestError`
- 401: Unauthorized → raises `AuthError`
- 403: Forbidden → raises `RequestError`
- 429: Too Many Requests → raises `RateLimitError`
- 5xx: Server errors → raises `ServerError`

Python usage:

```python
from timeback import Timeback
from timeback.models.request import (
    TimebackCreateAssessmentResultRequest,
    TimebackCreateAssessmentResultBody,
)
from timeback.models.timeback_assessment_line_item_ref import TimebackAssessmentLineItemRef
from timeback.models.timeback_student_ref import TimebackStudentRef
from timeback.enums import TimebackScoreStatus

client = Timeback()

body = TimebackCreateAssessmentResultBody(
    assessmentLineItem=TimebackAssessmentLineItemRef(sourcedId="<assessment-line-item-id>"),
    student=TimebackStudentRef(sourcedId="<student-id>"),
    scoreStatus=TimebackScoreStatus.FULLY_GRADED,
    scoreDate="2024-01-15",
    score=85.5,
    comment="Good work!",
)

request = TimebackCreateAssessmentResultRequest(assessmentResult=body)
response = client.oneroster.gradebook.create_assessment_result(request)

print(f"Created with sourcedId: {response.sourcedIdPairs.allocatedSourcedId}")
```

Notes:

- An assessment line item sourcedId and student sourcedId MUST be provided when creating an assessment result.
- If `sourcedId` is not provided in the request, a UUID will be auto-generated.
- The response contains mapping between the supplied sourcedId and the allocated sourcedId.

