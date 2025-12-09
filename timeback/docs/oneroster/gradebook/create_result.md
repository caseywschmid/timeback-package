## OneRoster — Gradebook - Create Result

### POST /ims/oneroster/gradebook/v1p2/results

- Method: POST
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Create a new Result. The request body must include a `result` object with the following required fields: `lineItem` (with sourcedId), `student` (with sourcedId), `scoreStatus`, and `scoreDate`. The responding system must return the set of sourcedIds that have been allocated to the newly created result records.

Path params:

- None

Request body (application/json):

- `{ "result": { ... } }` with required fields:
  - `lineItem` (object) — Reference to the line item:
    - `sourcedId` (string) — The sourcedId of the line item
  - `student` (object) — Reference to the student:
    - `sourcedId` (string) — The sourcedId of the student
  - `scoreStatus` (string, enum) — Status of the score: `"exempt"`, `"fully graded"`, `"not submitted"`, `"partially graded"`, or `"submitted"`
  - `scoreDate` (string) — Date when the score was recorded (ISO 8601 format)
  
- Optional fields:
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

- 400/422: Request/validation → raises `RequestError`
- 401: Unauthorized → raises `AuthError`
- 403: Forbidden → raises `RequestError`
- 404: Not Found → raises `NotFoundError`
- 429: Too Many Requests → raises `RateLimitError`
- 5xx: Server errors → raises `ServerError`

Python usage:

```python
from timeback import Timeback
from timeback.models.request import (
    TimebackCreateResultRequest,
    TimebackCreateResultBody,
)
from timeback.models.timeback_sourced_id_ref import TimebackSourcedIdReference
from timeback.enums import TimebackStatus, TimebackScoreStatus

client = Timeback()

# Basic result creation
body = TimebackCreateResultBody(
    sourcedId="result-001",  # Optional; auto-generated if omitted
    lineItem=TimebackSourcedIdReference(sourcedId="line-item-1"),
    student=TimebackSourcedIdReference(sourcedId="student-1"),
    scoreStatus=TimebackScoreStatus.FULLY_GRADED,
    scoreDate="2024-01-15T10:00:00Z",
    score=95.5,
)
req = TimebackCreateResultRequest(result=body)
resp = client.oneroster.gradebook.create_result(req)
print(resp.sourcedIdPairs.suppliedSourcedId, '->', resp.sourcedIdPairs.allocatedSourcedId)

# Result creation with all fields
body_with_all_fields = TimebackCreateResultBody(
    sourcedId="result-002",
    lineItem=TimebackSourcedIdReference(sourcedId="line-item-1"),
    student=TimebackSourcedIdReference(sourcedId="student-1"),
    scoreStatus=TimebackScoreStatus.FULLY_GRADED,
    scoreDate="2024-01-15T10:00:00Z",
    status=TimebackStatus.ACTIVE,
    score=95.5,
    textScore="A",
    comment="Excellent work",
    class_=TimebackSourcedIdReference(sourcedId="class-1"),
    scoreScale=TimebackSourcedIdReference(sourcedId="scale-1"),
)
req_with_all_fields = TimebackCreateResultRequest(result=body_with_all_fields)
resp_with_all_fields = client.oneroster.gradebook.create_result(req_with_all_fields)
print(f"Created: {resp_with_all_fields.sourcedIdPairs.allocatedSourcedId}")
```

Notes:

- `sourcedId` is optional and will be auto-generated as a UUID if omitted.
- `status` defaults to `TimebackStatus.ACTIVE` if not specified.
- The `lineItem` and `student` fields only require the `sourcedId` of the referenced entity.
- The `class` and `scoreScale` fields are optional and nullable.
- `scoreDate` must be in ISO 8601 format (e.g., "2024-01-15T10:00:00Z").
- Timeback returns `sourcedIdPairs` mapping your supplied ID to the allocated ID.

