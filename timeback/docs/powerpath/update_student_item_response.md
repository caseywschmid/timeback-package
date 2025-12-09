## PowerPath — Lesson Plans - Update Student Item Response

### POST /powerpath/lessonPlans/updateStudentItemResponse

- Method: POST
- Auth: OAuth2 Client Credentials (Bearer token)

Updates the student's response for a component or resource.

### Request Body

```json
{
  "studentId": "student-sourced-id",
  "componentResourceId": "component-or-resource-id",
  "result": {
    "status": "active",
    "scoreDate": "2024-01-15T10:00:00Z",
    "scoreStatus": "fully graded",
    "score": 85.5,
    "comment": "Good work!"
  }
}
```

### Required Fields

- `studentId`: Student's sourcedId
- `componentResourceId`: Component or resource ID
- `result.status`: "active" or "tobedeleted"
- `result.scoreDate`: ISO date-time
- `result.scoreStatus`: Score status (see below)

### Optional Result Fields

- `score`: Numeric score
- `textScore`: Text-based score
- `scorePercentile`: Percentile
- `comment`: Teacher/system comment
- `metadata`: Additional metadata
- `learningObjectiveSet`: Learning objective results
- `inProgress`, `incomplete`, `late`, `missing`: Status flags

### Score Statuses

- `exempt`
- `fully graded`
- `not submitted`
- `partially graded`
- `submitted`

### Response

```json
{
  "componentResourceLineItem": {
    "sourcedId": "ali-123",
    "status": "active",
    "title": "Quiz 1"
  },
  "componentResourceResult": {
    "sourcedId": "result-456",
    "score": 85.5,
    "scoreStatus": "fully graded"
  }
}
```

### Python Usage

```python
from timeback import Timeback
from timeback.models.request import (
    TimebackUpdateStudentItemResponseRequest,
    TimebackStudentItemResult,
)

client = Timeback()

result = TimebackStudentItemResult(
    status="active",
    scoreDate="2024-01-15T10:00:00Z",
    scoreStatus="fully graded",
    score=85.0,
    comment="Good work!",
)

request = TimebackUpdateStudentItemResponseRequest(
    student_id="student-id",
    component_resource_id="resource-id",
    result=result,
)

response = client.powerpath.update_student_item_response(request)
print(f"Line Item: {response.componentResourceLineItem}")
```

