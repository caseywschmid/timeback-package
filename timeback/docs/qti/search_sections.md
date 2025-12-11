## QTI API — Search Sections

### GET /assessment-tests/{assessmentTestIdentifier}/test-parts/{testPartIdentifier}/sections

- Method: GET
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Search and filter sections within a test part. Sections are containers that group related assessment items and define their presentation order.

Path params:

- `assessmentTestIdentifier` (string, required): Root assessment test identifier
- `testPartIdentifier` (string, required): Parent test part identifier

Query params (all optional):

- `query` (string): Fuzzy search on title and identifier fields
- `page` (int): Page number for pagination (default: 1)
- `limit` (int): Number of items per page (default: 10, max: 3000)
- `sort` (string): Field to sort by
- `order` (string): Sort order - "asc" or "desc" (default: desc)

Successful response (HTTP 200):

- Body: `{ "items": [...], "total": number, "page": number, "pages": number, "limit": number, "sort": string, "order": string }`
- `items` contains TimebackQTISection objects with:
  - `identifier` (string): Unique identifier
  - `title` (string): Human-readable title
  - `visible` (bool): Whether section is visible to candidates
  - `required` (bool): Whether section is required
  - `fixed` (bool): Whether section position is fixed
  - `sequence` (int): Order within parent
  - `qti-assessment-item-ref` (array): List of item references

Error responses:

- 400/422: Request/validation → raises `RequestError`
- 401: Unauthorized → raises `AuthError`
- 404: Not Found → raises `NotFoundError`
- 429: Too Many Requests → raises `RateLimitError`
- 5xx: Server errors → raises `ServerError`

Python usage:

```python
from timeback import Timeback
from timeback.models.request import TimebackSearchSectionsRequest

client = Timeback()

# Search all sections in a test part
response = client.qti.search_sections("test-001", "part-001")

print(f"Found {response.total} sections")
for section in response.items:
    print(f"  {section.identifier}: {section.title}")
    if section.qti_assessment_item_ref:
        print(f"    Items: {len(section.qti_assessment_item_ref)}")

# Search with query
request = TimebackSearchSectionsRequest(query="introduction")
response = client.qti.search_sections("test-001", "part-001", request)

# Pagination
request = TimebackSearchSectionsRequest(page=2, limit=20)
response = client.qti.search_sections("test-001", "part-001", request)

# Get all sections with their items
response = client.qti.search_sections("test-001", "part-001")
for section in response.items:
    print(f"Section: {section.title}")
    for item in section.qti_assessment_item_ref or []:
        print(f"  - {item.identifier}")
```

Notes:

- Sections are containers for grouping assessment items
- Each section belongs to exactly one test part
- Sections define presentation order via the `sequence` field
- Use `visible=False` to hide sections from candidates
- Item references link to assessment items in the `assessment-items` collection


