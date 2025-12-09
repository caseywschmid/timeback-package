## PowerPath — Placement - Get Current Level

### GET /powerpath/placement/getCurrentLevel

- Method: GET
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Get the current level of the student in a placement process.

The level is determined by the last completed placement test's grade level, starting from the lowest grade level available for the subject's placement tests. As the student completes placement tests and attains scores of 90 or greater, their level updates to the next level available for the subject.

Also returns the `onboarded` boolean that indicates if the student completed the onboarding process for the subject:
- `onboarded = true` means they either completed and passed all placement tests or they have gotten a score smaller than 90 in the last completed placement test.
- `onboarded = false` means they haven't completed placement tests yet or have achieved a score of 90 or greater in the last completed placement test and there are more tests to take.

Query params:

- `student` (string, required): The sourcedId of the student
- `subject` (string, required): The subject name. Valid values: `Reading`, `Language`, `Vocabulary`, `Social Studies`, `Writing`, `Science`, `FastMath`, `Math`

Successful response (HTTP 200):

- Body: `{ "gradeLevel": string | null, "onboarded": boolean, "availableTests": number }`
- Fields:
  - `gradeLevel`: The grade level of the current level in the subject (can be null if not yet determined). Valid values: "-1", "0", "1"..."13"
  - `onboarded`: Whether the student has completed the onboarding process for the subject
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
from timeback.models.request import TimebackGetCurrentLevelRequest
from timeback.enums import TimebackSubject

client = Timeback()

# Get current level for a student in Reading
request = TimebackGetCurrentLevelRequest(
    student="student-sourced-id",
    subject=TimebackSubject.READING,
)
response = client.powerpath.get_current_level(request)

print(f"Grade Level: {response.gradeLevel}")
print(f"Onboarded: {response.onboarded}")
print(f"Available Tests: {response.availableTests}")

if response.onboarded:
    print("Student has completed the onboarding process.")
else:
    print(f"Student has {response.availableTests} more test(s) to take.")
```

Notes:

- The `subject` parameter uses the `TimebackSubject` enum which maps to the API's expected string values.
- A `gradeLevel` of `null` indicates the student hasn't started placement tests yet.
- The `availableTests` count will be 0 when the student has completed all placement tests for the subject.

