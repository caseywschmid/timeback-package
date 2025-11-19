## OneRoster — Gradebook - Get All Score Scales

### GET /ims/oneroster/gradebook/v1p2/scoreScales

- Method: GET
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Get all of the ScoreScales on the service provider

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

- `TimebackGetAllScoreScalesRequest` with optional fields:
  - `query_params` (TimebackQueryParams, optional): Query parameters for filtering, pagination, sorting, etc.

Successful response (HTTP 200):

- Body: `TimebackGetAllScoreScalesResponse` with fields:
  - `score_scales` (List[TimebackScoreScale]): List of score scales. See TimebackScoreScale for structure.
  - `total_count` (int): Total number of results
  - `page_count` (int): Total number of pages
  - `page_number` (int): Current page number
  - `offset` (int): Offset for pagination
  - `limit` (int): Limit per page

Each `TimebackScoreScale` contains:
- `sourcedId` (str): Unique identifier
- `status` (TimebackStatus): Status - "active" or "tobedeleted"
- `dateLastModified` (str, optional): Last modification timestamp
- `metadata` (dict, optional): Additional metadata
- `title` (str): Title of the score scale
- `type` (str): Type of the score scale
- `class_` (TimebackSourcedIdReference): Associated class reference
- `course` (TimebackSourcedIdReference, optional): Associated course reference
- `scoreScaleValue` (List[TimebackScoreScaleValue]): List of scale values

Each `TimebackScoreScaleValue` contains:
- `itemValueLHS` (str): Left-hand side value (e.g., "90")
- `itemValueRHS` (str): Right-hand side value (e.g., "100")
- `value` (str): Display value (e.g., "A")
- `description` (str, optional): Description (e.g., "Excellent")

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
    TimebackGetAllScoreScalesRequest,
    TimebackQueryParams,
)

client = Timeback()

# Example 1: Get all score scales with default parameters
request = TimebackGetAllScoreScalesRequest()
resp = client.oneroster.gradebook.get_all_score_scales(request)

print(f"Total Score Scales: {resp.total_count}")
print(f"Page {resp.page_number} of {resp.page_count}")

for scale in resp.score_scales:
    print(f"- {scale.title} ({scale.sourcedId})")
    print(f"  Type: {scale.type}")
    print(f"  Status: {scale.status}")
    print(f"  Values: {len(scale.scoreScaleValue)} scale values")

# Example 2: Get score scales with query parameters
query_params = TimebackQueryParams(
    limit=50,
    offset=0,
    fields="sourcedId,title,type",
    filter="status='active'",
    sort="title",
    orderBy="asc"
)
request_filtered = TimebackGetAllScoreScalesRequest(query_params=query_params)
resp_filtered = client.oneroster.gradebook.get_all_score_scales(request_filtered)

print(f"Filtered Results: {len(resp_filtered.score_scales)} score scales")
```

Notes:

- This is the first **Gradebook** endpoint in the package (previous endpoints were Rostering).
- Score scales define grading scales used for assessments and results.
- The response is paginated - use `limit` and `offset` for pagination.
- The `search` parameter is a proprietary extension beyond the standard OneRoster specification.
- The maximum limit is 3000 items per page to prevent abuse and ensure optimal performance.
- Use the `fields` parameter to reduce response size by requesting only needed fields.
- The `filter` parameter follows the OneRoster filtering specification for complex queries.
