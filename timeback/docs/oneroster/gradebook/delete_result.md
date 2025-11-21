## OneRoster — Gradebook - Delete Result

### DELETE /ims/oneroster/gradebook/v1p2/results/{sourcedId}

- Method: DELETE
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Perform a soft delete on a specific Result on the service provider. This operation changes the status of the Result to 'tobedeleted'.

Path params:

- `sourcedId` (string, required): The sourcedId of the result to delete

Request model:

- `TimebackDeleteResultRequest` with required fields:
  - `sourced_id` (string): The sourcedId of the result (path parameter)

Successful response (HTTP 204):

- No Content. The method returns `None` (or empty dictionary depending on implementation details).

Error responses:

- 400: Bad Request → raises `RequestError`
- 401: Unauthorized → raises `AuthError`
- 403: Forbidden → raises `RequestError`
- 404: Result not found → raises `NotFoundError`
- 422: Unprocessable Entity / Validation Error → raises `RequestError`
- 429: Too Many Requests → raises `RateLimitError`
- 5xx: Server errors → raises `ServerError`

Python usage:

```python
from timeback import Timeback
from timeback.models.request import TimebackDeleteResultRequest

client = Timeback()
sourced_id = "result-123-456"

# Create the request
request = TimebackDeleteResultRequest(sourced_id=sourced_id)

# Call the API
client.oneroster.gradebook.delete_result(request)

print(f"Result Deleted Successfully!")
```

Notes:

- This is a "soft delete" operation. The record is marked as `tobedeleted` but may still exist in the system for a period.
- If the result is already deleted or does not exist, the server will return 404 Not Found with message 'Result not found'.

