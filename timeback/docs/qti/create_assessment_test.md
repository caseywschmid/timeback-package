## QTI API — Create Assessment Test

### POST /assessment-tests

- Method: POST
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Create a new QTI assessment test. Supports both JSON and XML formats. The recommended approach is to send format='xml' with QTI XML content.

Request body:

- `format` (string, required): Content format - `"xml"` (recommended) or `"json"`
- `xml` (string, required when format="xml"): QTI 3.0 XML content string
- `metadata` (object, optional): Custom metadata for the assessment test

Successful response (HTTP 201):

- Body: Created assessment test object
- Key fields: Same as GET /assessment-tests/{identifier}

Error responses:

- 400/422: Request/validation → raises `RequestError`
- 401: Unauthorized → raises `AuthError`
- 429: Too Many Requests → raises `RateLimitError`
- 5xx: Server errors → raises `ServerError`

Python usage:

```python
from timeback import Timeback
from timeback.models.request import TimebackCreateAssessmentTestRequest

client = Timeback()

# QTI 3.0 XML content
xml_content = '''<?xml version="1.0" encoding="UTF-8"?>
<qti-assessment-test
  xmlns="http://www.imsglobal.org/xsd/imsqtiasi_v3p0"
  identifier="math-test-001"
  title="Math Assessment"
  tool-name="Timeback"
  tool-version="1.0">
  <qti-outcome-declaration identifier="SCORE" cardinality="single" base-type="float">
    <qti-default-value>
      <qti-value>0</qti-value>
    </qti-default-value>
  </qti-outcome-declaration>
  <qti-test-part identifier="part-1" navigation-mode="linear" submission-mode="individual">
    <qti-assessment-section identifier="section-1" title="Section 1" visible="true">
      <qti-assessment-item-ref identifier="item-ref-1" href="/assessment-items/item-001"/>
      <qti-assessment-item-ref identifier="item-ref-2" href="/assessment-items/item-002"/>
    </qti-assessment-section>
  </qti-test-part>
</qti-assessment-test>'''

# Create with metadata
request = TimebackCreateAssessmentTestRequest(
    format="xml",
    xml=xml_content,
    metadata={
        "subject": "Math",
        "grade": "5",
        "type": "practice"
    }
)
test = client.qti.create_assessment_test(request)

print(f"Created: {test.identifier}")
print(f"Title: {test.title}")

# Create without metadata
request_simple = TimebackCreateAssessmentTestRequest(
    format="xml",
    xml=xml_content
)
test_simple = client.qti.create_assessment_test(request_simple)
```

Notes:

- XML format is strongly recommended for production use
- Assessment item references must point to existing assessment items
- The response includes the generated `rawXml` field with the validated XML
- Test parts can be configured with different navigation and submission modes


