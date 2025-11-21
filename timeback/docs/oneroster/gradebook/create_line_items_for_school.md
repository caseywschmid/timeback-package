## OneRoster — Gradebook - Create Line Items for School

### POST /ims/oneroster/gradebook/v1p2/schools/{sourcedId}/lineItems

- Method: POST
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: To create a set of lineItems for a specific school. The responding system must return the set of sourcedIds that have been allocated to the newly created lineItem records. If the corresponding record cannot be located, the api will return a 404 error code and message 'School not found.'

Path params:

- `sourcedId` (string, required): The sourcedId of the school

Request model:

- `TimebackCreateLineItemsForSchoolRequest` with required fields:
  - `school_sourced_id` (string): The sourcedId of the school (path parameter)
  - `lineItems` (List[TimebackCreateLineItemBody]): Array of line item data to create. See TimebackCreateLineItemBody for structure.

Request body (application/json):

The request body contains a `lineItems` array. Each line item object in the array must include the following required fields:

- `title` (string) — Title of the line item
- `assignDate` (string) — Assignment date (ISO 8601 format)
- `dueDate` (string) — Due date (ISO 8601 format)
- `class` (object) — Reference to class:
  - `sourcedId` (string) — The sourcedId of the class
- `school` (object) — Reference to school:
  - `sourcedId` (string) — The sourcedId of the school (should match path parameter)
- `category` (object) — Reference to category:
  - `sourcedId` (string) — The sourcedId of the category

Optional fields for each line item:
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

- 400: Bad Request → raises `RequestError`
- 401: Unauthorized → raises `AuthError`
- 403: Forbidden → raises `RequestError`
- 404: School not found → raises `NotFoundError`
- 422: Unprocessable Entity / Validation Error → raises `RequestError`
- 429: Too Many Requests → raises `RateLimitError`
- 5xx: Server errors → raises `ServerError`

Python usage:

```python
from timeback import Timeback
from timeback.models.request import (
    TimebackCreateLineItemsForSchoolRequest,
    TimebackCreateLineItemBody,
)
from timeback.models.timeback_sourced_id_ref import TimebackSourcedIdReference
from timeback.enums import TimebackStatus

client = Timeback()
school_sourced_id = "school-123"

# Create line item bodies
line_item1 = TimebackCreateLineItemBody(
    sourcedId="line-item-1",
    title="Math Quiz 1",
    assignDate="2024-01-15T00:00:00Z",
    dueDate="2024-01-20T23:59:59Z",
    class_=TimebackSourcedIdReference(sourcedId="class-1"),
    school=TimebackSourcedIdReference(sourcedId=school_sourced_id),
    category=TimebackSourcedIdReference(sourcedId="category-1"),
    status=TimebackStatus.ACTIVE,
    description="First quiz of the semester",
    scoreScale=TimebackSourcedIdReference(sourcedId="scale-1"),
    resultValueMin=0.0,
    resultValueMax=100.0,
)

line_item2 = TimebackCreateLineItemBody(
    sourcedId="line-item-2",
    title="Math Quiz 2",
    assignDate="2024-01-22T00:00:00Z",
    dueDate="2024-01-27T23:59:59Z",
    class_=TimebackSourcedIdReference(sourcedId="class-1"),
    school=TimebackSourcedIdReference(sourcedId=school_sourced_id),
    category=TimebackSourcedIdReference(sourcedId="category-1"),
    status=TimebackStatus.ACTIVE,
    description="Second quiz of the semester",
    scoreScale=TimebackSourcedIdReference(sourcedId="scale-1"),
    resultValueMin=0.0,
    resultValueMax=100.0,
)

# Create the request
request = TimebackCreateLineItemsForSchoolRequest(
    school_sourced_id=school_sourced_id,
    lineItems=[line_item1, line_item2]
)

# Call the API
resp = client.oneroster.gradebook.create_line_items_for_school(request)
print(f"Supplied SourcedId: {resp.sourcedIdPairs.suppliedSourcedId}")
print(f"Allocated SourcedId: {resp.sourcedIdPairs.allocatedSourcedId}")
```

Notes:

- This endpoint allows you to create multiple line items for a single school in one request.
- The `school.sourcedId` in each line item should match the `school_sourced_id` path parameter.
- `sourcedId` is optional for each line item and will be auto-generated as a UUID if omitted.
- `status` defaults to `TimebackStatus.ACTIVE` if not specified.
- The `class`, `school`, and `category` fields only require the `sourcedId` of the referenced entity.
- The `scoreScale`, `gradingPeriod`, and `academicSession` fields are optional and nullable.
- `assignDate` and `dueDate` must be in ISO 8601 format (e.g., "2024-01-15T00:00:00Z").
- If the school does not exist, the API will return a 404 error with message 'School not found.'
- Timeback returns `sourcedIdPairs` mapping your supplied ID to the allocated ID.

