## PowerPath — Screening - Get Results

### GET /powerpath/screening/results/{userId}

- Method: GET
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Get screening test results for a user.

Returns screening test results across all subjects. Each subject maps to either a result object or null if no screening test has been completed for that subject.

Path params:

- `userId` (string, required): The sourcedId of the user

Successful response (HTTP 200):

- Body: A dictionary mapping subject names to screening results (or null)
- Example:
  ```json
  {
    "Reading": {
      "grade": "5",
      "ritScore": 210.5,
      "testName": "Reading Screening Test",
      "completedAt": "2024-01-15T10:30:00Z"
    },
    "Math": null,
    "Language": {
      "grade": "4",
      "ritScore": 195.0,
      "testName": "Language Screening",
      "completedAt": "2024-01-10T09:00:00Z"
    }
  }
  ```
- Result object fields:
  - `grade`: The grade level determined by the screening test
  - `ritScore`: The RIT score achieved on the screening test
  - `testName`: The name of the screening test
  - `completedAt`: ISO timestamp when the test was completed

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

client = Timeback()

# Get screening results for a user
response = client.powerpath.get_screening_results("user-sourced-id")

for subject, result in response.root.items():
    if result:
        print(f"{subject}: Grade {result.grade}, RIT Score {result.ritScore}")
    else:
        print(f"{subject}: No screening test completed")
```

Notes:

- The response uses a `RootModel` pattern, so access the underlying dictionary via `.root`.
- Subjects without completed screening tests will have `null` values.
- RIT (Rasch Unit) scores are standardized scores used to measure student achievement.

