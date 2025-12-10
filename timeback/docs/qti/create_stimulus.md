## QTI API — Create Stimulus

### POST /stimuli

- Method: POST
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Create a new stimulus on the service provider. Stimuli are shared content pieces that can be referenced by multiple assessment items.

Request body (JSON):

Required fields:
- `identifier` (string): Unique identifier for the stimulus
- `title` (string): Human-readable title of the stimulus
- `content` (string): HTML content for the stimulus body

Optional fields:
- `format` (string, default "json"): Format type ('json' or 'xml')
- `xml` (string): Raw QTI XML content (required when format='xml')
- `label` (string): Human-readable label describing the stimulus
- `language` (string, default "en"): Language code for the content
- `stylesheet` (object): External stylesheet with `href` and `type`
- `catalogInfo` (array): Array of catalog cards for accessibility support
- `toolName` (string): Name of the tool creating the stimulus
- `toolVersion` (string): Version of the creating tool
- `metadata` (object): Additional custom metadata

Successful response (HTTP 201):

- Body: Complete stimulus object with server-generated fields
- Includes all provided fields plus:
  - `rawXml`: Auto-generated QTI XML representation
  - `content`: Parsed XML content structure
  - `createdAt`: Creation timestamp
  - `updatedAt`: Last update timestamp

Error responses:

- 400: Invalid stimulus data → raises `RequestError`
- 401: Unauthorized → raises `AuthError`
- 409: Stimulus with this identifier already exists → raises `RequestError`
- 429: Too Many Requests → raises `RateLimitError`
- 5xx: Server errors → raises `ServerError`

Python usage:

```python
from timeback import Timeback
from timeback.models.request import TimebackCreateStimulusRequest
from timeback.models.timeback_qti_stimulus import TimebackQTIStylesheet
from timeback.models.timeback_catalog_entry import TimebackCatalogEntry

client = Timeback()

# Minimal creation with required fields only
request = TimebackCreateStimulusRequest(
    identifier="stimulus-science-001",
    title="Forest Ecosystem Reading Passage",
    content="""
    <div class="stimulus-content">
        <h2>Forest Ecosystems</h2>
        <p>A forest ecosystem is a complex community of plants, animals,
        and microorganisms that interact with each other.</p>
    </div>
    """
)
response = client.qti.create_stimulus(request)
print(f"Created: {response.identifier}")
print(f"Raw XML: {response.raw_xml[:100]}...")

# Creation with all optional fields
stylesheet = TimebackQTIStylesheet(href="styles.css", type="text/css")
catalog_entry = TimebackCatalogEntry(
    id="spoken-1",
    support="spoken",
    content="<p>Audio narration of the passage</p>"
)

request = TimebackCreateStimulusRequest(
    identifier="stimulus-science-002",
    title="Complete Stimulus Example",
    content="<div><h2>Title</h2><p>Content...</p></div>",
    label="Science Reading Passage",
    language="en-US",
    stylesheet=stylesheet,
    catalog_info=[catalog_entry],
    tool_name="My Assessment Tool",
    tool_version="1.0.0",
    metadata={
        "subject": "Science",
        "grade": "7",
        "standard": "NGSS",
        "difficulty": "medium"
    }
)
response = client.qti.create_stimulus(request)
```

Notes:

- The `identifier` must be unique across all stimuli in the system
- The `content` field accepts HTML that will be wrapped in `qti-stimulus-body`
- The server generates `rawXml` from the provided content automatically
- Use `catalogInfo` to provide accessibility accommodations (e.g., spoken versions)
- The `metadata` field can store arbitrary key-value pairs for curriculum alignment
- Stimuli can be referenced by assessment items using their identifier

