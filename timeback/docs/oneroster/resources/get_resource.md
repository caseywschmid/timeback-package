## OneRoster - Resources - Get Resource

### GET /ims/oneroster/resources/v1p2/resources/{sourcedId}

- Method: GET
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Get a single resource by sourcedId.

Python usage:

```python
from timeback import Timeback
from timeback.models.request import TimebackGetResourceRequest

client = Timeback()
request = TimebackGetResourceRequest(sourced_id="<sourcedId>")
response = client.oneroster.resources.get_resource(request)
print(f"Title: {response.resource.title}")
```

