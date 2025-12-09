## PowerPath — Lesson Plans - Get Course Progress

### GET /powerpath/lessonPlans/getCourseProgress/{courseId}/student/{studentId}

- Method: GET
- Auth: OAuth2 Client Credentials (Bearer token)

Returns assessment line items and test-out status for a student in a course.

### Path Parameters

- `courseId` (string, required): The sourcedId of the course
- `studentId` (string, required): The sourcedId of the student

### Query Parameters

- `lessonId` (string, optional): Component resource ID to filter by lesson

### Response

```json
{
  "lineItems": [
    {
      "type": "component",
      "assessmentLineItemSourcedId": "ali-1",
      "courseComponentSourcedId": "comp-1",
      "title": "Unit 1",
      "results": []
    },
    {
      "type": "resource",
      "assessmentLineItemSourcedId": "ali-2",
      "courseComponentResourceSourcedId": "res-1",
      "title": "Quiz 1",
      "results": [
        {
          "status": "active",
          "scoreDate": "2024-01-15T10:00:00Z",
          "scoreStatus": "fully graded",
          "score": 85.5
        }
      ]
    }
  ],
  "testOut": {
    "status": "available"
  }
}
```

### Line Item Types

- `component`: A component of the lesson plan (unit, lesson)
- `resource`: A resource (video, quiz, document, etc.)

### Test-Out Statuses

- `not_eligible`: Student cannot take test-out
- `available`: Test-out is available
- `in_progress`: Test-out is being taken
- `completed`: Test-out was passed
- `failed`: Test-out was failed

### Python Usage

```python
from timeback import Timeback

client = Timeback()

# Get all progress
response = client.powerpath.get_course_progress(
    "course-id",
    "student-id"
)

# Filter by lesson
response = client.powerpath.get_course_progress(
    "course-id",
    "student-id",
    lesson_id="lesson-123"
)

for item in response.lineItems:
    print(f"[{item['type']}] {item['title']}")
    for result in item.get('results', []):
        print(f"  Score: {result.get('score')}")
```

