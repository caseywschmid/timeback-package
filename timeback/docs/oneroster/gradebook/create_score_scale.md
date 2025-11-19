## OneRoster — Gradebook - Create Score Scale

### POST /ims/oneroster/gradebook/v1p2/scoreScales

- Method: POST
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Create a new scoreScale. The responding system returns the sourcedIds that have been allocated to the newly created scoreScale record.

Request model:

- `TimebackCreateScoreScaleRequest` with required fields:
  - `score_scale` (TimebackScoreScale): Score scale data to create. See TimebackScoreScale for structure.

Request body (application/json):

The request body contains a `scoreScale` object with the following structure:

```json
{
  "scoreScale": {
    "sourcedId": "string",
    "status": "active" | "tobedeleted",
    "dateLastModified": "2024-01-01T00:00:00Z",
    "metadata": {},
    "title": "string",
    "type": "string",
    "class": {
      "sourcedId": "string"
    },
    "course": {
      "sourcedId": "string"
    },
    "scoreScaleValue": [
      {
        "itemValueLHS": "string",
        "itemValueRHS": "string",
        "value": "string",
        "description": "string"
      }
    ]
  }
}
```

**Required fields in scoreScale:**
- `status` (TimebackStatus): Status - "active" or "tobedeleted"
- `title` (str): Title of the score scale
- `type` (str): Type of the score scale
- `class` (TimebackSourcedIdReference): Associated class reference with sourcedId
- `scoreScaleValue` (List[TimebackScoreScaleValue]): List of scale values (at least one)

**Optional fields:**
- `sourcedId` (str): Client-supplied sourcedId (will be allocated by server if not provided)
- `dateLastModified` (str): Last modification timestamp
- `metadata` (dict): Additional metadata
- `course` (TimebackSourcedIdReference): Associated course reference

**Each scoreScaleValue requires:**
- `itemValueLHS` (str): Left-hand side value (e.g., "90")
- `itemValueRHS` (str): Right-hand side value (e.g., "100")
- `value` (str, optional): Display value (e.g., "A")
- `description` (str, optional): Description (e.g., "Excellent")

Successful response (HTTP 201):

- Body: `TimebackCreateScoreScaleResponse` with fields:
  - `sourcedIdPairs` (TimebackSourcedIdPairs): SourcedId mapping containing:
    - `suppliedSourcedId` (str): Client-supplied sourcedId
    - `allocatedSourcedId` (str): Server-allocated sourcedId

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
from timeback.models.request import TimebackCreateScoreScaleRequest
from timeback.models.timeback_score_scale import (
    TimebackScoreScale,
    TimebackScoreScaleValue,
)
from timeback.models.timeback_sourced_id_ref import TimebackSourcedIdReference
from timeback.enums import TimebackStatus

client = Timeback()

# Create scale values (grade ranges)
scale_values = [
    TimebackScoreScaleValue(
        itemValueLHS="90",
        itemValueRHS="100",
        value="A",
        description="Excellent",
    ),
    TimebackScoreScaleValue(
        itemValueLHS="80",
        itemValueRHS="89",
        value="B",
        description="Good",
    ),
    TimebackScoreScaleValue(
        itemValueLHS="70",
        itemValueRHS="79",
        value="C",
        description="Satisfactory",
    ),
    TimebackScoreScaleValue(
        itemValueLHS="60",
        itemValueRHS="69",
        value="D",
        description="Needs Improvement",
    ),
    TimebackScoreScaleValue(
        itemValueLHS="0",
        itemValueRHS="59",
        value="F",
        description="Failing",
    ),
]

# Create the score scale
score_scale = TimebackScoreScale(
    sourcedId="my-letter-grade-scale-001",
    status=TimebackStatus.ACTIVE,
    title="Standard Letter Grade Scale",
    type="letter",
    **{"class": TimebackSourcedIdReference(sourcedId="class-123-456")},
    course=None,
    scoreScaleValue=scale_values,
    metadata={"description": "Standard A-F grading scale"},
)

# Create the request
request = TimebackCreateScoreScaleRequest(score_scale=score_scale)

# Call the API
resp = client.oneroster.gradebook.create_score_scale(request)

print(f"Supplied SourcedId: {resp.sourcedIdPairs.suppliedSourcedId}")
print(f"Allocated SourcedId: {resp.sourcedIdPairs.allocatedSourcedId}")
```

Notes:

- The response returns a `sourcedIdPairs` object mapping the supplied sourcedId to the allocated sourcedId.
- If you don't provide a `sourcedId`, the server will generate one for you.
- Score scales define grading scales used for assessments and results.
- Each `scoreScaleValue` defines a range (LHS to RHS) with a display value and optional description.
- The `class` field is required and must reference an existing class.
- The `course` field is optional and can be null.
- Use `**{"class": ...}` syntax in Python because `class` is a reserved keyword.

Common Use Cases:

1. **Letter Grades (A-F)**: Standard academic grading
2. **Percentage Scales**: 0-100% ranges
3. **Pass/Fail**: Simple binary grading
4. **Custom Scales**: Institution-specific grading systems
