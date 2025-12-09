## PowerPath — External Tests - Get Test-Out

### GET /powerpath/testOut

- Method: GET
- Auth: OAuth2 Client Credentials (Bearer token)
- **Status: DEPRECATED**

⚠️ **This endpoint is deprecated and will be removed in a future version.**

### Migration

Use `GET /powerpath/lessonPlans/getCourseProgress/:courseId/student/:studentId` instead. The response now includes a `testOut` field with comprehensive status information.

---

### Legacy Behavior

Returns the testOut lesson reference for a student and course.

### Query Parameters

- `student` (string, required): The sourcedId of the student
- `course` (string, required): The sourcedId of the Course

### Response

```json
{
  "lessonType": "test-out",
  "lessonId": "component-resource-id",
  "finalized": true,
  "toolProvider": "edulastic",
  "attempt": 1,
  "credentials": {
    "email": "student@example.com",
    "password": "test-password"
  },
  "assignmentId": "assignment-id",
  "classId": "class-id",
  "testUrl": "https://edulastic.com/test/123",
  "testId": "test-id"
}
```

**Fields:**
- `lessonType`: Always "test-out"
- `lessonId`: The id of the testOut lesson. Null if no test-out found.
- `finalized`: Whether the Test Out has been finalized
- `toolProvider`: The tool provider (edulastic, mastery-track, or null)
- `attempt`: The attempt number
- `credentials`: External tool access credentials (if test was assigned)
- External IDs: `assignmentId`, `classId`, `testUrl`, `testId`

### Python Usage (deprecated)

```python
import warnings
from timeback import Timeback
from timeback.models.request import TimebackGetTestOutRequest

client = Timeback()

request = TimebackGetTestOutRequest(
    student="student-sourced-id",
    course="course-sourced-id",
)

# This will emit a DeprecationWarning
with warnings.catch_warnings():
    warnings.simplefilter("always")  # To see the warning
    response = client.powerpath.get_test_out(request)

if response.lessonId:
    print(f"Test-out available: {response.lessonId}")
else:
    print("No test-out in this course")
```

**Recommended: Use get_course_progress() instead.**

