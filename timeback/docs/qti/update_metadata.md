## QTI API — Update Metadata

### POST /assessment-items/metadata

- Method: POST
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Update metadata for assessment items. This operation is used to update metadata fields for assessment items, such as resetting the human approved status.

Request body:

- `format` (string, required): Content format - `"xml"` (recommended) or `"json"`
- `xml` (string, required when format="xml"): QTI 3.0 XML content string
- `metadata` (object, optional): Metadata fields to update
  - `subject` (string): Subject area (e.g., "Math", "Science")
  - `grade` (string): Grade level ("-1" to "13")
  - `difficulty` (string): Difficulty level ("easy", "medium", "hard")
  - `learningObjectiveSet` (array): Array of learning objectives

Successful response (HTTP 201):

- Body: Updated assessment item object
- Key fields: Same as GET /assessment-items/{identifier}

Error responses:

- 400/422: Request/validation → raises `RequestError`
- 401: Unauthorized → raises `AuthError`
- 429: Too Many Requests → raises `RateLimitError`
- 5xx: Server errors → raises `ServerError`

Python usage:

```python
from timeback import Timeback
from timeback.models.request import TimebackUpdateAssessmentItemMetadataRequest

client = Timeback()

# Update metadata for an assessment item
xml_content = '''<?xml version="1.0" encoding="UTF-8"?>
<qti-assessment-item
  xmlns="http://www.imsglobal.org/xsd/imsqtiasi_v3p0"
  identifier="item-001"
  title="Math Question"
  adaptive="false"
  time-dependent="false">
  <!-- QTI content -->
</qti-assessment-item>'''

request = TimebackUpdateAssessmentItemMetadataRequest(
    format="xml",
    xml=xml_content,
    metadata={
        "subject": "Math",
        "grade": "5",
        "difficulty": "medium"
    }
)
item = client.qti.update_metadata(request)

print(f"Updated: {item.identifier}")
print(f"Metadata: {item.metadata}")

# Update with learning objectives
request = TimebackUpdateAssessmentItemMetadataRequest(
    format="xml",
    xml=xml_content,
    metadata={
        "subject": "Math",
        "learningObjectiveSet": [
            {"source": "CASE", "learningObjectiveIds": ["D1.5.6-8"]}
        ]
    }
)
item = client.qti.update_metadata(request)
```

Notes:

- This endpoint accepts the same format as create/update assessment item endpoints
- The metadata field allows updating custom metadata properties
- Commonly used for resetting human approved status or updating curriculum mappings


