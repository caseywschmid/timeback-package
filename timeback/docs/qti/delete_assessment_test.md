## QTI API — Delete Assessment Test

### DELETE /assessment-tests/{identifier}

- Method: DELETE
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Permanently delete an assessment test and all its associated data including test parts, sections, and item references. This operation cannot be undone. The actual assessment items referenced by this test are NOT deleted.

Path params:

- `identifier` (string, required): Unique identifier of the assessment test to delete

Successful response (HTTP 204):

- Body: None (empty response on success)

Error responses:

- 401: Unauthorized → raises `AuthError`
- 404: Not Found → raises `NotFoundError`
- 429: Too Many Requests → raises `RateLimitError`
- 5xx: Server errors → raises `ServerError`

Python usage:

```python
from timeback import Timeback

client = Timeback()

# Delete an assessment test
client.qti.delete_assessment_test("math-test-001")
print("Assessment test deleted successfully")

# Common pattern: Create, use, then delete
from timeback.models.request import TimebackCreateAssessmentTestRequest

# Create test
request = TimebackCreateAssessmentTestRequest(
    format="xml",
    xml=xml_content
)
test = client.qti.create_assessment_test(request)
print(f"Created: {test.identifier}")

# Use test...

# Delete when done
client.qti.delete_assessment_test(test.identifier)
print(f"Deleted: {test.identifier}")
```

Notes:

- **Warning**: This operation cannot be undone
- Test parts, sections, and item references are deleted
- The actual assessment items are NOT deleted - only their references in this test
- Consider using the `rawXml` field to save test content before deletion
- Active test sessions may be affected


