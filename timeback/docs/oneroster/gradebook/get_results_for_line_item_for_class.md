## OneRoster — Gradebook - Get Results for Line Item for Class

### GET /ims/oneroster/gradebook/v1p2/classes/{classSourcedId}/lineItems/{lineItemSourcedId}/results

- Method: GET
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Get the set of results on the service provider for a specific lineItem and for a specific class. If the corresponding record cannot be located, the api will return a 404 error code and message 'Class or line item not found.'

Path params:

- `classSourcedId` (string, required): The sourcedId of the class
- `lineItemSourcedId` (string, required): The sourcedId of the line item

Query Parameters:

All query parameters are optional and can be passed via `TimebackQueryParams`:

- `fields` (string, optional): Comma-separated list of fields to include in the response (e.g., "sourcedId,scoreStatus")
- `limit` (integer, optional): Maximum number of items per page (default: 100, maximum: 3000)
- `offset` (integer, optional): Number of items to skip for pagination (default: 0)
- `sort` (string, optional): Field to sort the response by
- `orderBy` (string, optional): Sort order - "asc" or "desc"
- `filter` (string, optional): Filter expression following OneRoster specification (e.g., "status='active'")
- `search` (string, optional): **PROPRIETARY EXTENSION** - Free-text search across multiple fields

Request model:

- `TimebackGetResultsForLineItemForClassRequest` with required fields:
  - `class_sourced_id` (string): The sourcedId of the class (path parameter)
  - `line_item_sourced_id` (string): The sourcedId of the line item (path parameter)
  - `query_params` (TimebackQueryParams, optional): Query parameters for filtering, pagination, sorting, etc.

Successful response (HTTP 200):

- Body: `TimebackGetAllResultsResponse` with fields:
  - `results` (List[TimebackResult]): List of results. See TimebackResult for structure.
  - `total_count` (int): Total number of results
  - `page_count` (int): Total number of pages
  - `page_number` (int): Current page number
  - `offset` (int): Offset for pagination
  - `limit` (int): Limit per page

Each `TimebackResult` contains:
- `sourcedId` (str, optional): Unique identifier
- `status` (TimebackStatus): Status - "active" or "tobedeleted" (required)
- `dateLastModified` (str, optional): Last modification timestamp
- `metadata` (dict, optional): Additional metadata
- `lineItem` (TimebackSourcedIdReference): Reference to the line item (required)
- `student` (TimebackSourcedIdReference): Reference to the student (required)
- `class_` (TimebackSourcedIdReference, optional): Reference to class (aliased as "class")
- `scoreScale` (TimebackSourcedIdReference, optional): Reference to score scale
- `scoreStatus` (TimebackScoreStatus): Status of the score - "exempt", "fully graded", "not submitted", "partially graded", or "submitted" (required)
- `score` (float, optional): Numeric score value
- `textScore` (str, optional): Text representation of the score
- `scoreDate` (str): Date when the score was recorded in ISO 8601 format (required)
- `comment` (str, optional): Comment about the result
- `learningObjectiveSet` (List[TimebackLearningObjectiveSet], optional): Learning objective results
- `inProgress` (str, optional): In progress indicator
- `incomplete` (str, optional): Incomplete indicator
- `late` (str, optional): Late indicator
- `missing` (str, optional): Missing indicator

Error responses:

- 400: Bad Request → raises `RequestError`
- 401: Unauthorized → raises `AuthError`
- 403: Forbidden → raises `RequestError`
- 404: Class or line item not found → raises `NotFoundError`
- 422: Unprocessable Entity / Validation Error → raises `RequestError`
- 429: Too Many Requests → raises `RateLimitError`
- 5xx: Server errors → raises `ServerError`

Python usage:

```python
from timeback import Timeback
from timeback.models.request import (
    TimebackGetResultsForLineItemForClassRequest,
    TimebackQueryParams,
)

client = Timeback()
class_sourced_id = "class-123"
line_item_sourced_id = "line-item-456"

# Example 1: Get results for a line item and class with default parameters
request = TimebackGetResultsForLineItemForClassRequest(
    class_sourced_id=class_sourced_id,
    line_item_sourced_id=line_item_sourced_id
)
resp = client.oneroster.gradebook.get_results_for_line_item_for_class(request)

print(f"Total Results: {resp.total_count}")
print(f"Page {resp.page_number} of {resp.page_count}")

for result in resp.results:
    print(f"- Result {result.sourcedId}")
    print(f"  Student: {result.student.sourcedId}")
    print(f"  Line Item: {result.lineItem.sourcedId}")
    print(f"  Class: {result.class_.sourcedId if result.class_ else 'N/A'}")
    print(f"  Score Status: {result.scoreStatus}")
    if result.score is not None:
        print(f"  Score: {result.score}")
    if result.textScore:
        print(f"  Text Score: {result.textScore}")
    print(f"  Score Date: {result.scoreDate}")

# Example 2: Get results with query parameters
query_params = TimebackQueryParams(
    limit=50,
    offset=0,
    fields="sourcedId,scoreStatus,score",
    filter="status='active'",
    sort="scoreDate",
    orderBy="desc"
)
request_filtered = TimebackGetResultsForLineItemForClassRequest(
    class_sourced_id=class_sourced_id,
    line_item_sourced_id=line_item_sourced_id,
    query_params=query_params
)
resp_filtered = client.oneroster.gradebook.get_results_for_line_item_for_class(request_filtered)

print(f"Filtered Results: {len(resp_filtered.results)} results")
```

Notes:

- This endpoint returns only results associated with the specified class and line item.
- Results represent student performance on line items (assignments, assessments, etc.).
- The response is paginated - use `limit` and `offset` for pagination.
- The `search` parameter is a proprietary extension beyond the standard OneRoster specification.
- The maximum limit is 3000 items per page to prevent abuse and ensure optimal performance.
- Use the `fields` parameter to reduce response size by requesting only needed fields.
- The `filter` parameter follows the OneRoster filtering specification for complex queries.
- Required fields (`status`, `lineItem`, `student`, `scoreStatus`, `scoreDate`) must be present in all results.
- If the class or line item does not exist, the API will return a 404 error with message 'Class or line item not found.'

