## OneRoster — Rostering - Update School

### PUT /ims/oneroster/rostering/v1p2/schools/{sourcedId}

- Method: PUT
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Update an existing school identified by `sourcedId`.

Request model:

- `TimebackUpdateSchoolRequest` with required fields:
  - `org` (TimebackUpdateSchoolBody) — School data with required fields:
    - `sourcedId` (string) — The sourcedId of the school to update (used in path and body)
    - `name` (string) — Name of the school
    - `type` (TimebackOrgType) — Must be `TimebackOrgType.SCHOOL` ("school")
    - Optional fields: `status`, `metadata`, `identifier`, `parent`

Path params (extracted from request):

- `sourcedId` (string, required): Extracted from `request.org.sourcedId` for the path

Request body (application/json, extracted from request):

- `{ "org": { ... } }` with required fields as listed above

Successful response (HTTP 200):

- Body: `{ "org": TimebackOrg }`
- Client return type: `TimebackUpdateSchoolResponse`

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
from timeback.models.request import TimebackUpdateSchoolRequest, TimebackUpdateSchoolBody
from timeback.models.timeback_sourced_id_ref import TimebackSourcedIdReference
from timeback.enums import TimebackOrgType, TimebackStatus

client = Timeback()
body = TimebackUpdateSchoolBody(
    sourcedId="school-001",
    name="Updated School Name",
    type=TimebackOrgType.SCHOOL,
    status=TimebackStatus.ACTIVE,
)
req = TimebackUpdateSchoolRequest(org=body)
resp = client.oneroster.rostering.update_school(req)
print(resp.org.sourcedId, resp.org.name)

# Update with parent organization
parent = TimebackSourcedIdReference(sourcedId="district-123")
body_with_parent = TimebackUpdateSchoolBody(
    sourcedId="school-001",
    name="School with Parent",
    type=TimebackOrgType.SCHOOL,
    parent=parent,
)
req_with_parent = TimebackUpdateSchoolRequest(org=body_with_parent)
resp_with_parent = client.oneroster.rostering.update_school(req_with_parent)
print(f"Updated: {resp_with_parent.org.sourcedId}")
```

Notes:

- `type` must be `TimebackOrgType.SCHOOL` ("school") - this is enforced by the model validator.
- `status` defaults to `TimebackStatus.ACTIVE` if not specified, but can be set to `TimebackStatus.TOBEDELETED`.
- The `parent` field uses `TimebackSourcedIdReference` which only requires the `sourcedId` of the parent organization.

