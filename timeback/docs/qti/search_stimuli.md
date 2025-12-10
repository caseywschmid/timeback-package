## QTI API — Search Stimuli

### GET /stimuli

- Method: GET
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Search and filter stimuli with advanced filtering capabilities. Supports text search across titles and identifiers, sorting, and pagination.

Query params:

- `query` (string, optional): Fuzzy search term for title and identifier fields
- `page` (integer, optional, default 1): Page number for pagination (1-indexed)
- `limit` (integer, optional, default 10): Number of items per page
- `sort` (string, optional, enum: `title`, `identifier`, `createdAt`, `updatedAt`): Field to sort by
- `order` (string, optional, enum: `asc`, `desc`, default `desc`): Sort order

Successful response (HTTP 200):

- Body: `{ "items": [Stimulus, ...], "total": number, "page": number, "pages": number, "limit": number, "sort": string, "order": string }`
- Key fields:
  - `items`: Array of stimulus objects
  - `total`: Total count of matching stimuli
  - `page`: Current page number
  - `pages`: Total number of pages
  - `limit`: Items per page
  - `sort`: Sort field used
  - `order`: Sort order used

Stimulus object fields:

- `identifier` (string): Unique identifier for the stimulus
- `title` (string): Human-readable title
- `catalogInfo` (array): Array of catalog cards with accessibility support info
- `label` (string, optional): Human-readable label
- `language` (string, default "en"): Language code
- `stylesheet` (object, optional): External stylesheet with `href` and `type`
- `toolName` (string, optional): Tool that created the stimulus
- `toolVersion` (string, optional): Tool version
- `metadata` (object, optional): Custom metadata
- `rawXml` (string): Raw XML representation (use this for production)
- `content` (object, optional): Parsed XML content structure
- `createdAt` (datetime): Creation timestamp
- `updatedAt` (datetime): Last update timestamp

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
from timeback.models.request import TimebackSearchStimuliRequest
from timeback.enums import TimebackQTISortField, TimebackSortOrder

client = Timeback()

# Basic search with defaults
response = client.qti.search_stimuli()
print(f"Total: {response.total}, Page: {response.page}/{response.pages}")

# Search with query
request = TimebackSearchStimuliRequest(query="ecosystem")
response = client.qti.search_stimuli(request)
for stimulus in response.items:
    print(f"{stimulus.identifier}: {stimulus.title}")

# Paginated search
request = TimebackSearchStimuliRequest(page=2, limit=20)
response = client.qti.search_stimuli(request)

# Sorted search
request = TimebackSearchStimuliRequest(
    sort=TimebackQTISortField.TITLE,
    order=TimebackSortOrder.ASC,
    limit=10
)
response = client.qti.search_stimuli(request)

# Full search with all parameters
request = TimebackSearchStimuliRequest(
    query="science",
    page=1,
    limit=25,
    sort=TimebackQTISortField.UPDATED_AT,
    order=TimebackSortOrder.DESC
)
response = client.qti.search_stimuli(request)
```

Notes:

- The QTI API uses page-based pagination (page, pages) rather than offset-based pagination
- The `rawXml` field contains the complete QTI XML and is recommended for production use
- The `content` field contains parsed XML structure but may not include all XML features
- Stimuli can be shared across multiple assessment items

