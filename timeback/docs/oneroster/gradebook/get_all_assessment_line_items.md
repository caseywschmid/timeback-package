## OneRoster — Gradebook - Get All Assessment Line Items

### GET /ims/oneroster/gradebook/v1p2/assessmentLineItems

- Method: GET
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Get all assessment line items on the service provider (paginated).

Query params:

- `fields` (string, optional): Comma-separated list of fields to include
- `limit` (integer, optional): Maximum items per page (default: 100, max: 3000)
- `offset` (integer, optional): Number of items to skip
- `sort` (string, optional): Field to sort by
- `orderBy` (string, optional): Sort direction (`asc` or `desc`)
- `filter` (string, optional): Filter expression
- `search` (string, optional): Free-text search

Successful response (HTTP 200):

- Body: Paginated list of assessment line items
  - `assessmentLineItems`: Array of LineItem objects
  - `totalCount`: Total number of items
  - `pageCount`: Total number of pages
  - `pageNumber`: Current page number
  - `offset`: Current offset
  - `limit`: Current limit

Python usage:

```python
from timeback import Timeback
from timeback.models.request import TimebackGetAllAssessmentLineItemsRequest, TimebackQueryParams

client = Timeback()

# Basic request
request = TimebackGetAllAssessmentLineItemsRequest()
response = client.oneroster.gradebook.get_all_assessment_line_items(request)

print(f"Total: {response.total_count}")
for ali in response.assessmentLineItems:
    print(f"  {ali.sourcedId}: {ali.title}")

# With pagination
query_params = TimebackQueryParams(limit=50, offset=0, sort="title", order_by="asc")
request = TimebackGetAllAssessmentLineItemsRequest(query_params=query_params)
response = client.oneroster.gradebook.get_all_assessment_line_items(request)
```

Notes:

- Assessment line items define assignments, quizzes, and other gradeable items.
- Each line item has references to class, school, and category.
- The `component` and `componentResource` fields are proprietary extensions.

