## OneRoster — Gradebook - Get Line Items for Class

### GET /ims/oneroster/gradebook/v1p2/classes/{sourcedId}/lineItems

- Method: GET
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Get the set of lineItems on the service provider for a specific class. If the corresponding record cannot be located, the api will return a 404 error code and message 'Class not found.'

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

- `TimebackGetLineItemsForClassRequest` with required fields:
  - `class_sourced_id` (string): The sourcedId of the class (path parameter)
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
- `sourcedId` (str, optional): Unique identifier for the line item
- `status` (TimebackStatus): Status - "active" or "tobedeleted" (default: "active")
- `dateLastModified` (str, optional): Last modification timestamp in ISO 8601 format
- `metadata` (dict, optional): Additional metadata for the line item
- `title` (str): Title/name of the line item (required)
- `description` (str, optional): Description of the line item
- `assignDate` (str): Assignment date in ISO 8601 format (required)
- `dueDate` (str): Due date in ISO 8601 format (required)
- `class_` (TimebackSourcedIdReference): Reference to class (aliased as "class") (required)
- `school` (TimebackSourcedIdReference): Reference to school (required)
- `category` (TimebackSourcedIdReference): Reference to category (required)
- `gradingPeriod` (TimebackSourcedIdReference, optional): Reference to grading period
- `academicSession` (TimebackSourcedIdReference, optional): Reference to academic session
- `scoreScale` (TimebackSourcedIdReference, optional): Reference to score scale
- `resultValueMin` (float, optional): Minimum score value
- `resultValueMax` (float, optional): Maximum score value
- `learningObjectiveSet` (List[Dict[str, Any]], optional): Learning objectives

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
    TimebackGetLineItemsForClassRequest,
    TimebackQueryParams,
)

client = Timeback()
class_sourced_id = "class-123"

# Example 1: Get line items for a class with default parameters
request = TimebackGetLineItemsForClassRequest(
    class_sourced_id=class_sourced_id
)
resp = client.oneroster.gradebook.get_line_items_for_class(request)

print(f"Total Line Items: {resp.total_count}")
print(f"Page {resp.page_number} of {resp.page_count}")

for line_item in resp.line_items:
    print(f"- Line Item {line_item.sourcedId}")
    print(f"  Title: {line_item.title}")
    print(f"  Status: {line_item.status}")
    print(f"  Class: {line_item.class_.sourcedId}")
    print(f"  School: {line_item.school.sourcedId}")
    print(f"  Category: {line_item.category.sourcedId}")
    print(f"  Assign Date: {line_item.assignDate}")
    print(f"  Due Date: {line_item.dueDate}")
    if line_item.description:
        print(f"  Description: {line_item.description}")
    if line_item.resultValueMin is not None:
        print(f"  Min Score: {line_item.resultValueMin}")
    if line_item.resultValueMax is not None:
        print(f"  Max Score: {line_item.resultValueMax}")

# Example 2: Get line items with query parameters
query_params = TimebackQueryParams(
    limit=50,
    offset=0,
    fields="sourcedId,title,assignDate,dueDate",
    filter="status='active'",
    sort="dueDate",
    orderBy="asc"
)
request_filtered = TimebackGetLineItemsForClassRequest(
    class_sourced_id=class_sourced_id,
    query_params=query_params
)
resp_filtered = client.oneroster.gradebook.get_line_items_for_class(request_filtered)

print(f"Filtered Line Items: {len(resp_filtered.line_items)} line items")
```

Notes:

- Line items represent assignments, assessments, or other graded activities within a class.
- The response is paginated - use `limit` and `offset` for pagination.
- The `search` parameter is a proprietary extension beyond the standard OneRoster specification.
- The maximum limit is 3000 items per page to prevent abuse and ensure optimal performance.
- Use the `fields` parameter to reduce response size by requesting only needed fields.
- The `filter` parameter follows the OneRoster filtering specification for complex queries.
- Required fields (`title`, `assignDate`, `dueDate`, `class`, `school`, `category`) must be present in all line items.
- If the class does not exist, the API will return a 404 error with message 'Class not found.'

