## OneRoster — Gradebook - Get All Categories

### GET /ims/oneroster/gradebook/v1p2/categories

- Method: GET
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Fetch all line item categories with pagination support.

Query params:

- `fields` (string, optional): Comma-separated list of fields to include
- `limit` (integer, optional): Maximum items to return (default: 100, max: 3000)
- `offset` (integer, optional): Number of items to skip (default: 0)
- `sort` (string, optional): Field to sort by
- `orderBy` (string, optional): Sort order - "asc" or "desc"
- `filter` (string, optional): Filter expression (e.g., `status='active'`)
- `search` (string, optional): Free-text search (proprietary extension)

Successful response (HTTP 200):

- Body: `{ "categories": [...], "totalCount": N, "pageCount": N, "pageNumber": N, "offset": N, "limit": N }`
- The `categories` array contains Category objects with the following fields:
  - `sourcedId` (string): Unique identifier
  - `status` (string): "active" or "tobedeleted"
  - `dateLastModified` (string): ISO 8601 timestamp
  - `metadata` (object, optional): Additional metadata
  - `title` (string): Category title/name
  - `weight` (number, optional): Weight for grade calculation

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
from timeback.models.request import TimebackGetAllCategoriesRequest, TimebackQueryParams

client = Timeback()

# Basic request - get all categories
request = TimebackGetAllCategoriesRequest()
response = client.oneroster.gradebook.get_all_categories(request)

print(f"Total categories: {response.total_count}")
for category in response.categories:
    print(f"  - {category.sourcedId}: {category.title} (weight: {category.weight})")

# With pagination and filtering
query_params = TimebackQueryParams(
    limit=10,
    offset=0,
    filter="status='active'",
    sort="title",
    order_by="asc",
)
request_with_params = TimebackGetAllCategoriesRequest(query_params=query_params)
response_filtered = client.oneroster.gradebook.get_all_categories(request_with_params)
```

Notes:

- Categories are used to group line items (e.g., "Homework", "Exams", "Quizzes").
- The `weight` field is used for weighted grade calculations.
- The response includes pagination metadata for iterating through large result sets.
- The `search` parameter is a proprietary extension for free-text searching.

