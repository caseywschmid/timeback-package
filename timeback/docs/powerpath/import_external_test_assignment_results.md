## PowerPath — External Tests - Import External Test Assignment Results

### GET /powerpath/importExternalTestAssignmentResults

- Method: GET
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Retrieve and store results from an external test assignment.

Retrieves and stores the results of an external test assignment. Applies to 'test-out', 'placement', and 'unit-test' lessons.

### Tool Provider Behavior

**For "edulastic":**
- If the lesson is already finalized, no data import is performed.
- If not finalized, populates test and question results. The test is finalized when all questions are answered and grade is "GRADED".

**For "mastery-track":**
- If the lesson is already finalized, no data import is performed.
- If not finalized and write-back detected, processes results. The test is finalized when scoreStatus is "fully graded" and masteryTrackProcessed is true.

### Query Parameters

- `student` (string, required): The sourcedId of the student
- `lesson` (string, required): The sourcedId of the lesson (ComponentResource)
- `applicationName` (string, optional): The name of the application

### Response

```json
{
  "lessonType": "placement",
  "lessonId": "component-resource-id",
  "toolProvider": "edulastic",
  "finalized": true,
  "attempt": 1,
  "credentials": {
    "email": "student@example.com",
    "password": "test-password"
  },
  "assignmentId": "edulastic-assignment-id",
  "classId": "edulastic-class-id",
  "testUrl": "https://edulastic.com/test/123",
  "testId": "edulastic-test-id"
}
```

**Required fields:**
- `lessonType`: "test-out", "placement", or "unit-test"
- `lessonId`: The sourcedId of the lesson (can be null)
- `toolProvider`: The tool provider (can be null)
- `finalized`: Whether the test has been finalized
- `attempt`: The attempt number

**Optional fields:**
- `credentials`: Email/password for external tool access
- `assignmentId`, `classId`, `testUrl`, `testId`: External tool identifiers

### Python Usage

```python
from timeback import Timeback
from timeback.models.request import TimebackImportExternalTestAssignmentResultsRequest

client = Timeback()

request = TimebackImportExternalTestAssignmentResultsRequest(
    student="student-sourced-id",
    lesson="lesson-component-resource-id",
)
response = client.powerpath.import_external_test_assignment_results(request)

if response.finalized:
    print("Test completed! Results are ready.")
    # Use getAssessmentProgress to retrieve actual test results
else:
    print(f"Test not yet finalized. Attempt: {response.attempt}")
```

### Notes

- A previous test assignment via `make_external_test_assignment` is required before calling this endpoint.
- May trigger automatic course enrollment if the lesson is a placement test or test-out.
- Use `get_assessment_progress` to retrieve actual test results after finalization.

