## OneRoster - Resources - Get Resources for User

### GET /ims/oneroster/resources/v1p2/users/{userSourcedId}/resources

- Method: GET
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Get resources associated with a specific user.

Python usage:

```python
from timeback import Timeback
from timeback.models.request import TimebackGetResourcesForUserRequest

client = Timeback()
request = TimebackGetResourcesForUserRequest(user_sourced_id="<user-id>")
response = client.oneroster.resources.get_resources_for_user(request)
print(f"Total: {response.totalCount}")
```

