# Update Student Question Response

Updates a student's response to a question and returns updated scores.

## Endpoint

```
PUT /powerpath/updateStudentQuestionResponse
```

## Purpose

Submits and processes a student's answer to a question:
- Checks correctness using QTI response declarations
- Updates the score accordingly
- Creates/updates AssessmentLineItem and AssessmentResult objects

## Request Body

```json
{
  "student": "student-123",
  "question": "q-456",
  "lesson": "lesson-789",
  "responses": {
    "RESPONSE": "choice-A"
  }
}
```

### Request Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| student | string | Yes | The sourcedId of the student |
| question | string | Yes | The QTI question identifier |
| lesson | string | Yes | The sourcedId of the lesson (ComponentResource) |
| response | string/array | No | DEPRECATED: Use responses instead |
| responses | object | No | Response identifiers and values |

## Response

Response varies by lesson type. All responses include:

```json
{
  "lessonType": "powerpath-100"
}
```

### PowerPath-100 Response

```json
{
  "lessonType": "powerpath-100",
  "powerpathScore": 85.5,
  "responseResult": {
    "isCorrect": true,
    "score": 1,
    "feedback": "Correct!"
  },
  "accuracy": 0.9,
  "correctQuestions": 9,
  "totalQuestions": 10,
  "xp": 150,
  "multiplier": 1.5,
  "questionResult": {},
  "testResult": {}
}
```

### Quiz/Test-Out/Placement/Unit-Test Response

```json
{
  "lessonType": "quiz",
  "questionResult": {}
}
```

### Lesson Types

| Type | Description |
|------|-------------|
| powerpath-100 | Adaptive PowerPath lesson |
| quiz | Standard quiz |
| test-out | Test-out assessment |
| placement | Placement test |
| unit-test | Unit test |

## Usage

```python
from timeback import Timeback
from timeback.models.request import TimebackUpdateStudentQuestionResponseRequest

client = Timeback()

request = TimebackUpdateStudentQuestionResponseRequest(
    student="student-123",
    question="q-456",
    lesson="lesson-789",
    responses={"RESPONSE": "choice-A"}
)

response = client.powerpath.update_student_question_response(request)

print(f"Lesson Type: {response.lessonType}")

if response.lessonType == "powerpath-100":
    print(f"Score: {response.powerpathScore}")
    print(f"Correct: {response.responseResult.isCorrect}")
    print(f"XP: {response.xp}")
```

## Notes

- A 'Lesson' is a ComponentResource object with an associated Resource
- The `response` field is deprecated; use `responses` instead
- Response structure varies significantly based on lesson type

