## OneRoster — Gradebook - Put Category

### PUT /ims/oneroster/gradebook/v1p2/categories/{sourcedId}

- Method: PUT
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Create or update a category by `sourcedId`.

Path params:

- `sourcedId` (string, required): The category's sourcedId

Request body:

- `category` (Category, required): The category object to create/update
  - Required fields: `status`, `title`
  - Optional fields: `sourcedId`, `dateLastModified`, `metadata`, `weight`

Successful response (HTTP 201):

- Body: `{ "category": Category }`
- The `Category` object includes:
  - required: `sourcedId`, `status`, `title`
  - optional: `dateLastModified`, `metadata`, `weight`

Error responses:

- 400/422: Request/validation → raises `RequestError`
- 401: Unauthorized → raises `AuthError`
- 403: Forbidden → raises `RequestError`
- 404: Not found → raises `NotFoundError`
- 429: Too Many Requests → raises `RateLimitError`
- 5xx: Server errors → raises `ServerError`

Python usage:

```python
from timeback import Timeback
from timeback.models.request import TimebackPutCategoryRequest
from timeback.models.timeback_category import TimebackCategory
from timeback.enums import TimebackStatus

client = Timeback()

# Create or update a category
category = TimebackCategory(
    sourcedId="<sourcedId>",
    status=TimebackStatus.ACTIVE,
    title="Homework",
    weight=0.30,
)

request = TimebackPutCategoryRequest(
    sourced_id="<sourcedId>",
    category=category
)
response = client.oneroster.gradebook.put_category(request)

print(f"Category: {response.category.title}")
print(f"Weight: {response.category.weight}")
```

Notes:

- This endpoint uses upsert semantics: it creates a new category if one doesn't exist with the given `sourcedId`, or updates the existing category if it does.
- The `sourcedId` in the path and in the category object should match.
- The `weight` field is optional and used for weighted grade calculations.

