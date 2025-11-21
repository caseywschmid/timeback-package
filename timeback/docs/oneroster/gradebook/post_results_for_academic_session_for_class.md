## OneRoster — Gradebook - Post Results for Academic Session for Class

### POST /ims/oneroster/gradebook/v1p2/classes/{classSourcedId}/academicSessions/{academicSessionSourcedId}/results

- Method: POST
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: To create a set of results for a specific academic session and specific class. The responding system must return the set of sourcedIds that have been allocated to the newly created result records. If the corresponding record cannot be located, the api will return a 404 error code and message 'Class or academic session not found.'

Path params:

- `classSourcedId` (string, required): The sourcedId of the class
- `academicSessionSourcedId` (string, required): The sourcedId of the academic session

Request model:

- `TimebackPostResultsForAcademicSessionForClassRequest` with required fields:
  - `class_sourced_id` (string): The sourcedId of the class (path parameter)
  - `academic_session_sourced_id` (string): The sourcedId of the academic session (path parameter)
  - `results` (List[TimebackCreateResultBody]): Array of result data to create. See TimebackCreateResultBody for structure.

Request body (application/json):

The request body contains a `results` array. Each result object in the array must include the following required fields:

- `lineItem` (object) — Reference to the line item:
  - `sourcedId` (string) — The sourcedId of the line item
- `student` (object) — Reference to the student:
  - `sourcedId` (string) — The sourcedId of the student
- `scoreStatus` (string, enum) — Status of the score: `"exempt"`, `"fully graded"`, `"not submitted"`, `"partially graded"`, or `"submitted"`
- `scoreDate` (string) — Date when the score was recorded (ISO 8601 format)

Optional fields for each result:
- `sourcedId` (string) — Optional; if omitted, this package auto-generates a UUID
- `status` (string, enum: `"active"`, `"tobedeleted"`) — Defaults to `"active"`
- `metadata` (object) — Custom metadata
- `class` (object, nullable) — Reference to class:
  - `sourcedId` (string) — The sourcedId of the class
- `scoreScale` (object, nullable) — Reference to score scale:
  - `sourcedId` (string) — The sourcedId of the score scale
- `score` (number, nullable) — Numeric score value
- `textScore` (string, nullable) — Text representation of the score
- `comment` (string, nullable) — Comment about the result
- `learningObjectiveSet` (array, nullable) — Learning objective results
- `inProgress` (string) — In progress indicator
- `incomplete` (string) — Incomplete indicator
- `late` (string) — Late indicator
- `missing` (string) — Missing indicator

Successful response (HTTP 201):

- Body (per spec):
  - `{ "sourcedIdPairs": { "suppliedSourcedId": string, "allocatedSourcedId": string } }`

Error responses:

- 400: Bad Request → raises `RequestError`
- 401: Unauthorized → raises `AuthError`
- 403: Forbidden → raises `RequestError`
- 404: Class or academic session not found → raises `NotFoundError`
- 422: Unprocessable Entity / Validation Error → raises `RequestError`
- 429: Too Many Requests → raises `RateLimitError`
- 5xx: Server errors → raises `ServerError`

Python usage:

```python
from timeback import Timeback
from timeback.models.request import (
    TimebackPostResultsForAcademicSessionForClassRequest,
    TimebackCreateResultBody,
)
from timeback.models.timeback_sourced_id_ref import TimebackSourcedIdReference
from timeback.enums import TimebackStatus, TimebackScoreStatus

client = Timeback()
class_sourced_id = "class-123"
academic_session_sourced_id = "session-456"

# Create result bodies
result1 = TimebackCreateResultBody(
    sourcedId="result-1",
    lineItem=TimebackSourcedIdReference(sourcedId="line-item-1"),
    student=TimebackSourcedIdReference(sourcedId="student-1"),
    scoreStatus=TimebackScoreStatus.FULLY_GRADED,
    scoreDate="2024-01-15T10:00:00Z",
    score=95.5,
    textScore="A",
    comment="Excellent work",
    class_=TimebackSourcedIdReference(sourcedId=class_sourced_id),
)

result2 = TimebackCreateResultBody(
    sourcedId="result-2",
    lineItem=TimebackSourcedIdReference(sourcedId="line-item-1"),
    student=TimebackSourcedIdReference(sourcedId="student-2"),
    scoreStatus=TimebackScoreStatus.SUBMITTED,
    scoreDate="2024-01-16T10:00:00Z",
    score=88.0,
    textScore="B+",
    comment="Good work",
    class_=TimebackSourcedIdReference(sourcedId=class_sourced_id),
)

# Create the request
request = TimebackPostResultsForAcademicSessionForClassRequest(
    class_sourced_id=class_sourced_id,
    academic_session_sourced_id=academic_session_sourced_id,
    results=[result1, result2]
)

# Call the API
resp = client.oneroster.gradebook.post_results_for_academic_session_for_class(request)
print(f"Supplied SourcedId: {resp.sourcedIdPairs.suppliedSourcedId}")
print(f"Allocated SourcedId: {resp.sourcedIdPairs.allocatedSourcedId}")
```

Notes:

- This endpoint allows you to create multiple results for a specific academic session and class in one request.
- The `class` field in each result should match the `class_sourced_id` path parameter.
- `sourcedId` is optional for each result and will be auto-generated as a UUID if omitted.
- `status` defaults to `TimebackStatus.ACTIVE` if not specified.
- The `lineItem` and `student` fields only require the `sourcedId` of the referenced entity.
- The `class` and `scoreScale` fields are optional and nullable.
- `scoreDate` must be in ISO 8601 format (e.g., "2024-01-15T10:00:00Z").
- If the class or academic session does not exist, the API will return a 404 error with message 'Class or academic session not found.'
- Timeback returns `sourcedIdPairs` mapping your supplied ID to the allocated ID.

