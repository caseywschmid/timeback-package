## PowerPath — Lesson Plans - Create Lesson Plan

### POST /powerpath/lessonPlans/

- Method: POST
- Auth: OAuth2 Client Credentials (Bearer token)

Creates a new lesson plan for a course and student.

### Purpose

Use this endpoint when:
- A new student is enrolled in a course
- Initial setup of a student's learning path
- Creating a lesson plan from scratch

### Request Body

```json
{
  "courseId": "course-sourced-id",
  "userId": "student-sourced-id",
  "classId": "class-sourced-id"  // optional
}
```

**Required fields:**
- `courseId` (string): The sourcedId of the course
- `userId` (string): The sourcedId of the student

**Optional fields:**
- `classId` (string): The sourcedId of the class (defaults to current year's class)

### Response

Returns HTTP 200 if lesson plan already exists, HTTP 201 if newly created.
Both responses have the same structure:

```json
{
  "lessonPlanId": "lp-123-abc"
}
```

**Fields:**
- `lessonPlanId` (string): The ID of the created or existing lesson plan

### Python Usage

```python
from timeback import Timeback
from timeback.models.request import TimebackCreateLessonPlanRequest

client = Timeback()

request = TimebackCreateLessonPlanRequest(
    course_id="course-sourced-id",
    user_id="student-sourced-id",
    # class_id="class-sourced-id",  # optional
)

response = client.powerpath.create_lesson_plan(request)
print(f"Lesson Plan ID: {response.lessonPlanId}")
```

### Notes

- If a lesson plan already exists for the course/student combination, the existing ID is returned
- The optional `classId` parameter allows associating the lesson plan with a specific class
- Returns 404 if course, user, or class is not found

