## QTI API — Update Assessment Test Metadata

### PUT /assessment-tests/{identifier}/metadata

- Method: PUT
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Update only the metadata fields (title, description, etc.) of an assessment test without affecting its structure, test parts, sections, or assessment items. This is a lightweight operation for administrative changes.

Path params:

- `identifier` (string, required): Unique identifier of the assessment test to update

Request body:

- `metadata` (object, required): Custom metadata to update for the assessment test
  - Can include any key-value pairs
  - Common fields: subject, grade, description, learningObjectives

Successful response (HTTP 200):

- Body: Updated assessment test object
- Key fields: Same as GET /assessment-tests/{identifier}

Error responses:

- 400/422: Request/validation → raises `RequestError`
- 401: Unauthorized → raises `AuthError`
- 404: Not Found → raises `NotFoundError`
- 429: Too Many Requests → raises `RateLimitError`
- 5xx: Server errors → raises `ServerError`

Python usage:

```python
from timeback import Timeback
from timeback.models.request import TimebackUpdateAssessmentTestMetadataRequest

client = Timeback()

# Update simple metadata
request = TimebackUpdateAssessmentTestMetadataRequest(
    metadata={
        "subject": "Math",
        "grade": "5",
        "description": "Updated description"
    }
)
test = client.qti.update_assessment_test_metadata("test-001", request)

print(f"Updated: {test.identifier}")
print(f"Metadata: {test.metadata}")

# Update with complex metadata
request = TimebackUpdateAssessmentTestMetadataRequest(
    metadata={
        "subject": "Science",
        "learningObjectives": ["LO1", "LO2", "LO3"],
        "settings": {
            "timeLimit": 3600,
            "allowReview": True,
            "showFeedback": True
        },
        "version": "2.0"
    }
)
test = client.qti.update_assessment_test_metadata("test-001", request)

# Update just one field
request = TimebackUpdateAssessmentTestMetadataRequest(
    metadata={"description": "New description only"}
)
test = client.qti.update_assessment_test_metadata("test-001", request)
```

Notes:

- This is a lightweight operation that only affects metadata
- The test structure, test parts, sections, and item references are NOT modified
- Use `update_assessment_test` for structural changes
- Metadata can include any custom key-value pairs
- This endpoint is useful for administrative updates like changing descriptions or categorization


