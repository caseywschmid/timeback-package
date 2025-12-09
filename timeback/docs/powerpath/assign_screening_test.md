## PowerPath — Screening - Assign Test

### POST /powerpath/screening/tests/assign

- Method: POST
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Assign a screening test to a user.

Assigns a screening test for a specific subject to a user. Returns the updated screening session with assignment details.

Request body (JSON):

- `userId` (string, required): The sourcedId of the user
- `subject` (string, required): The subject name. Valid values: `Math`, `Reading`, `Language`, `Science`

**Note**: The subject enum for screening tests is more limited than placement tests.

Successful response (HTTP 200):

- Returns a `TimebackScreeningSession` object (same structure as `get_screening_session`)
- Includes:
  - `nweaStudentId`, `password`, `pin`: Credentials for the test
  - `assignment`: Updated assignment info with test key and status
  - `status`: Session status ("active" or "inactive")

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
from timeback.models.request import TimebackAssignScreeningTestRequest

client = Timeback()

# Assign a Reading screening test to a user
request = TimebackAssignScreeningTestRequest(
    userId="user-sourced-id",
    subject="Reading",  # Math, Reading, Language, or Science
)
session = client.powerpath.assign_screening_test(request)

print(f"Test assigned: {session.assignment.assignedTestKey}")
print(f"Status: {session.assignment.status}")
print(f"PIN: {session.pin}")
print(f"Password: {session.password}")
```

Notes:

- Only four subjects are supported for screening tests: Math, Reading, Language, Science.
- The returned session includes all credentials needed to start the NWEA screening test.
- After assigning, the `assignment.status` will typically be "assigned" or "enqueued".

