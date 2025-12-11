## QTI API — Search Test Parts

### GET /assessment-tests/{assessmentTestIdentifier}/test-parts

- Method: GET
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Search and filter test parts within an assessment test. Test parts are organizational units that group sections and define testing behaviors like linear/nonlinear navigation.

Path params:

- `assessmentTestIdentifier` (string, required): Unique identifier of the parent assessment test

Query params (all optional):

- `query` (string): Fuzzy search on title and identifier fields
- `page` (int): Page number for pagination (default: 1)
- `limit` (int): Number of items per page (default: 10, max: 3000)
- `sort` (string): Field to sort by
- `order` (string): Sort order - "asc" or "desc" (default: desc)
- `navigationMode` (string): Filter by navigation mode - "linear" or "nonlinear"
- `submissionMode` (string): Filter by submission mode - "individual" or "simultaneous"
- `filter` (string): Advanced filter expression

Successful response (HTTP 200):

- Body: `{ "items": [...], "total": number, "page": number, "pages": number, "limit": number, "sort": string, "order": string }`
- `items` contains TimebackQTITestPart objects with:
  - `identifier` (string): Unique identifier
  - `navigationMode` (string): "linear" or "nonlinear"
  - `submissionMode` (string): "individual" or "simultaneous"
  - `qti-assessment-section` (array): List of sections in this part

Error responses:

- 400/422: Request/validation → raises `RequestError`
- 401: Unauthorized → raises `AuthError`
- 404: Not Found → raises `NotFoundError`
- 429: Too Many Requests → raises `RateLimitError`
- 5xx: Server errors → raises `ServerError`

Python usage:

```python
from timeback import Timeback
from timeback.models.request import TimebackSearchTestPartsRequest
from timeback.enums import TimebackQTINavigationMode, TimebackQTISubmissionMode

client = Timeback()

# Search all test parts in an assessment test
response = client.qti.search_test_parts("test-001")

print(f"Found {response.total} test parts")
for part in response.items:
    print(f"  {part.identifier}: {part.navigation_mode.value}")

# Filter by navigation mode
request = TimebackSearchTestPartsRequest(
    navigation_mode=TimebackQTINavigationMode.LINEAR
)
response = client.qti.search_test_parts("test-001", request)

# Filter by submission mode
request = TimebackSearchTestPartsRequest(
    submission_mode=TimebackQTISubmissionMode.SIMULTANEOUS
)
response = client.qti.search_test_parts("test-001", request)

# Pagination and sorting
request = TimebackSearchTestPartsRequest(
    page=2,
    limit=20,
    sort="identifier",
    order=TimebackSortOrder.ASC
)
response = client.qti.search_test_parts("test-001", request)

# Combined filters
request = TimebackSearchTestPartsRequest(
    navigation_mode=TimebackQTINavigationMode.LINEAR,
    submission_mode=TimebackQTISubmissionMode.INDIVIDUAL,
    limit=50
)
response = client.qti.search_test_parts("test-001", request)
```

Notes:

- Test parts define the major divisions within an assessment test
- Navigation mode controls how learners move through items (linear = sequential, nonlinear = free)
- Submission mode controls when responses are submitted (individual = per item, simultaneous = all at once)
- Each test part contains one or more sections, which in turn contain item references


