## QTI API — Create Assessment Item

### POST /assessment-items

- Method: POST
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Create a QTI 3.0 assessment item, preferably from XML. The XML is validated against IMS QTI XSDs and must conform to the standard. JSON creation is also supported but is experimental.

Request body:

- `format` (string, required): Content format - `"xml"` (recommended) or `"json"`
- `xml` (string, required when format="xml"): QTI 3.0 XML content string
- `metadata` (object, optional): Custom metadata for the assessment item
  - `subject` (string): Subject area (e.g., "Math", "Science")
  - `grade` (string): Grade level ("-1" to "13", where -1 is Pre-K)
  - `difficulty` (string): Difficulty level ("easy", "medium", "hard")
  - `learningObjectiveSet` (array): Array of learning objectives

Successful response (HTTP 201):

- Body: Created assessment item object
- Key fields: Same as GET /assessment-items/{identifier}

Error responses:

- 400/422: Request/validation → raises `RequestError`
- 401: Unauthorized → raises `AuthError`
- 429: Too Many Requests → raises `RateLimitError`
- 5xx: Server errors → raises `ServerError`

Python usage:

```python
from timeback import Timeback
from timeback.models.request import TimebackCreateAssessmentItemRequest

client = Timeback()

# QTI 3.0 XML content
xml_content = '''<?xml version="1.0" encoding="UTF-8"?>
<qti-assessment-item
  xmlns="http://www.imsglobal.org/xsd/imsqtiasi_v3p0"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  identifier="math-addition-001"
  title="Basic Addition Question"
  adaptive="false"
  time-dependent="false">
  <qti-response-declaration identifier="RESPONSE" cardinality="single" base-type="identifier">
    <qti-correct-response>
      <qti-value>B</qti-value>
    </qti-correct-response>
  </qti-response-declaration>
  <qti-outcome-declaration identifier="SCORE" cardinality="single" base-type="float"/>
  <qti-item-body>
    <qti-choice-interaction response-identifier="RESPONSE" max-choices="1">
      <qti-prompt>What is 2 + 2?</qti-prompt>
      <qti-simple-choice identifier="A">3</qti-simple-choice>
      <qti-simple-choice identifier="B">4</qti-simple-choice>
      <qti-simple-choice identifier="C">5</qti-simple-choice>
    </qti-choice-interaction>
  </qti-item-body>
  <qti-response-processing template="match_correct"/>
</qti-assessment-item>'''

# Create with metadata
request = TimebackCreateAssessmentItemRequest(
    format="xml",
    xml=xml_content,
    metadata={
        "subject": "Math",
        "grade": "5",
        "difficulty": "easy"
    }
)
item = client.qti.create_assessment_item(request)

print(f"Created: {item.identifier}")
print(f"Title: {item.title}")
print(f"Type: {item.type}")

# Create without metadata
request_simple = TimebackCreateAssessmentItemRequest(
    format="xml",
    xml=xml_content
)
item_simple = client.qti.create_assessment_item(request_simple)
```

Notes:

- XML format is strongly recommended for production use
- The XML must validate against IMS QTI 3.0 XSDs
- JSON creation is experimental and the API may change
- The response includes the generated `rawXml` field with the validated XML


