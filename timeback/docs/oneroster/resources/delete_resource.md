## OneRoster - Resources - Delete Resource

### DELETE /ims/oneroster/resources/v1p2/resources/{sourcedId}

- Method: DELETE
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Soft delete a resource (sets status to tobedeleted).

Python usage:

```python
from timeback import Timeback

client = Timeback()
result = client.oneroster.resources.delete_resource("<sourcedId>")
```

