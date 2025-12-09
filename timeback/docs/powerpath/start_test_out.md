## PowerPath — Lesson Plans - Start Test Out

### POST /powerpath/lessonPlans/startTestOut

- Method: POST
- Auth: OAuth2 Client Credentials (Bearer token)

Creates an on-demand test-out assignment for a student in a course.

### Purpose

This is the recommended endpoint for initiating test-out workflows. It:
- Validates student eligibility for test-out
- Creates an unlisted test assignment (or reuses existing active assignment)
- Returns assignment info for launching the external test

**Note:** This endpoint does NOT start the external test. After calling this, use `make_external_test_assignment` to start the test with the provider (Edulastic or MasteryTrack).

### Eligibility Requirements

- Course must have a supported subject+grade combination
- Student must be actively enrolled in a course with that subject+grade
- Student must not have a completed or failed test-out for this subject+grade

### Request Body

```json
{
  "courseId": "course-sourced-id",
  "studentId": "student-sourced-id"
}
```

**Required fields:**
- `courseId` (string): The sourcedId of the course
- `studentId` (string): The sourcedId of the student

### Response

```json
{
  "assignmentId": "assign-123",
  "lessonId": "lesson-456",
  "resourceId": "resource-789",
  "status": "created"
}
```

**Fields:**
- `assignmentId` (string): The test assignment ID
- `lessonId` (string): The component resource ID (lesson)
- `resourceId` (string): The resource ID
- `status` (string): Either `"created"` (new) or `"existing"` (reused)

### Python Usage

```python
from timeback import Timeback
from timeback.models.request import TimebackStartTestOutRequest

client = Timeback()

request = TimebackStartTestOutRequest(
    course_id="course-sourced-id",
    student_id="student-sourced-id",
)

response = client.powerpath.start_test_out(request)

if response.status == "created":
    print("New test-out assignment created")
else:
    print("Using existing assignment")

print(f"Assignment ID: {response.assignmentId}")
```

### Workflow

1. Call `start_test_out` to create/get the assignment
2. Call `make_external_test_assignment` with the assignment info to start the external test
3. Student completes the test on the external platform
4. Call `import_external_test_assignment_results` to retrieve results

### Notes

- Replaces the deprecated `create_external_test_out` endpoint
- Idempotent: calling multiple times returns the same active assignment
- Returns 400 if student is not eligible (not enrolled, already completed, etc.)

