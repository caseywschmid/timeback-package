# Get Next Question

Returns the next question in a PowerPath-100 lesson.

## Endpoint

```
GET /powerpath/getNextQuestion
```

## Purpose

Retrieves the next question for adaptive learning in a PowerPath-100 lesson. This endpoint only works with lessons of type 'powerpath-100'.

## Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| student | string | Yes | The sourcedId of the student |
| lesson | string | Yes | The sourcedId of the lesson (ComponentResource) |

## Response

```json
{
  "score": 75.5,
  "question": {
    "id": "q-123",
    "index": 5,
    "title": "Math Question 5",
    "url": "https://qti.example.com/question/123",
    "difficulty": "medium",
    "humanApproved": true,
    "content": {
      "type": "choice",
      "rawXml": "<qti-assessment-item>...</qti-assessment-item>"
    },
    "learningObjectives": ["lo-1", "lo-2"]
  }
}
```

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| score | number | Current PowerPath score in this lesson |
| question.id | string | Question ID in the test |
| question.index | number | Question index in the test |
| question.title | string | Question title |
| question.url | string | URL to the QTI question |
| question.difficulty | string | Difficulty: easy, medium, or hard |
| question.humanApproved | boolean | null | Whether human-approved |
| question.content | object | QTI content with rawXml |
| question.response | string | array | Previous student response (if any) |
| question.correct | boolean | Whether previous response was correct |
| question.result | object | Previous result with score/feedback |
| question.learningObjectives | array | Associated learning objective IDs |

## Usage

```python
from timeback import Timeback

client = Timeback()

response = client.powerpath.get_next_question(
    student="student-123",
    lesson="powerpath-100-lesson-id"
)

print(f"Current Score: {response.score}")
print(f"Next Question: {response.question.title}")
print(f"Difficulty: {response.question.difficulty}")
```

## Notes

- Only works with lessons of type 'powerpath-100'
- A 'Lesson' is a ComponentResource object with an associated Resource
- The question content includes raw QTI XML for rendering

