## OneRoster — Gradebook - Get Score Scale

### GET /ims/oneroster/gradebook/v1p2/scoreScales/{sourcedId}

- Method: GET
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Get a specific scoreScale on the service provider.

Path params:

- `sourcedId` (string, required): The sourcedId of the score scale to fetch

Query Parameters:

- `fields` (string, optional): Comma-separated list of fields to include in the response (e.g., "sourcedId,title")
  - Passed via `TimebackQueryParams`

Request model:

- `TimebackGetScoreScaleRequest` with fields:
  - `sourced_id` (string, required): The sourcedId of the score scale
  - `query_params` (TimebackQueryParams, optional): Query parameters

Successful response (HTTP 200):

- Body: `TimebackGetScoreScaleResponse` with fields:
  - `score_scale` (TimebackScoreScale): The requested score scale. See TimebackScoreScale for structure.

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
    TimebackGetScoreScaleRequest,
    TimebackQueryParams,
)

client = Timeback()
sourced_id = "scale-123-456"

# Example 1: Get score scale by sourcedId
request = TimebackGetScoreScaleRequest(sourced_id=sourced_id)
resp = client.oneroster.gradebook.get_score_scale(request)

scale = resp.score_scale
print(f"Found Score Scale: {scale.title} ({scale.sourcedId})")
print(f"Type: {scale.type}")
print(f"Status: {scale.status}")

# Example 2: Get score scale with fields parameter
query_params = TimebackQueryParams(fields="sourcedId,title,type")
request_fields = TimebackGetScoreScaleRequest(
    sourced_id=sourced_id, query_params=query_params
)
resp_fields = client.oneroster.gradebook.get_score_scale(request_fields)
```

Notes:

- Returns a single score scale object wrapped in the response.
- Use the `fields` parameter to reduce response size by requesting only needed fields.
- If the score scale is not found, a `NotFoundError` (404) will be raised.
