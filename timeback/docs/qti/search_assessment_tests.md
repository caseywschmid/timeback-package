## QTI API — Search Assessment Tests

### GET /assessment-tests

- Method: GET
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Search and retrieve assessment tests with advanced filtering capabilities. Supports text search across titles and identifiers, filtering by navigation/submission modes, and pagination. Assessment tests are the top-level containers that define complete testing experiences through their test parts and sections.

Query params:

- `query` (string, optional): Fuzzy search term for title and identifier fields
- `page` (integer, optional, default 1): Page number for pagination (1-indexed)
- `limit` (integer, optional, default 10): Number of items per page
- `sort` (string, optional, enum: `title`, `identifier`, `createdAt`, `updatedAt`): Field to sort by
- `order` (string, optional, enum: `asc`, `desc`, default `desc`): Sort order
- `navigationMode` (string, optional, enum: `linear`, `nonlinear`): Filter by navigation mode
- `submissionMode` (string, optional, enum: `individual`, `simultaneous`): Filter by submission mode
- `filter` (string, optional): Advanced filter expression using =, !=, >, >=, <, <=, ~ and logical AND/OR

Successful response (HTTP 200):

- Body: `{ "items": [AssessmentTest, ...], "total": number, "page": number, "pages": number, "limit": number, "sort": string, "order": string }`
- Key fields:
  - `items`: Array of assessment test objects
  - `total`: Total count of matching tests
  - `page`: Current page number
  - `pages`: Total number of pages
  - `limit`: Items per page
  - `sort`: Sort field used
  - `order`: Sort order used

Assessment Test object fields:

- `identifier` (string): Unique identifier for the test
- `title` (string): Human-readable title
- `qtiVersion` (string): QTI version (default "3.0")
- `qti-test-part` (array): Test parts containing sections and items
- `qti-outcome-declaration` (array): Outcome variable declarations
- `timeLimit` (number, optional): Time limit in seconds
- `maxAttempts` (number, optional): Maximum attempts allowed
- `toolsEnabled` (object, optional): Enabled assessment tools
- `metadata` (object, optional): Custom metadata
- `rawXml` (string): Raw XML representation
- `content` (object, optional): Parsed XML content structure
- `createdAt` (datetime): Creation timestamp
- `updatedAt` (datetime): Last update timestamp

Error responses:

- 400/422: Request/validation → raises `RequestError`
- 401: Unauthorized → raises `AuthError`
- 429: Too Many Requests → raises `RateLimitError`
- 5xx: Server errors → raises `ServerError`

Python usage:

```python
from timeback import Timeback
from timeback.models.request import TimebackSearchAssessmentTestsRequest
from timeback.enums import (
    TimebackQTIAssessmentTestSortField,
    TimebackSortOrder,
    TimebackQTINavigationMode,
    TimebackQTISubmissionMode,
)

client = Timeback()

# Basic search with defaults
response = client.qti.search_assessment_tests()
print(f"Total: {response.total}, Page: {response.page}/{response.pages}")

# Search with query
request = TimebackSearchAssessmentTestsRequest(query="math")
response = client.qti.search_assessment_tests(request)
for test in response.items:
    print(f"{test.identifier}: {test.title}")

# Filter by navigation mode (linear = sequential, nonlinear = free navigation)
request = TimebackSearchAssessmentTestsRequest(
    navigation_mode=TimebackQTINavigationMode.LINEAR
)
response = client.qti.search_assessment_tests(request)

# Filter by submission mode (individual = per item, simultaneous = all at once)
request = TimebackSearchAssessmentTestsRequest(
    submission_mode=TimebackQTISubmissionMode.INDIVIDUAL
)
response = client.qti.search_assessment_tests(request)

# Paginated search
request = TimebackSearchAssessmentTestsRequest(page=2, limit=20)
response = client.qti.search_assessment_tests(request)

# Sorted search
request = TimebackSearchAssessmentTestsRequest(
    sort=TimebackQTIAssessmentTestSortField.TITLE,
    order=TimebackSortOrder.ASC,
    limit=10
)
response = client.qti.search_assessment_tests(request)

# Full search with all parameters
request = TimebackSearchAssessmentTestsRequest(
    query="algebra",
    page=1,
    limit=25,
    sort=TimebackQTIAssessmentTestSortField.CREATED_AT,
    order=TimebackSortOrder.DESC,
    navigation_mode=TimebackQTINavigationMode.LINEAR,
    submission_mode=TimebackQTISubmissionMode.INDIVIDUAL,
    filter="type='practice'"
)
response = client.qti.search_assessment_tests(request)
```

Notes:

- Assessment tests contain test parts, which contain sections, which contain assessment item references
- Navigation mode controls how candidates move through the test (linear = in order, nonlinear = any order)
- Submission mode controls when responses are submitted (individual = after each item, simultaneous = at the end)
- The `rawXml` field contains the complete QTI XML and is recommended for production use
- The QTI API uses page-based pagination (page, pages) rather than offset-based pagination


