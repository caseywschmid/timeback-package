## OneRoster — Rostering - Get All Classes

### GET /ims/oneroster/rostering/v1p2/classes

- Method: GET
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Get all Classes on the service provider (paginated).

Query params:

- `fields` (string, optional): Comma-separated fields to include (e.g., `sourcedId,title`)
- `limit` (integer, optional, default 100, max 3000): Max items per page
- `offset` (integer, optional, default 0): Number of items to skip
- `sort` (string, optional): Field to sort by
- `orderBy` (string, optional, enum: `asc`, `desc`): Sort order
- `filter` (string, optional): OneRoster filter expression (e.g., `status='active'`)
- `search` (string, optional): **PROPRIETARY EXTENSION** - Free-text search across multiple fields

Request model:

- `TimebackGetAllClassesRequest` with optional fields:
  - `query_params` (TimebackQueryParams, optional): Query parameters for filtering, pagination, sorting, etc.

Successful response (HTTP 200):

- Body: `TimebackGetAllClassesResponse` with fields:
  - `classes` (List[TimebackClass]): List of classes. See TimebackClass for structure.
  - `total_count` (int): Total number of classes
  - `page_count` (int): Total number of pages
  - `page_number` (int): Current page number
  - `offset` (int): Offset for pagination
  - `limit` (int): Limit per page

Each `TimebackClass` contains:
- `sourcedId` (str): Unique identifier for the class (required)
- `status` (TimebackStatus): Status - "active" or "tobedeleted" (required)
- `dateLastModified` (str, optional): Last modification timestamp in ISO 8601 format
- `metadata` (dict, optional): Additional metadata for the class
- `title` (str): Title/name of the class (required)
- `classCode` (str, optional): Class code identifier
- `classType` (TimebackClassType, optional): Type of class - "homeroom" or "scheduled"
- `location` (str, optional): Physical location of the class
- `grades` (List[str], optional): List of grade levels (e.g., ["9", "10", "11", "12"])
- `subjects` (List[str], optional): List of subjects (e.g., ["Math", "Science"])
- `course` (TimebackCourseRef): Reference to the parent course (required)
- `org` (TimebackOrgRef): Reference to the organization/school (required)
- `terms` (List[TimebackTermRef]): References to academic terms/sessions (required)
- `subjectCodes` (List[str], optional): List of subject codes
- `periods` (List[str], optional): List of class periods
- `resources` (List[TimebackSourcedIdReference], optional): References to learning resources

Error responses:

- 400/422: Request/validation → raises `RequestError`
- 401: Unauthorized → raises `AuthError`
- 403: Forbidden → raises `RequestError`
- 404: Not Found → raises `NotFoundError`
- 429: Too Many Requests → raises `RateLimitError`
- 5xx: Server errors → raises `ServerError`

Python usage:

```python
from timeback import Timeback
from timeback.models.request import TimebackGetAllClassesRequest, TimebackQueryParams

client = Timeback()

# Basic request without query params
request = TimebackGetAllClassesRequest()
response = client.oneroster.rostering.get_all_classes(request)

print(f"Total classes: {response.total_count}")
if response.classes:
    first_class = response.classes[0]
    print(f"First class: {first_class.sourcedId}, {first_class.title}")
    print(f"  Class Code: {first_class.classCode}")
    print(f"  Class Type: {first_class.classType}")
    print(f"  Location: {first_class.location}")
    print(f"  Course: {first_class.course.sourcedId}")
    print(f"  School: {first_class.org.sourcedId}")
    if first_class.terms:
        print(f"  Terms: {[term.sourcedId for term in first_class.terms]}")

# With query params
query_params = TimebackQueryParams(
    limit=50,
    offset=0,
    fields="sourcedId,title,classCode",
    filter="status='active'",
    sort="title",
    order_by="asc",
    search="math"
)
request_with_params = TimebackGetAllClassesRequest(query_params=query_params)
response_filtered = client.oneroster.rostering.get_all_classes(request_with_params)

print(f"Filtered classes: {len(response_filtered.classes)} classes on page {response_filtered.page_number}")
```

Notes:

- Classes represent specific instances of courses, typically for a particular term/semester.
- Students enroll in classes, not courses directly.
- The `search` parameter is a proprietary extension beyond the standard OneRoster specification.
- The maximum limit is 3000 items per page to prevent abuse and ensure optimal performance.
- Use the `fields` parameter to reduce response size by requesting only needed fields.
- The `filter` parameter follows the OneRoster filtering specification for complex queries.
- Required fields (`sourcedId`, `status`, `title`, `course`, `org`, `terms`) must be present in all classes.
- The `order_by` field in `TimebackQueryParams` maps to `orderBy` in the API query.
- The `fields` field accepts a string or list of strings; lists are joined with commas.

