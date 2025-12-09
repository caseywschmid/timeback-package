## OneRoster — Rostering - Get Class

### GET /ims/oneroster/rostering/v1p2/classes/{sourcedId}

- Method: GET
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Fetch a specific OneRoster class by `sourcedId`.
- Query params:
- `fields` (string, optional): Comma-separated field list (e.g., `sourcedId,title`)

Path params:

- `sourcedId` (string, required): The class's sourcedId

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
from timeback.models.request import TimebackGetClassRequest, TimebackQueryParams

client = Timeback()

# Basic request without query params
request = TimebackGetClassRequest(sourced_id="<sourcedId>")
response = client.oneroster.rostering.get_class(request)

# With fields filter
query_params = TimebackQueryParams(fields=["sourcedId", "title", "classCode"])
request_with_fields = TimebackGetClassRequest(
    sourced_id="<sourcedId>", 
    query_params=query_params
)
response_min = client.oneroster.rostering.get_class(request_with_fields)

print(response.class_.sourcedId, response.class_.title)
print(response.class_.course.sourcedId)  # Associated course
print([t.sourcedId for t in response.class_.terms])  # Associated terms
```

Notes:

- The client returns the full API response as `TimebackGetClassResponse` which contains a `class_` field.
- The response model mirrors the API structure: `{ "class": Class }`. The field is named `class_` in Python to avoid the reserved keyword conflict.
- If the API omits required fields, validation will fail with a `ParseError`.
- The `fields` query parameter allows you to request only specific fields, reducing response size.
- A class represents a specific section/instance of a course for a particular term.

