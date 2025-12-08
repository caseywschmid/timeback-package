## OneRoster — Gradebook - Delete Category

### DELETE /ims/oneroster/gradebook/v1p2/categories/{sourcedId}

- Method: DELETE
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Soft delete (tombstone) a category by `sourcedId`. Sets the category's status to `tobedeleted`.

Path params:

- `sourcedId` (string, required): The category's sourcedId

Successful response:

- HTTP 204 No Content (returns `None`)
- Or HTTP 200 with response body (returns raw dict)

Error responses:

- 400/422: Request/validation → raises `RequestError`
- 401: Unauthorized → raises `AuthError`
- 403: Forbidden → raises `RequestError`
- 404: Category not found → raises `NotFoundError`
- 429: Too Many Requests → raises `RateLimitError`
- 5xx: Server errors → raises `ServerError`

Python usage:

```python
from timeback import Timeback

client = Timeback()

# Delete a category by sourcedId
result = client.oneroster.gradebook.delete_category("<sourcedId>")

if result is None:
    print("Category deleted successfully (204 No Content)")
else:
    print(f"Category deleted with response: {result}")
```

Notes:

- This performs a "soft delete" (tombstone), setting the category's status to `tobedeleted`.
- The category is not permanently removed from the system.
- If the category does not exist, a `NotFoundError` is raised.
- Returns `None` for HTTP 204 No Content responses, or a raw dict for other success responses.

