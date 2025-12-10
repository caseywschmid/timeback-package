## QTI API — Update Assessment Test

### PUT /assessment-tests/{identifier}

- Method: PUT
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Update an entire assessment test by replacing its complete structure. This operation updates the test including its test parts, sections, and item references. The updated XML structure is automatically regenerated.

Path params:

- `identifier` (string, required): Unique identifier of the assessment test to update

Request body:

- `format` (string, required): Content format - `"xml"` (recommended) or `"json"`
- `xml` (string, required when format="xml"): Updated QTI 3.0 XML content string
- `metadata` (object, optional): Updated custom metadata

Successful response (HTTP 200):

- Body: Updated assessment test object
- Key fields: Same as GET /assessment-tests/{identifier}

Error responses:

- 400/422: Request/validation → raises `RequestError`
- 401: Unauthorized → raises `AuthError`
- 404: Not Found → raises `NotFoundError`
- 429: Too Many Requests → raises `RateLimitError`
- 5xx: Server errors → raises `ServerError`

Python usage:

```python
from timeback import Timeback
from timeback.models.request import TimebackUpdateAssessmentTestRequest

client = Timeback()

# Updated QTI XML content
updated_xml = '''<?xml version="1.0" encoding="UTF-8"?>
<qti-assessment-test
  xmlns="http://www.imsglobal.org/xsd/imsqtiasi_v3p0"
  identifier="math-test-001"
  title="Updated Math Assessment"
  tool-name="Timeback"
  tool-version="1.0">
  <qti-test-part identifier="part-1" navigation-mode="nonlinear" submission-mode="simultaneous">
    <qti-assessment-section identifier="section-1" title="Updated Section" visible="true">
      <qti-assessment-item-ref identifier="item-ref-1" href="/assessment-items/item-001"/>
      <qti-assessment-item-ref identifier="item-ref-2" href="/assessment-items/item-002"/>
      <qti-assessment-item-ref identifier="item-ref-3" href="/assessment-items/item-003"/>
    </qti-assessment-section>
  </qti-test-part>
</qti-assessment-test>'''

# Update with new content and metadata
request = TimebackUpdateAssessmentTestRequest(
    format="xml",
    xml=updated_xml,
    metadata={
        "subject": "Math",
        "grade": "6",
        "version": "2.0"
    }
)
test = client.qti.update_assessment_test("math-test-001", request)

print(f"Updated: {test.identifier}")
print(f"New title: {test.title}")

# Update without metadata changes
request_simple = TimebackUpdateAssessmentTestRequest(
    format="xml",
    xml=updated_xml
)
test = client.qti.update_assessment_test("math-test-001", request_simple)
```

Notes:

- This replaces the entire test structure, not a partial update
- All test parts, sections, and item references are replaced
- The `rawXml` field in the response contains the regenerated XML
- Assessment item references must point to existing assessment items


