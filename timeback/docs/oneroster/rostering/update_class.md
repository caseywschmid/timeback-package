## OneRoster — Rostering - Update Class

### PUT /ims/oneroster/rostering/v1p2/classes/{sourcedId}

- Method: PUT
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Update an existing OneRoster class by `sourcedId`.

Path params:

- `sourcedId` (string, required): The class's sourcedId (also included in request body)

Request body:

- Body: `{ "class": ClassUpdate }`
- The `ClassUpdate` object includes:
  - required: `sourcedId`
  - optional: `status`, `metadata`, `title`, `classCode`, `classType`, `location`, `grades`, `subjects`, `subjectCodes`, `periods`, `resources`, `terms`

Successful response (HTTP 200):

- Body: `{ "class": Class }`
- The `Class` object includes (non-exhaustive):
  - required: `sourcedId`, `title`, `course`, `org`, `terms`
  - optional: `status`, `dateLastModified`, `metadata`, `classCode`, `classType`, `location`, `grades`, `subjects`, `subjectCodes`, `periods`, `resources`

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
from timeback.models.request import TimebackUpdateClassRequest, TimebackUpdateClassBody
from timeback.models.timeback_sourced_id_ref import TimebackSourcedIdReference
from timeback.enums import TimebackStatus, TimebackClassType

client = Timeback()

# Basic update - just title and status
body = TimebackUpdateClassBody(
    sourcedId="<sourcedId>",
    title="Updated Class Title",
    status=TimebackStatus.ACTIVE,
)
request = TimebackUpdateClassRequest(class_=body)
response = client.oneroster.rostering.update_class(request)

print(response.class_.sourcedId, response.class_.title)

# Update with optional fields
body_with_options = TimebackUpdateClassBody(
    sourcedId="<sourcedId>",
    classType=TimebackClassType.SCHEDULED,
    classCode="MATH-101-A",
    location="Room 101",
    grades=["9", "10"],
    subjects=["Math"],
)
request_with_options = TimebackUpdateClassRequest(class_=body_with_options)
response_min = client.oneroster.rostering.update_class(request_with_options)

# Update with term and resource references
body_with_refs = TimebackUpdateClassBody(
    sourcedId="<sourcedId>",
    terms=[TimebackSourcedIdReference(sourcedId="term-001")],
    resources=[TimebackSourcedIdReference(sourcedId="resource-001")],
)
request_with_refs = TimebackUpdateClassRequest(class_=body_with_refs)
response_refs = client.oneroster.rostering.update_class(request_with_refs)
```

Notes:

- The client returns the full API response as `TimebackUpdateClassResponse` which contains a `class_` field.
- The response model mirrors the API structure: `{ "class": Class }`. The field is named `class_` in Python to avoid the reserved keyword conflict.
- The `sourcedId` must be included in both the URL path and the request body.
- Only fields that need to be updated should be included in the request body.
- If the API cannot find the class, a `NotFoundError` is raised.

