## OneRoster — Gradebook - Delete Assessment Result

### DELETE /ims/oneroster/gradebook/v1p2/assessmentResults/{sourcedId}

- Method: DELETE
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Soft delete (tombstone) an assessment result by `sourcedId`. Sets the status to `tobedeleted`.

Path params:

- `sourcedId` (string, required): The assessment result's sourcedId

Successful response:

- HTTP 204 No Content (returns `None`)
- Or HTTP 200 with response body (returns raw dict)

Error responses:

- 400/422: Request/validation → raises `RequestError`
- 401: Unauthorized → raises `AuthError`
- 403: Forbidden → raises `RequestError`
- 404: Assessment result not found → raises `NotFoundError`
- 429: Too Many Requests → raises `RateLimitError`
- 5xx: Server errors → raises `ServerError`

Python usage:

```python
from timeback import Timeback

client = Timeback()

# Delete an assessment result by sourcedId
result = client.oneroster.gradebook.delete_assessment_result("<sourcedId>")

if result is None:
    print("Assessment result deleted successfully (204 No Content)")
else:
    print(f"Deleted with response: {result}")
```

Notes:

- This performs a "soft delete" (tombstone), setting the status to `tobedeleted`.
- The assessment result is not permanently removed from the system.
- If the assessment result does not exist, a `NotFoundError` is raised.

