## OneRoster — Gradebook - Create Assessment Line Item

### POST /ims/oneroster/gradebook/v1p2/assessmentLineItems

- Method: POST
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Create a new assessment line item. Title is required.

Request body:

- `assessmentLineItem` (object, required):
  - Required: `title`, `assignDate`, `dueDate`, `class`, `school`, `category`
  - Optional: `sourcedId`, `status`, `description`, `metadata`, `scoreScale`, `resultValueMin`, `resultValueMax`, `component`, `componentResource`

Successful response (HTTP 201):

- Body: `{ "sourcedIdPairs": { "suppliedSourcedId": "...", "allocatedSourcedId": "..." } }`

Python usage:

```python
from timeback import Timeback
from timeback.models.request import TimebackCreateAssessmentLineItemRequest, TimebackCreateAssessmentLineItemBody
from timeback.models.timeback_sourced_id_ref import TimebackSourcedIdReference

client = Timeback()

body = TimebackCreateAssessmentLineItemBody(
    title="Quiz 1",
    assignDate="2024-01-01",
    dueDate="2024-01-15",
    class_=TimebackSourcedIdReference(sourcedId="<class-id>"),
    school=TimebackSourcedIdReference(sourcedId="<school-id>"),
    category=TimebackSourcedIdReference(sourcedId="<category-id>"),
)
request = TimebackCreateAssessmentLineItemRequest(assessmentLineItem=body)
response = client.oneroster.gradebook.create_assessment_line_item(request)
print(f"Created: {response.sourcedIdPairs.allocatedSourcedId}")
```

