## PowerPath — Assessment - Create New Attempt

### POST /powerpath/createNewAttempt

- Method: POST
- Auth: OAuth2 Client Credentials (Bearer token)

Creates a new attempt for a student in a lesson if the current attempt is completed.

### Request Body

```json
{
  "student": "student-sourced-id",
  "lesson": "lesson-component-resource-id"
}
```

### Assessment Bank Behavior

For Assessment Bank lessons:
- Updates state to associate new attempt with a different sub-resource
- Uses round-robin logic over sub-resources
- Different test may be served on subsequent attempts

### Response

```json
{
  "attempt": {
    "attempt": 2,
    "score": 0,
    "scoreStatus": "not submitted",
    "xp": null,
    "startedAt": "2024-01-15T10:00:00Z",
    "completedAt": null
  }
}
```

### Python Usage

```python
from timeback import Timeback
from timeback.models.request import TimebackCreateNewAttemptRequest

client = Timeback()

request = TimebackCreateNewAttemptRequest(
    student="student-id",
    lesson="lesson-component-resource-id",
)

response = client.powerpath.create_new_attempt(request)

print(f"Attempt #{response.attempt.attempt}")
print(f"Status: {response.attempt.scoreStatus}")
```

