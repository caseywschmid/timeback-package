## QTI API — Update Section

### PUT /assessment-tests/{assessmentTestIdentifier}/test-parts/{testPartIdentifier}/sections/{identifier}

- Method: PUT
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Update an existing section within a test part.

Path params:

- `assessmentTestIdentifier` (string, required): Root assessment test identifier
- `testPartIdentifier` (string, required): Parent test part identifier
- `identifier` (string, required): Section identifier

Request body:

- `identifier` (string, required): Section identifier
- `title` (string, required): Human-readable title
- `visible` (bool, optional): Whether section is visible (default: true)
- `required` (bool, optional): Whether section is required
- `fixed` (bool, optional): Whether section position is fixed
- `sequence` (int, optional): Order within parent
- `qti-assessment-item-ref` (array, optional): List of item references

Successful response (HTTP 200):

- Body: Updated section object

Error responses:

- 400/422: Request/validation → raises `RequestError`
- 401: Unauthorized → raises `AuthError`
- 404: Not Found → raises `NotFoundError`
- 429: Too Many Requests → raises `RateLimitError`
- 5xx: Server errors → raises `ServerError`

Python usage:

```python
from timeback import Timeback
from timeback.models.request import TimebackUpdateSectionRequest

client = Timeback()

# Update section title
request = TimebackUpdateSectionRequest(
    identifier="section-001",
    title="Updated Section Title",
    visible=True
)
section = client.qti.update_section(
    "test-001", "part-001", "section-001", request
)

print(f"Updated: {section.title}")

# Hide a section
request = TimebackUpdateSectionRequest(
    identifier="section-001",
    title="Hidden Section",
    visible=False
)
section = client.qti.update_section(
    "test-001", "part-001", "section-001", request
)
```

Notes:

- All required fields must be provided
- The parent assessment test's XML is automatically regenerated
- Item references can be updated to change the items in the section


