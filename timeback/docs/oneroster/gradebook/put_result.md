## OneRoster — Gradebook - Put Result

### PUT /ims/oneroster/gradebook/v1p2/results/{sourcedId}

- Method: PUT
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: To update an existing result or create a new one if it doesn't exist. The sourcedId for the record is supplied by the requesting system.

Path params:

- `sourcedId` (string, required): The sourcedId of the result to update/create

Request model:

- `TimebackPutResultRequest` with required fields:
  - `sourced_id` (string): The sourcedId of the result (path parameter)
  - `result` (TimebackPutResultBody): Result data to update/create. See TimebackPutResultBody for structure.

Request body (application/json):

The request body contains a `result` object. The `sourcedId` in the body should match the path parameter.

Required fields:
- `lineItem` (object) — Reference to the line item:
  - `sourcedId` (string) — The sourcedId of the line item
- `student` (object) — Reference to the student:
  - `sourcedId` (string) — The sourcedId of the student
- `scoreStatus` (string, enum) — Status of the score: `"exempt"`, `"fully graded"`, `"not submitted"`, `"partially graded"`, or `"submitted"`
- `scoreDate` (string) — Date when the score was recorded (ISO 8601 format)

Optional fields:
- `sourcedId` (string) — Should match path parameter if provided
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

- Body: `TimebackPutResultResponse` with fields:
  - `result` (TimebackResult): The updated/created result. See TimebackResult for structure.

Error responses:

- 400: Bad Request → raises `RequestError`
- 401: Unauthorized → raises `AuthError`
- 403: Forbidden → raises `RequestError`
- 404: Not Found → raises `NotFoundError`
- 422: Unprocessable Entity / Validation Error → raises `RequestError`
- 429: Too Many Requests → raises `RateLimitError`
- 5xx: Server errors → raises `ServerError`

Python usage:

```python
from timeback import Timeback
from timeback.models.request import (
    TimebackPutResultRequest,
    TimebackPutResultBody,
)
from timeback.models.timeback_sourced_id_ref import TimebackSourcedIdReference
from timeback.enums import TimebackStatus, TimebackScoreStatus

client = Timeback()
sourced_id = "result-123-456"

# Create the result body
result_body = TimebackPutResultBody(
    sourcedId=sourced_id,
    lineItem=TimebackSourcedIdReference(sourcedId="line-item-1"),
    student=TimebackSourcedIdReference(sourcedId="student-1"),
    scoreStatus=TimebackScoreStatus.FULLY_GRADED,
    scoreDate="2024-01-15T10:00:00Z",
    status=TimebackStatus.ACTIVE,
    score=95.5,
    textScore="A",
    comment="Excellent work - updated",
    class_=TimebackSourcedIdReference(sourcedId="class-1"),
    scoreScale=TimebackSourcedIdReference(sourcedId="scale-1"),
)

# Create the request
request = TimebackPutResultRequest(
    sourced_id=sourced_id, 
    result=result_body
)

# Call the API
resp = client.oneroster.gradebook.put_result(request)

print(f"Updated/Created Result: {resp.result.sourcedId}")
print(f"Score: {resp.result.score}")
print(f"Text Score: {resp.result.textScore}")
```

Notes:

- This endpoint is idempotent: calling it multiple times with the same data produces the same result.
- The `sourcedId` in the path should match the `sourcedId` in the body (if provided).
- If the result does not exist, it will be created with the provided `sourcedId`.
- If it exists, it will be updated.
- The `lineItem` and `student` fields only require the `sourcedId` of the referenced entity.
- The `class` and `scoreScale` fields are optional and nullable.
- `scoreDate` must be in ISO 8601 format (e.g., "2024-01-15T10:00:00Z").

