## QTI API — Update Stimulus

### PUT /stimuli/{identifier}

- Method: PUT
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Update an existing stimulus on the service provider with new content.

Path parameters:

- `identifier` (string, required): Unique identifier of the stimulus to update

Request body (JSON):

Required fields:
- `identifier` (string): Must match the path parameter
- `title` (string): Human-readable title of the stimulus
- `content` (string): HTML content for the stimulus body

Optional fields:
- `label` (string): Human-readable label describing the stimulus
- `language` (string, default "en"): Language code for the content
- `stylesheet` (object): External stylesheet with `href` and `type`
- `catalogInfo` (array): Array of catalog cards for accessibility support
- `toolName` (string): Name of the tool updating the stimulus
- `toolVersion` (string): Version of the updating tool
- `metadata` (object): Additional custom metadata

Successful response (HTTP 200):

- Body: Updated stimulus object with all fields
- The `updatedAt` timestamp reflects the update time
- The `rawXml` is regenerated from the new content

Error responses:

- 400: Invalid stimulus data → raises `RequestError`
- 401: Unauthorized → raises `AuthError`
- 404: Stimulus not found → raises `NotFoundError`
- 429: Too Many Requests → raises `RateLimitError`
- 5xx: Server errors → raises `ServerError`

Python usage:

```python
from timeback import Timeback
from timeback.models.request import TimebackUpdateStimulusRequest
from timeback.models.timeback_qti_stimulus import TimebackQTIStylesheet

client = Timeback()

# Update stimulus with new content
request = TimebackUpdateStimulusRequest(
    identifier="stimulus-science-001",
    title="Updated Forest Ecosystem Reading Passage",
    content="""
    <div class="stimulus-content">
        <h2>Forest Ecosystems - Revised</h2>
        <p>This is the updated content for the reading passage.</p>
    </div>
    """
)
response = client.qti.update_stimulus(request)
print(f"Updated at: {response.updated_at}")

# Update with all optional fields
stylesheet = TimebackQTIStylesheet(href="new-styles.css", type="text/css")

request = TimebackUpdateStimulusRequest(
    identifier="stimulus-science-001",
    title="Complete Update Example",
    content="<div><h2>Title</h2><p>Content...</p></div>",
    label="Updated Science Reading",
    language="en-US",
    stylesheet=stylesheet,
    tool_name="Content Editor",
    tool_version="2.0.0",
    metadata={
        "subject": "Science",
        "grade": "8",
        "lastEditor": "curriculum-team",
        "revisionNumber": 2
    }
)
response = client.qti.update_stimulus(request)
```

Notes:

- The `identifier` in the request must match the identifier in the URL path
- All content is replaced (not merged) with the new values
- The `rawXml` is automatically regenerated from the updated content
- The `updatedAt` timestamp is automatically set to the current time
- Use `get_stimulus` after updating to verify the changes
- Empty optional fields will clear the previous values

