## OneRoster — Rostering - Get School

### GET /ims/oneroster/rostering/v1p2/schools/{sourcedId}

- Method: GET
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Fetch a specific OneRoster school (organization) by `sourcedId`.
- Query params:
- `fields` (string, optional): Comma-separated field list (e.g., `sourcedId,name`)

Path params:

- `sourcedId` (string, required): The school's sourcedId

Successful response (HTTP 200):

- Body: `{ "org": Org }`
- The `Org` object includes (non-exhaustive):
  - required: `sourcedId`, `name`, `type`
  - optional: `status`, `dateLastModified`, `metadata`, `identifier`, `parent`, `children`

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
from timeback.models.request import TimebackGetSchoolRequest, TimebackQueryParams

client = Timeback()

# Basic request without query params
request = TimebackGetSchoolRequest(sourced_id="<sourcedId>")
response = client.oneroster.rostering.get_school(request)

# With fields filter
query_params = TimebackQueryParams(fields=["sourcedId", "name"])
request_with_fields = TimebackGetSchoolRequest(
    sourced_id="<sourcedId>", 
    query_params=query_params
)
response_min = client.oneroster.rostering.get_school(request_with_fields)

print(response.org.sourcedId, response.org.name, response.org.type)
```

Notes:

- The client returns the full API response as `TimebackGetSchoolResponse` which contains an `org` field.
- The response model mirrors the API structure: `{ "org": Org }`.
- If the API omits required fields, validation will fail with a `ParseError`.
- The `fields` query parameter allows you to request only specific fields, reducing response size.

