## OneRoster - Resources - Update Resource

### PUT /ims/oneroster/resources/v1p2/resources/{sourcedId}

- Method: PUT
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Update a resource by sourcedId.

Python usage:

```python
from timeback import Timeback
from timeback.models.request import TimebackUpdateResourceRequest, TimebackUpdateResourceBody
from timeback.enums import TimebackImportance

client = Timeback()
body = TimebackUpdateResourceBody(
    title="Updated Resource",
    vendorResourceId="vendor-123",
    importance=TimebackImportance.PRIMARY,
)
request = TimebackUpdateResourceRequest(sourced_id="<sourcedId>", resource=body)
response = client.oneroster.resources.update_resource(request)
print(f"Updated: {response.resource.title}")
```

