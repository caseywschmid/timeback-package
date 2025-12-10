## QTI API — Get Assessment Test

### GET /assessment-tests/{identifier}

- Method: GET
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Retrieve a complete assessment test including all its test parts, sections, and assessment item references. This provides the full hierarchical structure needed to understand the test organization and flow.

Path params:

- `identifier` (string, required): Unique identifier of the assessment test

Successful response (HTTP 200):

- Body: Complete assessment test object
- Key fields:
  - `identifier` (string): Unique identifier
  - `title` (string): Human-readable title
  - `qtiVersion` (string): QTI version (default "3.0")
  - `qti-test-part` (array): Test parts containing sections and items
  - `qti-outcome-declaration` (array): Outcome variable declarations
  - `timeLimit` (number, optional): Time limit in seconds
  - `maxAttempts` (number, optional): Maximum attempts allowed
  - `toolsEnabled` (object, optional): Enabled assessment tools
  - `metadata` (object, optional): Custom metadata
  - `rawXml` (string): Raw XML representation

Error responses:

- 400/422: Request/validation → raises `RequestError`
- 401: Unauthorized → raises `AuthError`
- 404: Not Found → raises `NotFoundError`
- 429: Too Many Requests → raises `RateLimitError`
- 5xx: Server errors → raises `ServerError`

Python usage:

```python
from timeback import Timeback

client = Timeback()

# Get a specific assessment test
test = client.qti.get_assessment_test("test-001")

print(f"Identifier: {test.identifier}")
print(f"Title: {test.title}")
print(f"QTI Version: {test.qti_version}")

# Access test parts
if test.qti_test_part:
    for part in test.qti_test_part:
        print(f"Part: {part.identifier}")
        print(f"  Navigation: {part.navigation_mode}")
        print(f"  Submission: {part.submission_mode}")

# Access time limit
if test.time_limit:
    print(f"Time limit: {test.time_limit} seconds")

# Access metadata
if test.metadata:
    print(f"Metadata: {test.metadata}")

# Access raw XML for production use
print(test.raw_xml)
```

Notes:

- The `rawXml` field contains the complete QTI XML and is recommended for production use
- Assessment tests contain a hierarchical structure: test → test parts → sections → item references
- The actual assessment items are referenced by identifier but not included inline


