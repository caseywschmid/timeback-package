## OneRoster — Rostering - Delete School

### DELETE /ims/oneroster/rostering/v1p2/schools/{sourcedId}

- Method: DELETE
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Perform a soft delete on a specific school. This operation changes the status of the school to 'tobedeleted'.

Path params:

- `sourcedId` (string, required): The sourcedId of the school to delete

Successful response (HTTP 204):

- No content body
- Client return type: `Optional[Dict[str, Any]]` (typically `None` for 204 responses)

Error responses:

- 400: Bad Request → raises `RequestError`
- 401: Unauthorized → raises `AuthError`
- 403: Forbidden → raises `RequestError`
- 404: Not Found → raises `NotFoundError`
- 422: Unprocessable Entity → raises `RequestError`
- 429: Too Many Requests → raises `RateLimitError`
- 5xx: Server errors → raises `ServerError`

Python usage:

```python
from timeback import Timeback

client = Timeback()
sourced_id = "school-001"
result = client.oneroster.rostering.delete_school(sourced_id)
print("Result:", result)  # Typically None for 204 No Content
```

Notes:

- This is a soft delete operation - the school's status is changed to 'tobedeleted' rather than being permanently removed.
- The endpoint returns `None` for successful 204 No Content responses.
- If the school does not exist, a `NotFoundError` will be raised.

