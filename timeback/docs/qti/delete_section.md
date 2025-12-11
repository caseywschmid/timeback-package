## QTI API — Delete Section

### DELETE /assessment-tests/{assessmentTestIdentifier}/test-parts/{testPartIdentifier}/sections/{identifier}

- Method: DELETE
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Permanently delete a section from a test part. This operation cannot be undone.

Path params:

- `assessmentTestIdentifier` (string, required): Root assessment test identifier
- `testPartIdentifier` (string, required): Parent test part identifier
- `identifier` (string, required): Section identifier

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

# Delete a section
client.qti.delete_section("test-001", "part-001", "section-001")
print("Section deleted successfully")

# Verify deletion
try:
    client.qti.get_section("test-001", "part-001", "section-001")
except Exception as e:
    print(f"Confirmed deleted: {e}")

# Delete with cleanup pattern
section_id = "section-to-delete"
try:
    # Do something with the section
    pass
finally:
    # Clean up
    try:
        client.qti.delete_section("test-001", "part-001", section_id)
    except Exception:
        pass  # Ignore if already deleted
```

Notes:

- **This operation cannot be undone**
- Item references within the section are removed
- The actual assessment items are NOT deleted
- The parent assessment test's XML is automatically regenerated


