# Reset Attempt

Resets a student's attempt for a lesson.

## Endpoint

```
POST /powerpath/resetAttempt
```

## Purpose

Resets the current attempt for a student in a PowerPath lesson:
- Soft-deletes all previous question responses
- Resets the test score to 0
- Updates the scoreStatus to "not submitted"

For external tests, only resets the score to 0. For Assessment Bank lessons, keeps the user state in the same bank test for the current attempt.

## Request Body

```json
{
  "student": "student-123",
  "lesson": "lesson-456"
}
```

### Request Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| student | string | Yes | The sourcedId of the student |
| lesson | string | Yes | The sourcedId of the lesson (ComponentResource) |

## Response

```json
{
  "success": true,
  "score": 0
}
```

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| success | boolean | Whether the reset was successful |
| score | number | The reset score (always 0 on success) |

## Usage

```python
from timeback import Timeback
from timeback.models.request import TimebackResetAttemptRequest

client = Timeback()

request = TimebackResetAttemptRequest(
    student="student-123",
    lesson="lesson-456"
)

response = client.powerpath.reset_attempt(request)

if response.success:
    print("Attempt reset successfully")
else:
    print("Reset failed")
```

## Notes

- A 'Lesson' is a ComponentResource object with an associated Resource
- For external tests, only the score is reset (not question responses)
- For Assessment Bank lessons, the user remains in the same sub-test

