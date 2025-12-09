## OneRoster - Resources - Create Resource

### POST /ims/oneroster/resources/v1p2/resources

- Method: POST
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Create a new resource.

Request body:

- `resource` (object): Resource data
  - Required: `title`, `vendorResourceId`, `importance`

Python usage:

```python
from timeback import Timeback
from timeback.models.request import TimebackCreateResourceRequest, TimebackCreateResourceBody
from timeback.enums import TimebackImportance

client = Timeback()
body = TimebackCreateResourceBody(
    title="My Resource",
    vendorResourceId="vendor-123",
    importance=TimebackImportance.PRIMARY,
)
request = TimebackCreateResourceRequest(resource=body)
response = client.oneroster.resources.create_resource(request)
print(f"Created: {response.sourcedIdPairs.allocatedSourcedId}")
```

