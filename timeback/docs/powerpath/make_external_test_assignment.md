## PowerPath — External Tests - Make External Test Assignment

### POST /powerpath/makeExternalTestAssignment

- Method: POST
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Make an external test assignment for a student.

Makes an external test assignment for a student. Applies to 'test-out', 'placement', and 'unit-test' lessons. Returns credentials and URLs needed to take the test on the external platform.

### Tool Provider Behavior

**For "edulastic":**
- Authenticates the student with their email on Edulastic
- Assigns the test to the student in Edulastic
- Stores the received assignmentId and classId
- Returns the test link, credentials, and IDs for results consumption

**For "mastery-track":**
- Authenticates the student with their email on MasteryTrack
- Assigns the test (using testId or subject+grade from Resource metadata)
- Stores the received assignmentId
- Waits for a test result write-back on test end

### Request Body

```json
{
  "student": "student-sourced-id",
  "lesson": "lesson-component-resource-id",
  "applicationName": "optional-app-name",
  "testId": "optional-specific-test-id",
  "skipCourseEnrollment": false
}
```

**Required fields:**
- `student` (string): The sourcedId of the student
- `lesson` (string): The sourcedId of the lesson (ComponentResource)

**Optional fields:**
- `applicationName` (string): Application name for external tool authentication
- `testId` (string): Specific test ID for MasteryTrack (overrides subject+grade selection)
- `skipCourseEnrollment` (boolean): When true, skips automatic course enrollment after test completion

### Response

```json
{
  "toolProvider": "edulastic",
  "lessonType": "placement",
  "attempt": 1,
  "credentials": {
    "email": "student@example.com",
    "password": "test-password"
  },
  "assignmentId": "edulastic-assignment-id",
  "classId": "edulastic-class-id",
  "testUrl": "https://edulastic.com/test/123",
  "testId": "test-id"
}
```

### Python Usage

```python
from timeback import Timeback
from timeback.models.request import TimebackMakeExternalTestAssignmentRequest

client = Timeback()

request = TimebackMakeExternalTestAssignmentRequest(
    student="student-sourced-id",
    lesson="lesson-component-resource-id",
    skipCourseEnrollment=True,  # Optional: prevent auto-enrollment
)
response = client.powerpath.make_external_test_assignment(request)

print(f"Test URL: {response.testUrl}")
print(f"Email: {response.credentials.email}")
print(f"Password: {response.credentials.password}")
```

### Workflow

1. **Create test** using `create_external_placement_test` or `create_external_test_out`
2. **Assign test** using `make_external_test_assignment` → get credentials
3. **Student takes test** on external platform using credentials
4. **Import results** using `import_external_test_assignment_results`
5. **Get results** using `get_assessment_progress`

### Notes

- A lesson must be created first (external placement test, test-out, or unit-test).
- The credentials returned are for the student to authenticate on the external platform.
- Use `skipCourseEnrollment=True` to prevent automatic course enrollment after test completion.

