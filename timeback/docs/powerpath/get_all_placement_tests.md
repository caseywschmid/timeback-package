## PowerPath — Placement - Get All Placement Tests

### GET /powerpath/placement/getAllPlacementTests

- Method: GET
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Get all placement tests for a student and subject, including available results for each.

A 'Lesson' (placement test) in this context is a ComponentResource object which has a Resource object with `metadata.lessonType = "placement"` associated with it.

Query params:

- `student` (string, required): The sourcedId of the student
- `subject` (string, required): The subject name. Valid values: `Reading`, `Language`, `Vocabulary`, `Social Studies`, `Writing`, `Science`, `FastMath`, `Math`

Successful response (HTTP 200):

- Body: `{ "placementTests": [PlacementTest, ...] }`
- Each PlacementTest contains:
  - `component_resources` (object): The component resource data
  - `resources` (object): The resource data
  - `resources_metadata` (object): Metadata associated with the resource
  - `assessment_line_items` (object | null): Assessment line item data, if available
  - `assessment_results` (array | null): List of assessment results, if available

Error responses:

- 400/422: Request/validation → raises `RequestError`
- 401: Unauthorized → raises `AuthError`
- 403: Forbidden → raises `RequestError`
- 404: Not Found → raises `NotFoundError`
- 429: Too Many Requests → raises `RateLimitError`
- 5xx: Server errors → raises `ServerError`

Python usage:

```python
from timeback import Timeback
from timeback.models.request import TimebackGetAllPlacementTestsRequest
from timeback.enums import TimebackSubject

client = Timeback()

# Get all placement tests for a student in Reading
request = TimebackGetAllPlacementTestsRequest(
    student="student-sourced-id",
    subject=TimebackSubject.READING,
)
response = client.powerpath.get_all_placement_tests(request)

print(f"Found {len(response.placementTests)} placement tests")

for test in response.placementTests:
    print(f"Component Resource: {test.component_resources.get('sourcedId')}")
    print(f"Resource: {test.resources.get('sourcedId')}")
    if test.assessment_results:
        print(f"Has {len(test.assessment_results)} assessment result(s)")
```

Notes:

- The `subject` parameter uses the `TimebackSubject` enum which maps to the API's expected string values.
- Assessment data (`assessment_line_items` and `assessment_results`) may be null if no assessments have been created or completed for the placement test.

