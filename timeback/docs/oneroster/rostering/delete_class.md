## OneRoster — Rostering - Delete Class

### DELETE /ims/oneroster/rostering/v1p2/classes/{sourcedId}

- Method: DELETE
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Perform a soft delete on a specific class. This operation changes the status of the class to 'tobedeleted'.

Path params:

- `sourcedId` (string, required): The sourcedId of the class to delete

Successful response (HTTP 204):

- No content returned

Error responses:

- 400/422: Request/validation → raises `RequestError`
- 401: Unauthorized → raises `AuthError`
- 403: Forbidden → raises `RequestError`
- 404: Not Found → raises `NotFoundError`
- 429: Too Many Requests → raises `RateLimitError`
- 5xx: Server errors → raises `ServerError`

Python usage:

```python
from timeback import Timeback

client = Timeback()

# Delete a class (soft delete)
result = client.oneroster.rostering.delete_class("<sourcedId>")

# result is None for successful 204 response
print(f"Class deleted: {result is None}")
```

Notes:

- This is a soft delete operation - the class status is set to 'tobedeleted'.
- The class data is not permanently removed from the system.
- Returns `None` for successful 204 No Content response.
- If the class does not exist, a `NotFoundError` is raised.

