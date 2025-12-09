## PowerPath — Placement - Get Next Placement Test

### GET /powerpath/placement/getNextPlacementTest

- Method: GET
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Get the next placement test the student should take for a subject.

Returns the next placement test for the student in a subject:
- If the student has completed all placement tests for the subject, the lesson will be null and exhaustedTests = true.
- If the student hasn't completed a single placement test, returns the first placement test.
- If the student scored < 90 on the last completed test, returns null for lesson (onboarded = true).
- If the student scored >= 90 on the last test, returns the next available placement test.

A 'Lesson' in this context is a ComponentResource object which has a Resource object with `metadata.lessonType = "placement"` associated with it.

Query params:

- `student` (string, required): The sourcedId of the student
- `subject` (string, required): The subject name. Valid values: `Reading`, `Language`, `Vocabulary`, `Social Studies`, `Writing`, `Science`, `FastMath`, `Math`

Successful response (HTTP 200):

- Body: `{ "exhaustedTests": boolean, "gradeLevel": string | null, "lesson": string | null, "onboarded": boolean, "availableTests": number }`
- Fields:
  - `exhaustedTests`: Whether the student has exhausted all placement tests
  - `gradeLevel`: The grade level of the next placement test (can be null)
  - `lesson`: The sourcedId of the next placement test ComponentResource (can be null)
  - `onboarded`: Whether the student has completed the onboarding process
  - `availableTests`: The number of placement tests available for the subject

Error responses:

- 400/422: Request/validation → raises `RequestError`
- 401: Unauthorized → raises `AuthError`
- 403: Forbidden → raises `RequestError`
- 404: Not Found → raises `NotFoundError`
- 429: Too Many Requests → raises `RateLimitError`
- 5xx: Server errors → raises `ServerError`

Python usage:

```python
from timeback import Timeback
from timeback.models.request import TimebackGetNextPlacementTestRequest
from timeback.enums import TimebackSubject

client = Timeback()

# Get next placement test for a student in Reading
request = TimebackGetNextPlacementTestRequest(
    student="student-sourced-id",
    subject=TimebackSubject.READING,
)
response = client.powerpath.get_next_placement_test(request)

print(f"Exhausted Tests: {response.exhaustedTests}")
print(f"Next Lesson: {response.lesson}")
print(f"Onboarded: {response.onboarded}")

if response.lesson:
    print(f"Student should take placement test: {response.lesson}")
elif response.onboarded:
    print("Student has been placed in the subject.")
```

Notes:

- The `subject` parameter uses the `TimebackSubject` enum which maps to the API's expected string values.
- A `lesson` of `null` can mean either:
  1. The student has exhausted all tests (`exhaustedTests = true`)
  2. The student scored < 90 on the last test and is now onboarded (`onboarded = true`)
- Check `exhaustedTests` and `onboarded` to determine the student's placement status.

