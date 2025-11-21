## OneRoster — Gradebook - Get Line Item

### GET /ims/oneroster/gradebook/v1p2/lineItems/{sourcedId}

- Method: GET
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Get a specific Line Item on the service provider. If the corresponding record cannot be located, the api will return a 404 error code and message 'Line item not found.'

Path params:

- `sourcedId` (string, required): The sourcedId of the line item to fetch

Query Parameters:

- `fields` (string, optional): Comma-separated list of fields to include in the response (e.g., "sourcedId,title,assignDate")
  - Passed via `TimebackQueryParams`

Request model:

- `TimebackGetLineItemRequest` with fields:
  - `sourced_id` (string, required): The sourcedId of the line item
  - `query_params` (TimebackQueryParams, optional): Query parameters

Successful response (HTTP 200):

- Body: `TimebackGetLineItemResponse` with fields:
  - `line_item` (LineItem): The requested line item. See LineItem for structure.

Error responses:

- 400: Bad Request → raises `RequestError`
- 401: Unauthorized → raises `AuthError`
- 403: Forbidden → raises `RequestError`
- 404: Line item not found → raises `NotFoundError`
- 422: Unprocessable Entity / Validation Error → raises `RequestError`
- 429: Too Many Requests → raises `RateLimitError`
- 5xx: Server errors → raises `ServerError`

Python usage:

```python
from timeback import Timeback
from timeback.models.request import (
    TimebackGetLineItemRequest,
    TimebackQueryParams,
)

client = Timeback()
sourced_id = "line-item-123-456"

# Example 1: Get line item by sourcedId
request = TimebackGetLineItemRequest(sourced_id=sourced_id)
resp = client.oneroster.gradebook.get_line_item(request)

line_item = resp.line_item
print(f"Found Line Item: {line_item.sourcedId}")
print(f"Title: {line_item.title}")
if line_item.description:
    print(f"Description: {line_item.description}")
print(f"Status: {line_item.status}")
print(f"Assign Date: {line_item.assignDate}")
print(f"Due Date: {line_item.dueDate}")
print(f"Class: {line_item.class_.sourcedId}")
print(f"School: {line_item.school.sourcedId}")
print(f"Category: {line_item.category.sourcedId}")
if line_item.scoreScale:
    print(f"Score Scale: {line_item.scoreScale.sourcedId}")

# Example 2: Get line item with fields parameter
query_params = TimebackQueryParams(fields="sourcedId,title,assignDate,dueDate")
request_fields = TimebackGetLineItemRequest(
    sourced_id=sourced_id, query_params=query_params
)
resp_fields = client.oneroster.gradebook.get_line_item(request_fields)
print(f"Fetched partial line item: {resp_fields.line_item.sourcedId}")
```

Notes:

- Returns a single line item object wrapped in the response.
- Use the `fields` parameter to reduce response size by requesting only needed fields.
- If the line item is not found, a `NotFoundError` (404) will be raised with message 'Line item not found.'
- The line item includes references to `class`, `school`, and `category` which contain only the `sourcedId` of those entities.
- Optional fields like `description`, `scoreScale`, `resultValueMin`, `resultValueMax`, `gradingPeriod`, and `academicSession` may be `None` if not set.

