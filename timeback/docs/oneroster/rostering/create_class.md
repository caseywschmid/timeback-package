## OneRoster — Rostering - Create Class

### POST /ims/oneroster/rostering/v1p2/classes

- Method: POST
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Create a new Class. The responding system must return the set of sourcedIds that have been allocated to the newly created class record.

Path params:

- None

Request body (application/json):

- `{ "class": { ... } }` with required fields:
  - `title` (string) — Title/name of the class
  - `course` (object) — Reference to the parent course:
    - `sourcedId` (string) — The sourcedId of the course
  - `org` (object) — Reference to the organization/school:
    - `sourcedId` (string) — The sourcedId of the organization/school
  - `terms` (array) — References to academic terms/sessions:
    - Each term object contains:
      - `sourcedId` (string) — The sourcedId of the term
  
- Optional fields:
  - `sourcedId` (string) — Optional; if omitted, this package auto-generates a UUID
  - `status` (string, enum: `"active"`, `"tobedeleted"`) — Defaults to `"active"`
  - `metadata` (object) — Custom metadata
  - `classCode` (string) — Class code identifier
  - `classType` (string, enum: `"homeroom"`, `"scheduled"`) — Type of class
  - `location` (string) — Physical location of the class
  - `grades` (array of strings) — List of grade levels (e.g., `["9", "10", "11", "12"]`)
  - `subjects` (array of strings) — List of subjects (e.g., `["Math", "Science"]`)
  - `subjectCodes` (array of strings) — List of subject codes
  - `periods` (array of strings) — List of class periods
  - `resources` (array of objects) — References to learning resources:
    - Each resource object contains:
      - `sourcedId` (string) — The sourcedId of the resource

Request model:

- `TimebackCreateClassRequest` with required fields:
  - `class_` (TimebackCreateClassBody): Class data to create. See TimebackCreateClassBody for structure.

Successful response (HTTP 201):

- Body: `TimebackCreateClassResponse` with fields:
  - `sourcedIdPairs` (TimebackSourcedIdPairs): SourcedId mapping containing:
    - `suppliedSourcedId` (string): The sourcedId you provided (or auto-generated UUID)
    - `allocatedSourcedId` (string): The sourcedId allocated by the system

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
    TimebackCreateClassRequest,
    TimebackCreateClassBody,
)
from timeback.models.timeback_sourced_id_ref import TimebackSourcedIdReference
from timeback.enums import TimebackStatus, TimebackClassType

client = Timeback()

# Example 1: Create a class with minimal required fields
course_ref = TimebackSourcedIdReference(sourcedId="course-123")
org_ref = TimebackSourcedIdReference(sourcedId="org-123")
term_ref = TimebackSourcedIdReference(sourcedId="term-123")

body = TimebackCreateClassBody(
    title="Math 101",
    course=course_ref,
    org=org_ref,
    terms=[term_ref],
)
request = TimebackCreateClassRequest(class_=body)
response = client.oneroster.rostering.create_class(request)

print(f"Created class:")
print(f"  Supplied SourcedId: {response.sourcedIdPairs.suppliedSourcedId}")
print(f"  Allocated SourcedId: {response.sourcedIdPairs.allocatedSourcedId}")

# Example 2: Create a class with all optional fields
course_ref2 = TimebackSourcedIdReference(sourcedId="course-456")
org_ref2 = TimebackSourcedIdReference(sourcedId="org-456")
term_ref2 = TimebackSourcedIdReference(sourcedId="term-456")
resource_ref = TimebackSourcedIdReference(sourcedId="resource-123")

body_full = TimebackCreateClassBody(
    sourcedId="my-custom-class-id",  # Optional; auto-generated if omitted
    title="Advanced Mathematics",
    course=course_ref2,
    org=org_ref2,
    terms=[term_ref2],
    classCode="MATH-301",
    classType=TimebackClassType.SCHEDULED,
    location="Building A, Room 301",
    status=TimebackStatus.ACTIVE,
    grades=["11", "12"],
    subjects=["Math"],
    subjectCodes=["MATH"],
    periods=["Period 1"],
    resources=[resource_ref],
    metadata={"custom": "value"},
)
request_full = TimebackCreateClassRequest(class_=body_full)
response_full = client.oneroster.rostering.create_class(request_full)

print(f"\nCreated class with all fields:")
print(f"  Supplied SourcedId: {response_full.sourcedIdPairs.suppliedSourcedId}")
print(f"  Allocated SourcedId: {response_full.sourcedIdPairs.allocatedSourcedId}")
```

Notes:

- `sourcedId` is optional and will be auto-generated as a UUID if omitted.
- `status` defaults to `TimebackStatus.ACTIVE` if not specified.
- Classes represent specific instances of courses, typically for a particular term/semester.
- Students enroll in classes, not courses directly.
- The `course`, `org`, `terms`, and `resources` fields only require `sourcedId` references (not full reference objects with href/type).
- Multiple terms can be provided in the `terms` array.
- Multiple resources can be provided in the `resources` array.
- Valid grade values are: `"-1"`, `"0"`, `"1"` through `"13"`.
- Valid subject values are: `"Reading"`, `"Language"`, `"Vocabulary"`, `"Social Studies"`, `"Writing"`, `"Science"`, `"FastMath"`, `"Math"`.
- Timeback returns `sourcedIdPairs` mapping your supplied ID to the allocated ID.

