## OneRoster — Rostering - Create School

### POST /ims/oneroster/rostering/v1p2/schools

- Method: POST
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Create a new School (organization). The responding system must return the set of sourcedIds that have been allocated to the newly created school record.

Path params:

- None

Request body (application/json):

- `{ "org": { ... } }` with required fields:
  - `name` (string) — Name of the school
  - `type` (string) — Must be `"school"` (enforced by model)
  
- Optional fields:
  - `sourcedId` (string) — Optional; if omitted, this package auto-generates a UUID
  - `status` (string, enum: `"active"`, `"tobedeleted"`) — Defaults to `"active"`
  - `metadata` (object) — Custom metadata
  - `identifier` (string) — External identifier for the school
  - `parent` (object) — Reference to parent organization:
    - `sourcedId` (string) — The sourcedId of the parent organization

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
    TimebackCreateSchoolRequest,
    TimebackCreateSchoolBody,
)
from timeback.models.timeback_sourced_id_ref import TimebackSourcedIdReference
from timeback.enums import TimebackOrgType, TimebackStatus

client = Timeback()

# Basic school creation
body = TimebackCreateSchoolBody(
    sourcedId="school-001",  # Optional; auto-generated if omitted
    name="Lincoln Elementary School",
    type=TimebackOrgType.SCHOOL,
)
req = TimebackCreateSchoolRequest(org=body)
resp = client.oneroster.rostering.create_school(req)
print(resp.sourcedIdPairs.suppliedSourcedId, '->', resp.sourcedIdPairs.allocatedSourcedId)

# School creation with parent organization
parent = TimebackSourcedIdReference(sourcedId="district-123")
body_with_parent = TimebackCreateSchoolBody(
    name="Washington Middle School",
    type=TimebackOrgType.SCHOOL,
    status=TimebackStatus.ACTIVE,
    identifier="MS001",
    parent=parent,
)
req_with_parent = TimebackCreateSchoolRequest(org=body_with_parent)
resp_with_parent = client.oneroster.rostering.create_school(req_with_parent)
print(f"Created: {resp_with_parent.sourcedIdPairs.allocatedSourcedId}")
```

Notes:

- `sourcedId` is optional and will be auto-generated as a UUID if omitted.
- `type` must be `TimebackOrgType.SCHOOL` ("school") - this is enforced by the model.
- `status` defaults to `TimebackStatus.ACTIVE` if not specified.
- The `parent` field is optional and only requires the `sourcedId` of the parent organization.
- Timeback returns `sourcedIdPairs` mapping your supplied ID to the allocated ID.

