## OneRoster — Gradebook - Get Categories for Class

### GET /ims/oneroster/gradebook/v1p2/classes/{sourcedId}/categories

- Method: GET
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Get the set of categories on the service provider for a specific class. If the corresponding record cannot be located, the api will return a 404 error code and message 'Class not found.'

Path params:

- `sourcedId` (string, required): The sourcedId of the class

Query Parameters:

All query parameters are optional and can be passed via `TimebackQueryParams`:

- `fields` (string, optional): Comma-separated list of fields to include in the response (e.g., "sourcedId,title")
- `limit` (integer, optional): Maximum number of items per page (default: 100, maximum: 3000)
- `offset` (integer, optional): Number of items to skip for pagination (default: 0)
- `sort` (string, optional): Field to sort the response by
- `orderBy` (string, optional): Sort order - "asc" or "desc"
- `filter` (string, optional): Filter expression following OneRoster specification (e.g., "status='active'")
- `search` (string, optional): **PROPRIETARY EXTENSION** - Free-text search across multiple fields

Request model:

- `TimebackGetCategoriesForClassRequest` with required fields:
  - `class_sourced_id` (string): The sourcedId of the class (path parameter)
  - `query_params` (TimebackQueryParams, optional): Query parameters for filtering, pagination, sorting, etc.

Successful response (HTTP 200):

- Body: `TimebackGetAllCategoriesResponse` with fields:
  - `categories` (List[TimebackCategory]): List of categories. See TimebackCategory for structure.
  - `total_count` (int): Total number of categories
  - `page_count` (int): Total number of pages
  - `page_number` (int): Current page number
  - `offset` (int): Offset for pagination
  - `limit` (int): Limit per page

Each `TimebackCategory` contains:
- `sourcedId` (str, optional): Unique identifier for the category
- `status` (TimebackStatus): Status - "active" or "tobedeleted" (required)
- `dateLastModified` (str, optional): Last modification timestamp in ISO 8601 format
- `metadata` (dict, optional): Additional metadata for the category
- `title` (str): Title/name of the category (required)
- `weight` (float, optional): Weight of the category for grade calculation

Error responses:

- 400: Bad Request → raises `RequestError`
- 401: Unauthorized → raises `AuthError`
- 403: Forbidden → raises `RequestError`
- 404: Class not found → raises `NotFoundError`
- 422: Unprocessable Entity / Validation Error → raises `RequestError`
- 429: Too Many Requests → raises `RateLimitError`
- 5xx: Server errors → raises `ServerError`

Python usage:

```python
from timeback import Timeback
from timeback.models.request import (
    TimebackGetCategoriesForClassRequest,
    TimebackQueryParams,
)

client = Timeback()
class_sourced_id = "class-123"

# Example 1: Get categories for a class with default parameters
request = TimebackGetCategoriesForClassRequest(
    class_sourced_id=class_sourced_id
)
resp = client.oneroster.gradebook.get_categories_for_class(request)

print(f"Total Categories: {resp.total_count}")
print(f"Page {resp.page_number} of {resp.page_count}")

for category in resp.categories:
    print(f"- Category {category.sourcedId}")
    print(f"  Title: {category.title}")
    print(f"  Status: {category.status}")
    if category.weight is not None:
        print(f"  Weight: {category.weight}")
    if category.dateLastModified:
        print(f"  Last Modified: {category.dateLastModified}")

# Example 2: Get categories with query parameters
query_params = TimebackQueryParams(
    limit=50,
    offset=0,
    fields="sourcedId,title,weight",
    filter="status='active'",
    sort="title",
    orderBy="asc"
)
request_filtered = TimebackGetCategoriesForClassRequest(
    class_sourced_id=class_sourced_id,
    query_params=query_params
)
resp_filtered = client.oneroster.gradebook.get_categories_for_class(request_filtered)

print(f"Filtered Categories: {len(resp_filtered.categories)} categories")
```

Notes:

- Categories are used to organize and group line items (assignments, assessments, etc.) in a class.
- Each category can have a weight that contributes to the overall grade calculation.
- The response is paginated - use `limit` and `offset` for pagination.
- The `search` parameter is a proprietary extension beyond the standard OneRoster specification.
- The maximum limit is 3000 items per page to prevent abuse and ensure optimal performance.
- Use the `fields` parameter to reduce response size by requesting only needed fields.
- The `filter` parameter follows the OneRoster filtering specification for complex queries.
- Required fields (`status`, `title`) must be present in all categories.
- If the class does not exist, the API will return a 404 error with message 'Class not found.'

