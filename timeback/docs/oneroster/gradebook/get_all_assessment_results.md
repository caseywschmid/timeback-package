## OneRoster — Gradebook - Get All Assessment Results

### GET /ims/oneroster/gradebook/v1p2/assessmentResults

- Method: GET
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Get all assessment results on the service provider (paginated).

Query params:

- `fields` (string, optional): Comma-separated list of fields to include
- `limit` (integer, optional): Maximum items per page (default: 100, max: 3000)
- `offset` (integer, optional): Number of items to skip
- `sort` (string, optional): Field to sort by
- `orderBy` (string, optional): Sort direction (`asc` or `desc`)
- `filter` (string, optional): Filter expression
- `search` (string, optional): Free-text search

Successful response (HTTP 200):

- Body: Paginated list of assessment results
  - `assessmentResults`: Array of AssessmentResult objects
  - `totalCount`: Total number of items
  - `pageCount`: Total number of pages
  - `pageNumber`: Current page number
  - `offset`: Current offset
  - `limit`: Current limit

Error responses:

- 400/422: Request/validation → raises `RequestError`
- 401: Unauthorized → raises `AuthError`
- 403: Forbidden → raises `RequestError`
- 429: Too Many Requests → raises `RateLimitError`
- 5xx: Server errors → raises `ServerError`

Python usage:

```python
from timeback import Timeback
from timeback.models.request import TimebackGetAllAssessmentResultsRequest, TimebackQueryParams

client = Timeback()

# Basic request
request = TimebackGetAllAssessmentResultsRequest()
response = client.oneroster.gradebook.get_all_assessment_results(request)

print(f"Total: {response.total_count}")
for ar in response.assessmentResults:
    print(f"  {ar.sourcedId}: score={ar.score}")

# With pagination and sorting
query_params = TimebackQueryParams(
    limit=50,
    offset=0,
    sort="scoreDate",
    order_by="desc"
)
request = TimebackGetAllAssessmentResultsRequest(query_params=query_params)
response = client.oneroster.gradebook.get_all_assessment_results(request)
```

Notes:

- Assessment results link students to their scores on specific assessment line items.
- Each assessment result contains a reference to the student and the assessment line item.
- The `scoreStatus` field indicates whether the result is fully graded, partially graded, etc.
- Use pagination parameters to handle large result sets efficiently.

