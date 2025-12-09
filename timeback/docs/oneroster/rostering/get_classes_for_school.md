## OneRoster — Rostering - Get Classes for School

### GET /ims/oneroster/rostering/v1p2/schools/{schoolSourcedId}/classes

- Method: GET
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Fetch all classes for a specific school with pagination support.

Path params:

- `schoolSourcedId` (string, required): The sourcedId of the school

Query params:

- `fields` (string, optional): Comma-separated list of fields to include
- `limit` (integer, optional): Maximum items to return (default: 100, max: 3000)
- `offset` (integer, optional): Number of items to skip (default: 0)
- `sort` (string, optional): Field to sort by
- `orderBy` (string, optional): Sort order - "asc" or "desc"
- `filter` (string, optional): Filter expression (e.g., `status='active'`)
- `search` (string, optional): Free-text search (proprietary extension)

Successful response (HTTP 200):

- Body: `{ "classes": [...], "totalCount": N, "pageCount": N, "pageNumber": N, "offset": N, "limit": N }`
- The `classes` array contains Class objects with standard OneRoster fields

Error responses:

- 400/422: Request/validation → raises `RequestError`
- 401: Unauthorized → raises `AuthError`
- 403: Forbidden → raises `RequestError`
- 404: School not found → raises `NotFoundError`
- 429: Too Many Requests → raises `RateLimitError`
- 5xx: Server errors → raises `ServerError`

Python usage:

```python
from timeback import Timeback
from timeback.models.request import TimebackGetClassesForSchoolRequest, TimebackQueryParams

client = Timeback()

# Basic request - get all classes for a school
request = TimebackGetClassesForSchoolRequest(school_sourced_id="<schoolSourcedId>")
response = client.oneroster.rostering.get_classes_for_school(request)

print(f"Total classes: {response.total_count}")
for cls in response.classes:
    print(f"  - {cls.sourcedId}: {cls.title}")

# With pagination and filtering
query_params = TimebackQueryParams(
    limit=10,
    offset=0,
    filter="status='active'",
    sort="title",
    order_by="asc",
)
request_with_params = TimebackGetClassesForSchoolRequest(
    school_sourced_id="<schoolSourcedId>",
    query_params=query_params,
)
response_filtered = client.oneroster.rostering.get_classes_for_school(request_with_params)
```

Notes:

- The response uses `TimebackGetAllClassesResponse` which includes pagination metadata.
- If the school does not exist, a `NotFoundError` is raised.
- The `search` parameter is a proprietary extension for free-text searching across class fields.
- The `filter` parameter uses OneRoster filter syntax (e.g., `status='active'`).

