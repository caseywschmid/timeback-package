## QTI API — Update Assessment Item

### PUT /assessment-items/{identifier}

- Method: PUT
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Update an assessment item including its question content, interactions, response processing, and scoring logic. This operation regenerates the QTI XML structure and validates all content.

Path params:

- `identifier` (string, required): Unique identifier of the assessment item to update

Request body:

- `format` (string, required): Content format - `"xml"` (recommended) or `"json"`
- `xml` (string, required when format="xml"): Updated QTI 3.0 XML content string
- `metadata` (object, optional): Updated custom metadata

Successful response (HTTP 200):

- Body: Updated assessment item object
- Key fields: Same as GET /assessment-items/{identifier}

Error responses:

- 400/422: Request/validation → raises `RequestError`
- 401: Unauthorized → raises `AuthError`
- 404: Not Found → raises `NotFoundError`
- 429: Too Many Requests → raises `RateLimitError`
- 5xx: Server errors → raises `ServerError`

Python usage:

```python
from timeback import Timeback
from timeback.models.request import TimebackUpdateAssessmentItemRequest

client = Timeback()

# Updated QTI XML content
updated_xml = '''<?xml version="1.0" encoding="UTF-8"?>
<qti-assessment-item
  xmlns="http://www.imsglobal.org/xsd/imsqtiasi_v3p0"
  identifier="math-addition-001"
  title="Updated Addition Question"
  adaptive="false"
  time-dependent="false">
  <qti-response-declaration identifier="RESPONSE" cardinality="single" base-type="identifier">
    <qti-correct-response>
      <qti-value>C</qti-value>
    </qti-correct-response>
  </qti-response-declaration>
  <qti-item-body>
    <qti-choice-interaction response-identifier="RESPONSE" max-choices="1">
      <qti-prompt>What is 3 + 3?</qti-prompt>
      <qti-simple-choice identifier="A">5</qti-simple-choice>
      <qti-simple-choice identifier="B">7</qti-simple-choice>
      <qti-simple-choice identifier="C">6</qti-simple-choice>
    </qti-choice-interaction>
  </qti-item-body>
  <qti-response-processing template="match_correct"/>
</qti-assessment-item>'''

# Update with new content and metadata
request = TimebackUpdateAssessmentItemRequest(
    format="xml",
    xml=updated_xml,
    metadata={
        "subject": "Math",
        "grade": "6",
        "difficulty": "medium"
    }
)
item = client.qti.update_assessment_item("math-addition-001", request)

print(f"Updated: {item.identifier}")
print(f"New title: {item.title}")

# Update metadata only (content unchanged)
request_metadata = TimebackUpdateAssessmentItemRequest(
    format="xml",
    xml=existing_xml,  # Original XML
    metadata={"difficulty": "hard"}
)
item = client.qti.update_assessment_item("math-addition-001", request_metadata)
```

Notes:

- Assessment tests that reference this item will automatically use the updated version
- The XML is re-validated against IMS QTI XSDs on update
- The `rawXml` field in the response contains the regenerated XML


