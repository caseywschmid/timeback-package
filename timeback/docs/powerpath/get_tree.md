## PowerPath — Lesson Plans - Get Tree

### GET /powerpath/lessonPlans/{courseId}/{userId}

- Method: GET
- Auth: OAuth2 Client Credentials (Bearer token)

Returns the complete lesson plan tree for a course and student.

### Path Parameters

- `courseId` (string, required): The sourcedId of the course
- `userId` (string, required): The sourcedId of the student

### Response

The response is a nested tree structure containing the course info and all components:

```json
{
  "lessonPlan": {
    "lessonPlan": {
      "course": {
        "sourcedId": "course-123",
        "status": "active",
        "title": "Math Grade 5",
        "org": { "sourcedId": "org-1" },
        "grades": ["5"],
        "subjects": ["Math"]
      },
      "subComponents": [
        {
          "sourcedId": "unit-1",
          "title": "Unit 1: Numbers",
          "status": "active",
          "sortOrder": "1",
          "componentResources": [...],
          "subComponents": [...]
        }
      ]
    }
  }
}
```

### Tree Structure

- **Course**: Top-level course information
- **subComponents**: List of components (units, chapters)
  - Each component can have nested `subComponents` (lessons, activities)
  - Each component can have `componentResources` (learning materials)

### Component Properties

- `sourcedId` (string): Unique identifier
- `title` (string): Display name
- `status` (string): "active" or "tobedeleted"
- `sortOrder` (string): Order within parent
- `metadata` (object): Additional metadata
- `prerequisites` (array): Required component IDs
- `componentResources` (array): Associated resources
- `subComponents` (array): Nested components

### Python Usage

```python
from timeback import Timeback
from timeback.models.request import TimebackGetTreeRequest

client = Timeback()

request = TimebackGetTreeRequest(
    course_id="course-sourced-id",
    user_id="student-sourced-id",
)

lesson_plan = client.powerpath.get_tree(request)

print(f"Course: {lesson_plan.course['title']}")
print(f"Units: {len(lesson_plan.subComponents)}")

for unit in lesson_plan.subComponents:
    print(f"  - {unit.title}")
    for lesson in unit.subComponents or []:
        print(f"    - {lesson.title}")
```

### Return Type

Returns a `LessonPlan` object with:
- `course` (dict): Course information
- `subComponents` (List[LessonPlanComponent]): Tree of components
- `metadata` (dict): Additional plan metadata

### Notes

- The tree is specific to the student and includes their progress data
- Use `get_lesson_plan` with a lessonPlanId for direct access if you know the ID
- Returns 404 if no lesson plan exists for the course/student

