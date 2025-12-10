## QTI API — Delete Stimulus

### DELETE /stimuli/{identifier}

- Method: DELETE
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Permanently delete a stimulus from the service provider. This operation cannot be undone.

Path parameters:

- `identifier` (string, required): Unique identifier of the stimulus to delete

Successful response (HTTP 204):

- No content returned on successful deletion

Error responses:

- 401: Unauthorized → raises `AuthError`
- 404: Stimulus not found → raises `NotFoundError`
- 429: Too Many Requests → raises `RateLimitError`
- 5xx: Server errors → raises `ServerError`

Python usage:

```python
from timeback import Timeback

client = Timeback()

# Delete a stimulus
client.qti.delete_stimulus("stimulus-science-001")
# No return value on success

# Handle potential errors
try:
    client.qti.delete_stimulus("nonexistent-stimulus")
except NotFoundError:
    print("Stimulus not found")
```

Notes:

- This operation is **permanent** and cannot be undone
- Assessment items that reference this stimulus may be affected
- Consider checking for references before deletion
- The endpoint returns 204 No Content on success (no response body)
- Use `get_stimulus` to verify the stimulus exists before attempting deletion

