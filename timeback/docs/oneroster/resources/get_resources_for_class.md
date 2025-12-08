## OneRoster - Resources - Get Resources for Class

### GET /ims/oneroster/resources/v1p2/classes/{classSourcedId}/resources

- Method: GET
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Get resources associated with a specific class.

Python usage:

```python
from timeback import Timeback
from timeback.models.request import TimebackGetResourcesForClassRequest

client = Timeback()
request = TimebackGetResourcesForClassRequest(class_sourced_id="<class-id>")
response = client.oneroster.resources.get_resources_for_class(request)
print(f"Total: {response.totalCount}")
```

