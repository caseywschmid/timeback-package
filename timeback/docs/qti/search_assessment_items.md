## QTI API — Search Assessment Items

### GET /assessment-items

- Method: GET
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Search and filter assessment items with advanced filtering capabilities. Supports text search across titles and identifiers, filtering by type, sorting, and pagination.

Query params:

- `query` (string, optional): Search term for fuzzy matching on title and identifier fields
- `page` (integer, optional, default 1): Page number for pagination (1-indexed)
- `limit` (integer, optional, default 10): Number of items per page
- `sort` (string, optional, enum: `title`, `identifier`, `type`, `createdAt`, `updatedAt`): Field to sort by
- `order` (string, optional, enum: `asc`, `desc`, default `desc`): Sort order
- `filter` (string, optional): Advanced filter expression using =, !=, >, >=, <, <=, ~ and logical AND/OR. Example: `type='choice'`

Successful response (HTTP 200):

- Body: `{ "items": [AssessmentItem, ...], "total": number, "page": number, "pages": number, "limit": number, "sort": string, "order": string }`
- Key fields:
  - `items`: Array of assessment item objects
  - `total`: Total count of matching items
  - `page`: Current page number
  - `pages`: Total number of pages

Assessment Item fields:

- `identifier` (string): Unique identifier
- `title` (string): Human-readable title
- `type` (string): Interaction type (choice, text-entry, extended-text, etc.)
- `qtiVersion` (string): QTI version (default: "3.0")
- `timeDependent` (boolean): Whether timing affects scoring
- `adaptive` (boolean): Whether item adapts to responses
- `responseDeclarations` (array): Response variable definitions
- `outcomeDeclarations` (array): Outcome variable definitions
- `responseProcessing` (object): Scoring/feedback logic
- `metadata` (object): Custom metadata (subject, grade, difficulty, etc.)
- `rawXml` (string): Complete QTI XML representation

Error responses:

- 400/422: Request/validation → raises `RequestError`
- 401: Unauthorized → raises `AuthError`
- 429: Too Many Requests → raises `RateLimitError`
- 5xx: Server errors → raises `ServerError`

Python usage:

```python
from timeback import Timeback
from timeback.models.request import TimebackSearchAssessmentItemsRequest
from timeback.enums import TimebackQTIAssessmentItemSortField, TimebackSortOrder

client = Timeback()

# Basic search with defaults
response = client.qti.search_assessment_items()
print(f"Total: {response.total}, Page: {response.page}/{response.pages}")

# Search with query
request = TimebackSearchAssessmentItemsRequest(query="multiplication")
response = client.qti.search_assessment_items(request)
for item in response.items:
    print(f"{item.identifier}: {item.title} [{item.type}]")

# Filter by type
request = TimebackSearchAssessmentItemsRequest(filter="type='choice'")
response = client.qti.search_assessment_items(request)

# Paginated search
request = TimebackSearchAssessmentItemsRequest(page=2, limit=20)
response = client.qti.search_assessment_items(request)

# Sorted search
request = TimebackSearchAssessmentItemsRequest(
    sort=TimebackQTIAssessmentItemSortField.TITLE,
    order=TimebackSortOrder.ASC,
    limit=10
)
response = client.qti.search_assessment_items(request)

# Full search with all parameters
request = TimebackSearchAssessmentItemsRequest(
    query="algebra",
    page=1,
    limit=25,
    sort=TimebackQTIAssessmentItemSortField.CREATED_AT,
    order=TimebackSortOrder.DESC,
    filter="type='choice' AND metadata.difficulty='medium'"
)
response = client.qti.search_assessment_items(request)
```

Notes:

- The QTI API uses page-based pagination (page, pages) rather than offset-based pagination
- The `filter` parameter supports complex expressions for advanced querying
- Item types include: choice, text-entry, extended-text, inline-choice, match, order, associate, select-point, graphic-order, graphic-associate, graphic-gap-match, hotspot, hottext, slider, drawing, media, upload
- The `rawXml` field contains the complete QTI XML and is recommended for production use

