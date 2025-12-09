## OneRoster - Resources - Get All Resources

### GET /ims/oneroster/resources/v1p2/resources

- Method: GET
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Get all resources (paginated).

Query params:

- `fields`, `limit`, `offset`, `sort`, `orderBy`, `filter`, `search`

Python usage:

```python
from timeback import Timeback
from timeback.models.request import TimebackGetAllResourcesRequest

client = Timeback()
request = TimebackGetAllResourcesRequest()
response = client.oneroster.resources.get_all_resources(request)
print(f"Total: {response.totalCount}")
```

