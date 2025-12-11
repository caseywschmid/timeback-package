## QTI API — Delete Test Part

### DELETE /assessment-tests/{assessmentTestIdentifier}/test-parts/{identifier}

- Method: DELETE
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Permanently delete a test part and all its sections from an assessment test. This operation cannot be undone.

Path params:

- `assessmentTestIdentifier` (string, required): Unique identifier of the parent assessment test
- `identifier` (string, required): Unique identifier of the test part to delete

Successful response (HTTP 200/204):

- Body: None (operation successful)

Error responses:

- 401: Unauthorized → raises `AuthError`
- 404: Not Found → raises `NotFoundError`
- 429: Too Many Requests → raises `RateLimitError`
- 5xx: Server errors → raises `ServerError`

Python usage:

```python
from timeback import Timeback

client = Timeback()

# Delete a test part
client.qti.delete_test_part("test-001", "part-001")
print("Test part deleted successfully")

# Verify deletion
try:
    client.qti.get_test_part("test-001", "part-001")
except Exception as e:
    print(f"Confirmed deleted: {e}")

# Delete with cleanup pattern
part_id = "part-to-delete"
try:
    # Do something with the part
    pass
finally:
    # Clean up
    try:
        client.qti.delete_test_part("test-001", part_id)
    except Exception:
        pass  # Ignore if already deleted
```

Notes:

- **This operation cannot be undone**
- All sections within the test part are also deleted
- The parent assessment test's XML is automatically regenerated
- Assessment items referenced by sections are NOT deleted


