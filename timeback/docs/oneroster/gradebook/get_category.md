## OneRoster — Gradebook - Get Category

### GET /ims/oneroster/gradebook/v1p2/categories/{sourcedId}

- Method: GET
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Fetch a specific category by `sourcedId`.

Path params:

- `sourcedId` (string, required): The category's sourcedId

Query params:

- `fields` (string, optional): Comma-separated list of fields to include

Successful response (HTTP 200):

- Body: `{ "category": Category }`
- The `Category` object includes:
  - required: `sourcedId`, `status`, `title`
  - optional: `dateLastModified`, `metadata`, `weight`

Error responses:

- 400/422: Request/validation → raises `RequestError`
- 401: Unauthorized → raises `AuthError`
- 403: Forbidden → raises `RequestError`
- 404: Category not found → raises `NotFoundError`
- 429: Too Many Requests → raises `RateLimitError`
- 5xx: Server errors → raises `ServerError`

Python usage:

```python
from timeback import Timeback
from timeback.models.request import TimebackGetCategoryRequest, TimebackQueryParams

client = Timeback()

# Basic request
request = TimebackGetCategoryRequest(sourced_id="<sourcedId>")
response = client.oneroster.gradebook.get_category(request)

print(f"Category: {response.category.title}")
print(f"Weight: {response.category.weight}")

# With fields filter
query_params = TimebackQueryParams(fields=["sourcedId", "title", "weight"])
request_with_fields = TimebackGetCategoryRequest(
    sourced_id="<sourcedId>",
    query_params=query_params
)
response_min = client.oneroster.gradebook.get_category(request_with_fields)
```

Notes:

- The response contains a single category object.
- The `fields` query parameter allows you to request only specific fields, reducing response size.
- If the category does not exist, a `NotFoundError` is raised.
- The `weight` field is optional and used for weighted grade calculations.

