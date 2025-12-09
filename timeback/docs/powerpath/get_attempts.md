# Get Attempts

Returns all attempts for a student in a lesson.

## Endpoint

```
GET /powerpath/getAttempts
```

## Purpose

Retrieves the complete history of attempts for a student in a specific lesson. For Assessment Bank lessons, each attempt may represent a different sub-test of the bank.

## Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| student | string | Yes | The sourcedId of the student |
| lesson | string | Yes | The sourcedId of the lesson (ComponentResource) |

## Response

```json
{
  "attempts": [
    {
      "attempt": 1,
      "score": 80,
      "scoreStatus": "fully graded",
      "xp": 100,
      "startedAt": "2024-01-15T10:00:00Z",
      "completedAt": "2024-01-15T10:30:00Z"
    },
    {
      "attempt": 2,
      "score": 90,
      "scoreStatus": "submitted",
      "xp": 120,
      "startedAt": "2024-01-16T10:00:00Z",
      "completedAt": null
    }
  ]
}
```

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| attempts | array | List of all attempts |
| attempts[].attempt | number | null | The attempt number |
| attempts[].score | number | The current score for this attempt |
| attempts[].scoreStatus | string | Status: exempt, fully graded, not submitted, partially graded, submitted |
| attempts[].xp | number | null | XP earned in this attempt |
| attempts[].startedAt | string | null | When this attempt was started |
| attempts[].completedAt | string | null | When this attempt was completed |

## Usage

```python
from timeback import Timeback

client = Timeback()

response = client.powerpath.get_attempts(
    student="student-123",
    lesson="lesson-456"
)

for attempt in response.attempts:
    print(f"Attempt {attempt.attempt}: {attempt.score} ({attempt.score_status})")
```

## Notes

- A 'Lesson' in this context is a ComponentResource object with an associated Resource
- For Assessment Bank lessons, review results with care as each attempt may represent a different sub-test

