## OneRoster — Gradebook - Patch Assessment Line Item

### PATCH /ims/oneroster/gradebook/v1p2/assessmentLineItems/{sourcedId}

- Method: PATCH
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Partially update an assessment line item with metadata merging.

Path params:

- `sourcedId` (string, required): The assessment line item's sourcedId

Request body:

- `assessmentLineItem` (object, required): Partial assessment line item data
  - All fields optional; only provided fields are updated
  - `metadata` is merged with existing

Successful response (HTTP 200):

- Body: `{ "assessmentLineItem": LineItem }`

Python usage:

```python
from timeback import Timeback
from timeback.models.request import TimebackPatchAssessmentLineItemRequest, TimebackPatchAssessmentLineItemBody

client = Timeback()

body = TimebackPatchAssessmentLineItemBody(
    title="Patched Title",
    description="Updated description",
)
request = TimebackPatchAssessmentLineItemRequest(sourced_id="<sourcedId>", assessmentLineItem=body)
response = client.oneroster.gradebook.patch_assessment_line_item(request)
```

