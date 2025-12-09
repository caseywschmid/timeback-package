## OneRoster — Gradebook - Get Result

### GET /ims/oneroster/gradebook/v1p2/results/{sourcedId}

- Method: GET
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Get a specific result on the service provider. If the corresponding record cannot be located, the api will return a 404 error code and message 'Result not found.'

Path params:

- `sourcedId` (string, required): The sourcedId of the result to fetch

Query Parameters:

- `fields` (string, optional): Comma-separated list of fields to include in the response (e.g., "sourcedId,score,textScore")
  - Passed via `TimebackQueryParams`

Request model:

- `TimebackGetResultRequest` with fields:
  - `sourced_id` (string, required): The sourcedId of the result
  - `query_params` (TimebackQueryParams, optional): Query parameters

Successful response (HTTP 200):

- Body: `TimebackGetResultResponse` with fields:
  - `result` (TimebackResult): The requested result. See TimebackResult for structure.

Error responses:

- 400: Bad Request → raises `RequestError`
- 401: Unauthorized → raises `AuthError`
- 403: Forbidden → raises `RequestError`
- 404: Result not found → raises `NotFoundError`
- 422: Unprocessable Entity / Validation Error → raises `RequestError`
- 429: Too Many Requests → raises `RateLimitError`
- 5xx: Server errors → raises `ServerError`

Python usage:

```python
from timeback import Timeback
from timeback.models.request import (
    TimebackGetResultRequest,
    TimebackQueryParams,
)

client = Timeback()
sourced_id = "result-123-456"

# Example 1: Get result by sourcedId
request = TimebackGetResultRequest(sourced_id=sourced_id)
resp = client.oneroster.gradebook.get_result(request)

result = resp.result
print(f"Found Result: {result.sourcedId}")
print(f"Status: {result.status}")
print(f"Score Status: {result.scoreStatus}")
print(f"Score Date: {result.scoreDate}")
if result.score is not None:
    print(f"Score: {result.score}")
if result.textScore is not None:
    print(f"Text Score: {result.textScore}")
if result.comment is not None:
    print(f"Comment: {result.comment}")
print(f"Line Item: {result.lineItem.sourcedId}")
print(f"Student: {result.student.sourcedId}")

# Example 2: Get result with fields parameter
query_params = TimebackQueryParams(fields="sourcedId,score,textScore,comment")
request_fields = TimebackGetResultRequest(
    sourced_id=sourced_id, query_params=query_params
)
resp_fields = client.oneroster.gradebook.get_result(request_fields)
print(f"Fetched partial result: {resp_fields.result.sourcedId}")
```

Notes:

- Returns a single result object wrapped in the response.
- Use the `fields` parameter to reduce response size by requesting only needed fields.
- If the result is not found, a `NotFoundError` (404) will be raised.
- The result includes references to `lineItem` and `student` which contain only the `sourcedId` of those entities.
- Optional fields like `score`, `textScore`, `comment`, `class`, and `scoreScale` may be `None` if not set.

