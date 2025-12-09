## OneRoster — Gradebook - Put Assessment Line Item

### PUT /ims/oneroster/gradebook/v1p2/assessmentLineItems/{sourcedId}

- Method: PUT
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Update or create an assessment line item by sourcedId.

Path params:

- `sourcedId` (string, required): The assessment line item's sourcedId

Request body:

- `assessmentLineItem` (object, required): Full assessment line item data
  - Required: `title`, `assignDate`, `dueDate`, `class`, `school`, `category`

Successful response (HTTP 201):

- Body: `{ "assessmentLineItem": LineItem }`

Python usage:

```python
from timeback import Timeback
from timeback.models.request import TimebackPutAssessmentLineItemRequest, TimebackPutAssessmentLineItemBody
from timeback.models.timeback_sourced_id_ref import TimebackSourcedIdReference

client = Timeback()

body = TimebackPutAssessmentLineItemBody(
    title="Updated Quiz",
    assignDate="2024-01-01",
    dueDate="2024-01-20",
    class_=TimebackSourcedIdReference(sourcedId="<class-id>"),
    school=TimebackSourcedIdReference(sourcedId="<school-id>"),
    category=TimebackSourcedIdReference(sourcedId="<category-id>"),
)
request = TimebackPutAssessmentLineItemRequest(sourced_id="<sourcedId>", assessmentLineItem=body)
response = client.oneroster.gradebook.put_assessment_line_item(request)
```

