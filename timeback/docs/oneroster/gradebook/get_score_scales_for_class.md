## OneRoster — Gradebook - Get Score Scales for Class

### GET /ims/oneroster/gradebook/v1p2/classes/{sourcedId}/scoreScales

- Method: GET
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Get the set of scoreScales on the service provider for a specific class. If the corresponding record cannot be located, the api will return a 404 error code and message 'Class not found.'

Path params:

- `sourcedId` (string, required): The sourcedId of the class

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

- `TimebackGetScoreScalesForClassRequest` with required fields:
  - `class_sourced_id` (string): The sourcedId of the class (path parameter)
  - `query_params` (TimebackQueryParams, optional): Query parameters for filtering, pagination, sorting, etc.

Successful response (HTTP 200):

- Body: `TimebackGetScoreScalesForSchoolResponse` with fields:
  - `score_scales` (List[TimebackScoreScale]): List of score scales. See TimebackScoreScale for structure.
  - `total_count` (int): Total number of score scales
  - `page_count` (int): Total number of pages
  - `page_number` (int): Current page number
  - `offset` (int): Offset for pagination
  - `limit` (int): Limit per page

Each `TimebackScoreScale` contains:
- `sourcedId` (str): Unique identifier for the score scale
- `status` (TimebackStatus): Status - "active" or "tobedeleted" (required)
- `dateLastModified` (str, optional): Last modification timestamp in ISO 8601 format
- `metadata` (dict, optional): Additional metadata for the score scale
- `title` (str): Title/name of the score scale (required)
- `type` (str): Type of score scale (e.g., "letter", "percentage") (required)
- `class_` (TimebackSourcedIdReference): Reference to class (aliased as "class") (required)
- `course` (TimebackSourcedIdReference, optional): Reference to course
- `scoreScaleValue` (List[TimebackScoreScaleValue]): List of score scale values (required)

Each `TimebackScoreScaleValue` contains:
- `itemValueLHS` (str): Left-hand side value (required)
- `itemValueRHS` (str): Right-hand side value (required)
- `value` (str): The score scale value
- `description` (str, optional): Description of the value

Error responses:

- 400: Bad Request → raises `RequestError`
- 401: Unauthorized → raises `AuthError`
- 403: Forbidden → raises `RequestError`
- 404: Class not found → raises `NotFoundError`
- 422: Unprocessable Entity / Validation Error → raises `RequestError`
- 429: Too Many Requests → raises `RateLimitError`
- 5xx: Server errors → raises `ServerError`

Python usage:

```python
from timeback import Timeback
from timeback.models.request import (
    TimebackGetScoreScalesForClassRequest,
    TimebackQueryParams,
)

client = Timeback()
class_sourced_id = "class-123"

# Example 1: Get score scales for a class with default parameters
request = TimebackGetScoreScalesForClassRequest(
    class_sourced_id=class_sourced_id
)
resp = client.oneroster.gradebook.get_score_scales_for_class(request)

print(f"Total Score Scales: {resp.total_count}")
print(f"Page {resp.page_number} of {resp.page_count}")

for scale in resp.score_scales:
    print(f"- Score Scale {scale.sourcedId}")
    print(f"  Title: {scale.title}")
    print(f"  Type: {scale.type}")
    print(f"  Status: {scale.status}")
    print(f"  Class: {scale.class_.sourcedId}")
    if scale.course:
        print(f"  Course: {scale.course.sourcedId}")
    print(f"  Score Scale Values:")
    for value in scale.scoreScaleValue:
        print(f"    {value.itemValueLHS}-{value.itemValueRHS}: {value.value}")
        if value.description:
            print(f"      Description: {value.description}")

# Example 2: Get score scales with query parameters
query_params = TimebackQueryParams(
    limit=50,
    offset=0,
    fields="sourcedId,title,type",
    filter="status='active'",
    sort="title",
    orderBy="asc"
)
request_filtered = TimebackGetScoreScalesForClassRequest(
    class_sourced_id=class_sourced_id,
    query_params=query_params
)
resp_filtered = client.oneroster.gradebook.get_score_scales_for_class(request_filtered)

print(f"Filtered Score Scales: {len(resp_filtered.score_scales)} score scales")
```

Notes:

- Score scales define how numeric scores are converted to letter grades, percentages, or other grading systems.
- Each score scale contains a list of `scoreScaleValue` entries that map score ranges to values.
- The response is paginated - use `limit` and `offset` for pagination.
- The `search` parameter is a proprietary extension beyond the standard OneRoster specification.
- The maximum limit is 3000 items per page to prevent abuse and ensure optimal performance.
- Use the `fields` parameter to reduce response size by requesting only needed fields.
- The `filter` parameter follows the OneRoster filtering specification for complex queries.
- Required fields (`status`, `title`, `type`, `class`, `scoreScaleValue`) must be present in all score scales.
- If the class does not exist, the API will return a 404 error with message 'Class not found.'

