## OneRoster — Gradebook - Create Category

### POST /ims/oneroster/gradebook/v1p2/categories

- Method: POST
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Create a new line item category. A 'title' is required when creating a category.

Request body:

- Body: `{ "category": Category }`
- The `Category` object includes:
  - required: `status`, `title`
  - optional: `sourcedId` (auto-generated if not provided), `dateLastModified`, `metadata`, `weight`

Successful response (HTTP 201):

- Body: `{ "sourcedIdPairs": { "suppliedSourcedId": "...", "allocatedSourcedId": "..." } }`
- The `sourcedIdPairs` contains the mapping from supplied to allocated sourcedId

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
from timeback.models.request import TimebackCreateCategoryRequest
from timeback.models.timeback_category import TimebackCategory
from timeback.enums import TimebackStatus

client = Timeback()

# Create a category with all fields
category = TimebackCategory(
    sourcedId="my-category-id",  # Optional
    status=TimebackStatus.ACTIVE,
    title="Homework",
    weight=0.3,  # Weight for grade calculation
    metadata={"description": "Daily homework assignments"},
)

request = TimebackCreateCategoryRequest(category=category)
response = client.oneroster.gradebook.create_category(request)

print(f"Supplied: {response.sourcedIdPairs.suppliedSourcedId}")
print(f"Allocated: {response.sourcedIdPairs.allocatedSourcedId}")

# Create a minimal category (only required fields)
minimal_category = TimebackCategory(
    status=TimebackStatus.ACTIVE,
    title="Exams",
)
minimal_request = TimebackCreateCategoryRequest(category=minimal_category)
minimal_response = client.oneroster.gradebook.create_category(minimal_request)
```

Notes:

- Categories are used to organize line items (e.g., "Homework", "Exams", "Quizzes").
- The `weight` field is optional and used for weighted grade calculations.
- The `sourcedId` is optional; if not provided, the server will generate one.
- The response contains both the supplied and allocated sourcedId for reference.
- The `title` field is required for category creation.

