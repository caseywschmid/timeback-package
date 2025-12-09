## OneRoster - Gradebook - Delete Assessment Line Item

### DELETE /ims/oneroster/gradebook/v1p2/assessmentLineItems/{sourcedId}

- Method: DELETE
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Soft delete an assessment line item (sets status to tobedeleted).

Path params:

- sourcedId (string, required): The assessment line items sourcedId

Successful response:

- HTTP 204 No Content (returns None)
- Or HTTP 200 with response body

Python usage:

```python
from timeback import Timeback

client = Timeback()

result = client.oneroster.gradebook.delete_assessment_line_item("<sourcedId>")
if result is None:
    print("Deleted successfully")
```

Notes:

- Soft delete only; sets status to tobedeleted.
- Raises NotFoundError if the item does not exist.

