## OneRoster — Gradebook - Create Line Item

### POST /ims/oneroster/gradebook/v1p2/lineItems

- Method: POST
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: To create a new Line Item. The responding system must return the set of sourcedIds that have been allocated to the newly created Line Item records.

Path params:

- None

Request body (application/json):

- `{ "lineItem": { ... } }` with required fields:
  - `title` (string) — Title of the line item
  - `assignDate` (string) — Assignment date (ISO 8601 format)
  - `dueDate` (string) — Due date (ISO 8601 format)
  - `class` (object) — Reference to class:
    - `sourcedId` (string) — The sourcedId of the class
  - `school` (object) — Reference to school:
    - `sourcedId` (string) — The sourcedId of the school
  - `category` (object) — Reference to category:
    - `sourcedId` (string) — The sourcedId of the category
  
- Optional fields:
  - `sourcedId` (string) — Optional; if omitted, this package auto-generates a UUID
  - `status` (string, enum: `"active"`, `"tobedeleted"`) — Defaults to `"active"`
  - `description` (string, nullable) — Description of the line item
  - `metadata` (object) — Custom metadata
  - `scoreScale` (object, nullable) — Reference to score scale:
    - `sourcedId` (string) — The sourcedId of the score scale
  - `resultValueMin` (number, nullable) — Minimum score value
  - `resultValueMax` (number, nullable) — Maximum score value
  - `learningObjectiveSet` (array, nullable) — Learning objective results
  - `gradingPeriod` (object, nullable) — Reference to grading period:
    - `sourcedId` (string) — The sourcedId of the grading period
  - `academicSession` (object, nullable) — Reference to academic session:
    - `sourcedId` (string) — The sourcedId of the academic session

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
    TimebackCreateLineItemRequest,
    TimebackCreateLineItemBody,
)
from timeback.models.timeback_sourced_id_ref import TimebackSourcedIdReference
from timeback.enums import TimebackStatus

client = Timeback()

# Basic line item creation
body = TimebackCreateLineItemBody(
    sourcedId="line-item-001",  # Optional; auto-generated if omitted
    title="Math Quiz 1",
    assignDate="2024-01-15T00:00:00Z",
    dueDate="2024-01-20T23:59:59Z",
    class_=TimebackSourcedIdReference(sourcedId="class-1"),
    school=TimebackSourcedIdReference(sourcedId="school-1"),
    category=TimebackSourcedIdReference(sourcedId="category-1"),
    description="First quiz of the semester",
    resultValueMin=0.0,
    resultValueMax=100.0,
)
req = TimebackCreateLineItemRequest(lineItem=body)
resp = client.oneroster.gradebook.create_line_item(req)
print(resp.sourcedIdPairs.suppliedSourcedId, '->', resp.sourcedIdPairs.allocatedSourcedId)

# Line item creation with all fields
body_with_all_fields = TimebackCreateLineItemBody(
    sourcedId="line-item-002",
    title="Math Quiz 2",
    assignDate="2024-01-22T00:00:00Z",
    dueDate="2024-01-27T23:59:59Z",
    class_=TimebackSourcedIdReference(sourcedId="class-1"),
    school=TimebackSourcedIdReference(sourcedId="school-1"),
    category=TimebackSourcedIdReference(sourcedId="category-1"),
    status=TimebackStatus.ACTIVE,
    description="Second quiz of the semester",
    scoreScale=TimebackSourcedIdReference(sourcedId="scale-1"),
    resultValueMin=0.0,
    resultValueMax=100.0,
    metadata={"semester": "Spring 2024"},
)
req_with_all_fields = TimebackCreateLineItemRequest(lineItem=body_with_all_fields)
resp_with_all_fields = client.oneroster.gradebook.create_line_item(req_with_all_fields)
print(f"Created: {resp_with_all_fields.sourcedIdPairs.allocatedSourcedId}")
```

Notes:

- `sourcedId` is optional and will be auto-generated as a UUID if omitted.
- `status` defaults to `TimebackStatus.ACTIVE` if not specified.
- The `class`, `school`, and `category` fields only require the `sourcedId` of the referenced entity.
- The `scoreScale`, `gradingPeriod`, and `academicSession` fields are optional and nullable.
- `assignDate` and `dueDate` must be in ISO 8601 format (e.g., "2024-01-15T00:00:00Z").
- Timeback returns `sourcedIdPairs` mapping your supplied ID to the allocated ID.

