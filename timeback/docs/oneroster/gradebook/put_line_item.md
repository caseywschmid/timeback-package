## OneRoster — Gradebook - Put Line Item

### PUT /ims/oneroster/gradebook/v1p2/lineItems/{sourcedId}

- Method: PUT
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: To update an existing Line Item or create a new one if it doesn't exist. The sourcedId for the record is supplied by the requesting system.

Path params:

- `sourcedId` (string, required): The sourcedId of the line item to update/create

Request model:

- `TimebackPutLineItemRequest` with required fields:
  - `sourced_id` (string): The sourcedId of the line item (path parameter)
  - `lineItem` (TimebackPutLineItemBody): Line item data to update/create. See TimebackPutLineItemBody for structure.

Request body (application/json):

The request body contains a `lineItem` object. The `sourcedId` in the body should match the path parameter.

Required fields:
- `title` (string) — Title of the line item
- `assignDate` (string) — Assignment date (ISO 8601 format)
- `dueDate` (string) — Due date (ISO 8601 format)
- `class` (object) — Reference to class:
  - `sourcedId` (string) — The sourcedId of the class
- `school` (object) — Reference to school:
  - `sourcedId` (string) — The sourcedId of the school
- `category` (object) — Reference to category:
  - `sourcedId` (string) — The sourcedId of the category

Optional fields:
- `sourcedId` (string) — Should match path parameter if provided
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

- Body: `TimebackPutLineItemResponse` with fields:
  - `line_item` (LineItem): The updated/created line item. See LineItem for structure.

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
    TimebackPutLineItemRequest,
    TimebackPutLineItemBody,
)
from timeback.models.timeback_sourced_id_ref import TimebackSourcedIdReference
from timeback.enums import TimebackStatus

client = Timeback()
sourced_id = "line-item-123-456"

# Create the line item body
line_item_body = TimebackPutLineItemBody(
    sourcedId=sourced_id,
    title="Updated Math Quiz 1",
    assignDate="2024-01-15T00:00:00Z",
    dueDate="2024-01-20T23:59:59Z",
    class_=TimebackSourcedIdReference(sourcedId="class-1"),
    school=TimebackSourcedIdReference(sourcedId="school-1"),
    category=TimebackSourcedIdReference(sourcedId="category-1"),
    status=TimebackStatus.ACTIVE,
    description="Updated quiz description",
    scoreScale=TimebackSourcedIdReference(sourcedId="scale-1"),
    resultValueMin=0.0,
    resultValueMax=100.0,
)

# Create the request
request = TimebackPutLineItemRequest(
    sourced_id=sourced_id, 
    lineItem=line_item_body
)

# Call the API
resp = client.oneroster.gradebook.put_line_item(request)

print(f"Updated/Created Line Item: {resp.line_item.sourcedId}")
print(f"Title: {resp.line_item.title}")
print(f"Status: {resp.line_item.status}")
```

Notes:

- This endpoint is idempotent: calling it multiple times with the same data produces the same result.
- The `sourcedId` in the path should match the `sourcedId` in the body (if provided).
- If the line item does not exist, it will be created with the provided `sourcedId`.
- If it exists, it will be updated.
- The `class`, `school`, and `category` fields only require the `sourcedId` of the referenced entity.
- The `scoreScale`, `gradingPeriod`, and `academicSession` fields are optional and nullable.
- `assignDate` and `dueDate` must be in ISO 8601 format (e.g., "2024-01-15T00:00:00Z").

