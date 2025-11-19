## OneRoster — Gradebook - Get Score Scales for School

### GET /ims/oneroster/gradebook/v1p2/schools/{sourcedId}/scoreScales

- Method: GET
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Get the set of scoreScales on the service provider for a specific school.

Path params:

- `sourcedId` (string, required): The sourcedId of the school

Query Parameters:

- `limit` (int, optional): Max items to return (default 100, max 3000)
- `offset` (int, optional): Items to skip (default 0)
- `sort` (string, optional): Field to sort by
- `orderBy` (string, optional): "asc" or "desc"
- `filter` (string, optional): Filter expression (e.g., "status='active'")
- `fields` (string, optional): Fields to include
- `search` (string, optional): Free-text search

Request model:

- `TimebackGetScoreScalesForSchoolRequest` with fields:
  - `sourced_id` (string, required): The sourcedId of the school
  - `query_params` (TimebackQueryParams, optional): Query parameters

Successful response (HTTP 200):

- Body: `TimebackGetScoreScalesForSchoolResponse` with fields:
  - `score_scales` (List[TimebackScoreScale]): List of score scales
  - `total_count` (int): Total count
  - `page_count` (int): Total pages
  - `page_number` (int): Current page
  - `offset` (int): Current offset
  - `limit` (int): Current limit

Error responses:

- 400: Bad Request → raises `RequestError`
- 401: Unauthorized → raises `AuthError`
- 403: Forbidden → raises `RequestError`
- 404: School Not Found → raises `NotFoundError`
- 422: Unprocessable Entity / Validation Error → raises `RequestError`
- 429: Too Many Requests → raises `RateLimitError`
- 5xx: Server errors → raises `ServerError`

Python usage:

```python
from timeback import Timeback
from timeback.models.request import (
    TimebackGetScoreScalesForSchoolRequest,
    TimebackQueryParams,
)

client = Timeback()
school_sourced_id = "school-123-456"

# Example 1: Get score scales for school
request = TimebackGetScoreScalesForSchoolRequest(sourced_id=school_sourced_id)
resp = client.oneroster.gradebook.get_score_scales_for_school(request)

print(f"Total Count: {resp.total_count}")
for scale in resp.score_scales:
    print(f"  - {scale.title} ({scale.sourcedId})")

# Example 2: Get score scales with pagination
query_params = TimebackQueryParams(limit=5, offset=0)
request_paginated = TimebackGetScoreScalesForSchoolRequest(
    sourced_id=school_sourced_id, query_params=query_params
)
resp_paginated = client.oneroster.gradebook.get_score_scales_for_school(request_paginated)
```

Notes:

- If the school sourcedId is invalid or not found, the API returns a 404 error.
- Supports standard OneRoster pagination and filtering.
