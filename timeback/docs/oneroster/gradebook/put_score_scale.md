## OneRoster — Gradebook - Put Score Scale

### PUT /ims/oneroster/gradebook/v1p2/scoreScales/{sourcedId}

- Method: PUT
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Update an existing scoreScale or create a new one if it doesn't exist. The sourcedId for the record is supplied by the requesting system.

Path params:

- `sourcedId` (string, required): The sourcedId of the score scale to update/create

Request model:

- `TimebackPutScoreScaleRequest` with required fields:
  - `sourced_id` (string): The sourcedId of the score scale (path parameter)
  - `score_scale` (TimebackScoreScale): Score scale data to update/create. See TimebackScoreScale for structure.

Request body (application/json):

The request body contains a `scoreScale` object. The `sourcedId` in the body should match the path parameter.

```json
{
  "scoreScale": {
    "sourcedId": "string",
    "status": "active",
    "title": "string",
    "type": "string",
    "class": { "sourcedId": "string" },
    "scoreScaleValue": [...]
  }
}
```

Successful response (HTTP 201):

- Body: `TimebackPutScoreScaleResponse` with fields:
  - `score_scale` (TimebackScoreScale): The updated/created score scale.

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
from timeback.models.request import TimebackPutScoreScaleRequest
from timeback.models.timeback_score_scale import (
    TimebackScoreScale,
    TimebackScoreScaleValue,
)
from timeback.models.timeback_sourced_id_ref import TimebackSourcedIdReference
from timeback.enums import TimebackStatus

client = Timeback()
sourced_id = "scale-123-456"

# Create scale values
scale_values = [
    TimebackScoreScaleValue(
        itemValueLHS="90",
        itemValueRHS="100",
        value="A",
        description="Excellent",
    )
]

# Create the score scale object
score_scale = TimebackScoreScale(
    sourcedId=sourced_id,
    status=TimebackStatus.ACTIVE,
    title="Updated Letter Grade Scale",
    type="letter",
    **{"class": TimebackSourcedIdReference(sourcedId="class-123-456")},
    scoreScaleValue=scale_values,
)

# Create the request
request = TimebackPutScoreScaleRequest(
    sourced_id=sourced_id, 
    score_scale=score_scale
)

# Call the API
resp = client.oneroster.gradebook.put_score_scale(request)

print(f"Updated: {resp.score_scale.title}")
```

Notes:

- This endpoint is idempotent: calling it multiple times with the same data produces the same result.
- The `sourcedId` in the path must match the `sourcedId` in the body.
- If the score scale does not exist, it will be created with the provided `sourcedId`.
- If it exists, it will be updated.
