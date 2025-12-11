## QTI API — Create Section

### POST /assessment-tests/{assessmentTestIdentifier}/test-parts/{testPartIdentifier}/sections

- Method: POST
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Create a new section within a test part. Sections organize assessment items and define their presentation behavior. The parent assessment test's XML is automatically updated.

Path params:

- `assessmentTestIdentifier` (string, required): Root assessment test identifier
- `testPartIdentifier` (string, required): Parent test part identifier

Request body:

- `identifier` (string, required): Unique identifier for the section
- `title` (string, required): Human-readable title
- `visible` (bool, optional): Whether section is visible (default: true)
- `required` (bool, optional): Whether section is required
- `fixed` (bool, optional): Whether section position is fixed
- `sequence` (int, optional): Order within parent
- `qti-assessment-item-ref` (array, optional): List of item references

Successful response (HTTP 201):

- Body: Created section object (same as TimebackQTISection)

Error responses:

- 400/422: Request/validation → raises `RequestError`
- 401: Unauthorized → raises `AuthError`
- 404: Not Found → raises `NotFoundError`
- 429: Too Many Requests → raises `RateLimitError`
- 5xx: Server errors → raises `ServerError`

Python usage:

```python
from timeback import Timeback
from timeback.models.request import TimebackCreateSectionRequest
from timeback.models.timeback_qti_item_ref import TimebackQTIItemRef

client = Timeback()

# Create a basic section
request = TimebackCreateSectionRequest(
    identifier="section-001",
    title="Introduction"
)
section = client.qti.create_section("test-001", "part-001", request)

print(f"Created: {section.identifier}")

# Create a section with item references
request = TimebackCreateSectionRequest(
    identifier="section-002",
    title="Questions",
    visible=True,
    qti_assessment_item_ref=[
        TimebackQTIItemRef(
            identifier="item-001",
            href="/assessment-items/item-001"
        ),
        TimebackQTIItemRef(
            identifier="item-002",
            href="/assessment-items/item-002"
        ),
    ]
)
section = client.qti.create_section("test-001", "part-001", request)

# Create a hidden section
request = TimebackCreateSectionRequest(
    identifier="section-hidden",
    title="Hidden Section",
    visible=False,
    fixed=True
)
section = client.qti.create_section("test-001", "part-001", request)
```

Notes:

- Each section must have a unique identifier within the test part
- The parent assessment test's XML is automatically regenerated
- Use `visible=False` to hide sections from candidates
- Item references link to existing assessment items


