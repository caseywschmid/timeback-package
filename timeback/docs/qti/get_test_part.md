## QTI API — Get Test Part

### GET /assessment-tests/{assessmentTestIdentifier}/test-parts/{identifier}

- Method: GET
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Retrieve a specific test part by identifier including all its sections and their assessment item references.

Path params:

- `assessmentTestIdentifier` (string, required): Unique identifier of the parent assessment test
- `identifier` (string, required): Unique identifier of the test part to retrieve

Successful response (HTTP 200):

- Body: Test part object with sections
- Key fields:
  - `identifier` (string): Test part identifier
  - `navigationMode` (string): "linear" or "nonlinear"
  - `submissionMode` (string): "individual" or "simultaneous"
  - `qti-assessment-section` (array): List of sections
  - `rawXml` (string): Raw XML representation
  - `content` (object): Parsed content structure

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

# Get a specific test part
part = client.qti.get_test_part("test-001", "part-001")

print(f"Part: {part.identifier}")
print(f"Navigation: {part.navigation_mode.value}")
print(f"Submission: {part.submission_mode.value}")

# Access sections
if part.qti_assessment_section:
    for section in part.qti_assessment_section:
        print(f"  Section: {section.identifier} - {section.title}")
        if section.qti_assessment_item_ref:
            for item in section.qti_assessment_item_ref:
                print(f"    Item: {item.identifier}")

# Access raw XML
if part.raw_xml:
    print(f"XML length: {len(part.raw_xml)}")

# Check parsed content
if part.content:
    print(f"Content keys: {part.content.keys()}")
```

Notes:

- Returns full test part details including all nested sections
- Sections include their assessment item references
- Use this to inspect the structure of a specific test part
- The `rawXml` field contains the original QTI XML representation
- The `content` field contains the parsed JSON structure


