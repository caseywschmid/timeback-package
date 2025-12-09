## PowerPath — Assessment - Get Assessment Progress

### GET /powerpath/getAssessmentProgress

- Method: GET
- Auth: OAuth2 Client Credentials (Bearer token)

Returns the progress a student has made in a PowerPath lesson.

### Query Parameters

- `student` (string, required): Student sourcedId
- `lesson` (string, required): Lesson (ComponentResource) sourcedId
- `attempt` (number, optional): Specific attempt number to query

### Response

Response structure varies by lesson type. Common fields:

```json
{
  "lessonType": "quiz",
  "finalized": false,
  "attempt": 1,
  "score": 75.0,
  "xp": 50,
  "multiplier": 1.0,
  "accuracy": 0.75,
  "correctQuestions": 3,
  "totalQuestions": 4,
  "questions": [
    {
      "id": "q1",
      "index": 0,
      "title": "Question 1",
      "url": "https://qti.example.com/q1",
      "difficulty": "medium",
      "response": "A",
      "correct": true
    }
  ],
  "toolProvider": null
}
```

### PowerPath-100 Response

For `powerpath-100` lessons, includes additional fields:

```json
{
  "lessonType": "powerpath-100",
  "remainingQuestionsPerDifficulty": {
    "easy": 2,
    "medium": 5,
    "hard": 3
  },
  "seenQuestions": []
}
```

### Python Usage

```python
from timeback import Timeback

client = Timeback()

# Get current progress
response = client.powerpath.get_assessment_progress(
    "student-id",
    "lesson-component-resource-id"
)

print(f"Score: {response.score}")
print(f"Accuracy: {response.accuracy}")
print(f"Progress: {response.correctQuestions}/{response.totalQuestions}")

# Get specific attempt
response = client.powerpath.get_assessment_progress(
    "student-id",
    "lesson-id",
    attempt=2
)
```

