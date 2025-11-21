## OneRoster — Gradebook - Get All Line Items

### GET /ims/oneroster/gradebook/v1p2/lineItems

- Method: GET
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Get all of the Line Items on the service provider

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

- `TimebackGetAllLineItemsRequest` with optional fields:
  - `query_params` (TimebackQueryParams, optional): Query parameters for filtering, pagination, sorting, etc.

Successful response (HTTP 200):

- Body: `TimebackGetAllLineItemsResponse` with fields:
  - `line_items` (List[LineItem]): List of line items. See LineItem for structure.
  - `total_count` (int): Total number of line items
  - `page_count` (int): Total number of pages
  - `page_number` (int): Current page number
  - `offset` (int): Offset for pagination
  - `limit` (int): Limit per page

Each `LineItem` contains:
- `sourcedId` (str, optional): Unique identifier
- `status` (TimebackStatus): Status - "active" or "tobedeleted" (required)
- `dateLastModified` (str, optional): Last modification timestamp
- `metadata` (dict, optional): Additional metadata
- `title` (str): Title of the line item (required)
- `description` (str, optional): Description of the line item
- `assignDate` (str): Assignment date in ISO 8601 format (required)
- `dueDate` (str): Due date in ISO 8601 format (required)
- `class_` (TimebackSourcedIdReference): Reference to class (aliased as "class") (required)
- `school` (TimebackSourcedIdReference): Reference to school (required)
- `category` (TimebackSourcedIdReference): Reference to category (required)
- `scoreScale` (TimebackSourcedIdReference, optional): Reference to score scale
- `resultValueMin` (float, optional): Minimum score value
- `resultValueMax` (float, optional): Maximum score value
- `learningObjectiveSet` (List[Dict[str, Any]], optional): Learning objective results
- `gradingPeriod` (TimebackSourcedIdReference, optional): Reference to grading period (nullable)
- `academicSession` (TimebackSourcedIdReference, optional): Reference to academic session (nullable)

Error responses:

- 400: Bad Request → raises `RequestError`
- 401: Unauthorized → raises `AuthError`
- 403: Forbidden → raises `RequestError`
- 404: Not Found → raises `NotFoundError`
- 422: Unprocessable Entity / Validation Error → raises `RequestError`
- 429: Too Many Requests → raises `RateLimitError`
- 5xx: Server errors → raises `ServerError`

Python usage:

```python
from timeback import Timeback
from timeback.models.request import (
    TimebackGetAllLineItemsRequest,
    TimebackQueryParams,
)

client = Timeback()

# Example 1: Get all line items with default parameters
request = TimebackGetAllLineItemsRequest()
resp = client.oneroster.gradebook.get_all_line_items(request)

print(f"Total Line Items: {resp.total_count}")
print(f"Page {resp.page_number} of {resp.page_count}")

for line_item in resp.line_items:
    print(f"- Line Item {line_item.sourcedId}")
    print(f"  Title: {line_item.title}")
    if line_item.description:
        print(f"  Description: {line_item.description}")
    print(f"  Class: {line_item.class_.sourcedId}")
    print(f"  School: {line_item.school.sourcedId}")
    print(f"  Category: {line_item.category.sourcedId}")
    print(f"  Assign Date: {line_item.assignDate}")
    print(f"  Due Date: {line_item.dueDate}")
    if line_item.scoreScale:
        print(f"  Score Scale: {line_item.scoreScale.sourcedId}")

# Example 2: Get line items with query parameters
query_params = TimebackQueryParams(
    limit=50,
    offset=0,
    fields="sourcedId,title,assignDate,dueDate",
    filter="status='active'",
    sort="dueDate",
    orderBy="asc"
)
request_filtered = TimebackGetAllLineItemsRequest(query_params=query_params)
resp_filtered = client.oneroster.gradebook.get_all_line_items(request_filtered)

print(f"Filtered Line Items: {len(resp_filtered.line_items)} line items")
```

Notes:

- Line items represent assignments, assessments, or other gradable activities.
- The response is paginated - use `limit` and `offset` for pagination.
- The `search` parameter is a proprietary extension beyond the standard OneRoster specification.
- The maximum limit is 3000 items per page to prevent abuse and ensure optimal performance.
- Use the `fields` parameter to reduce response size by requesting only needed fields.
- The `filter` parameter follows the OneRoster filtering specification for complex queries.
- Required fields (`title`, `assignDate`, `dueDate`, `class`, `school`, `category`) must be present in all line items.

