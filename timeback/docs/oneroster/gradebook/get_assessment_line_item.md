## OneRoster — Gradebook - Get Assessment Line Item

### GET /ims/oneroster/gradebook/v1p2/assessmentLineItems/{sourcedId}

- Method: GET
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Get a single assessment line item by sourcedId.

Path params:

- `sourcedId` (string, required): The assessment line item's sourcedId

Query params:

- `fields` (string, optional): Comma-separated list of fields to include

Successful response (HTTP 200):

- Body: `{ "assessmentLineItem": LineItem }`

Python usage:

```python
from timeback import Timeback
from timeback.models.request import TimebackGetAssessmentLineItemRequest

client = Timeback()

request = TimebackGetAssessmentLineItemRequest(sourced_id="<sourcedId>")
response = client.oneroster.gradebook.get_assessment_line_item(request)
print(f"Title: {response.assessmentLineItem.title}")
```

