## QTI API — Delete Assessment Item

### DELETE /assessment-items/{identifier}

- Method: DELETE
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Permanently delete an assessment item. This operation cannot be undone.

Path params:

- `identifier` (string, required): Unique identifier of the assessment item to delete

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

# Delete an assessment item
client.qti.delete_assessment_item("math-addition-001")
print("Assessment item deleted successfully")

# Common pattern: Create, use, then delete
from timeback.models.request import TimebackCreateAssessmentItemRequest

# Create item
request = TimebackCreateAssessmentItemRequest(
    format="xml",
    xml=xml_content
)
item = client.qti.create_assessment_item(request)
print(f"Created: {item.identifier}")

# Use item...

# Delete when done
client.qti.delete_assessment_item(item.identifier)
print(f"Deleted: {item.identifier}")
```

Notes:

- **Warning**: Assessment tests that reference this item may be affected
- Item references in test sections will need to be updated separately after deletion
- This operation cannot be undone - ensure you have backups if needed
- Consider using the `rawXml` field to save item content before deletion


