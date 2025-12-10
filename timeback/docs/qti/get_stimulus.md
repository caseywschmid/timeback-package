## QTI API — Get Stimulus

### GET /stimuli/{identifier}

- Method: GET
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Get a specific stimulus by identifier from the service provider. Returns the complete stimulus data including the raw XML representation.

Path parameters:

- `identifier` (string, required): Unique identifier of the stimulus to retrieve

Successful response (HTTP 200):

- Body: Complete stimulus object with all fields
- Key fields:
  - `identifier`: Unique identifier
  - `title`: Human-readable title
  - `catalogInfo`: Array of accessibility catalog cards
  - `label`: Optional human-readable label
  - `language`: Language code (default: "en")
  - `stylesheet`: Optional external stylesheet reference
  - `toolName`: Tool that created the stimulus
  - `toolVersion`: Version of the creating tool
  - `metadata`: Custom metadata object
  - `rawXml`: Complete QTI XML representation (use this for production)
  - `content`: Parsed XML content structure
  - `createdAt`: Creation timestamp
  - `updatedAt`: Last update timestamp

Error responses:

- 401: Unauthorized → raises `AuthError`
- 404: Stimulus not found → raises `NotFoundError`
- 429: Too Many Requests → raises `RateLimitError`
- 5xx: Server errors → raises `ServerError`

Python usage:

```python
from timeback import Timeback

client = Timeback()

# Get a stimulus by identifier
stimulus = client.qti.get_stimulus("stimulus-science-001")

# Access stimulus properties
print(f"Title: {stimulus.title}")
print(f"Language: {stimulus.language}")
print(f"Created: {stimulus.created_at}")

# Use the raw XML for rendering or processing
raw_xml = stimulus.raw_xml
print(f"XML length: {len(raw_xml)} characters")

# Access metadata if present
if stimulus.metadata:
    print(f"Subject: {stimulus.metadata.get('subject')}")
    print(f"Grade: {stimulus.metadata.get('grade')}")

# Check for accessibility catalog info
for entry in stimulus.catalog_info:
    print(f"Support type: {entry.support}")
    print(f"Content: {entry.content}")

# Access stylesheet if present
if stimulus.stylesheet:
    print(f"Stylesheet: {stimulus.stylesheet.href}")
```

Notes:

- The `rawXml` field contains the complete QTI XML and should be used for production rendering
- The `content` field is a parsed representation but may not include all XML features
- Use this endpoint to fetch the complete stimulus data before displaying it to learners
- The identifier is case-sensitive and must match exactly
- Stimuli can be referenced by assessment items using their identifier

