## QTI API — Get Section

### GET /assessment-tests/{assessmentTestIdentifier}/test-parts/{testPartIdentifier}/sections/{identifier}

- Method: GET
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Retrieve a specific section by identifier including all its assessment item references.

Path params:

- `assessmentTestIdentifier` (string, required): Root assessment test identifier
- `testPartIdentifier` (string, required): Parent test part identifier
- `identifier` (string, required): Section identifier

Successful response (HTTP 200):

- Body: Section object (TimebackQTISection)
- Key fields: identifier, title, visible, required, fixed, sequence, qti-assessment-item-ref

Error responses:

- 401: Unauthorized → raises `AuthError`
- 404: Not Found → raises `NotFoundError`
- 429: Too Many Requests → raises `RateLimitError`
- 5xx: Server errors → raises `ServerError`

Python usage:

```python
from timeback import Timeback

client = Timeback()

# Get a specific section
section = client.qti.get_section("test-001", "part-001", "section-001")

print(f"Section: {section.title}")
print(f"Visible: {section.visible}")

# Access item references
if section.qti_assessment_item_ref:
    print(f"Items: {len(section.qti_assessment_item_ref)}")
    for item in section.qti_assessment_item_ref:
        print(f"  - {item.identifier}: {item.href}")
```

Notes:

- Returns full section details including all item references
- Item references contain identifiers and hrefs to the actual assessment items
- Use this to inspect the contents of a specific section


