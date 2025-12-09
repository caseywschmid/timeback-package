## PowerPath — Screening - Get Session

### GET /powerpath/screening/session/{userId}

- Method: GET
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Get screening session information for a user.

Returns session credentials and status needed to start or continue a screening test via NWEA.

Path params:

- `userId` (string, required): The sourcedId of the user

Successful response (HTTP 200):

- Body: Session object with the following fields:
  - `nweaStudentId` (string, UUID): The NWEA student ID
  - `createdOn` (string, ISO datetime): When the session was created
  - `password` (string): Password for the screening session
  - `name` (string): Name associated with the session
  - `proctorId` (string, UUID): The proctor ID
  - `pin` (string): PIN for the screening session
  - `testSessionId` (string, UUID): The test session ID
  - `status` (string): "active" or "inactive"
  - `assignment` (object): Assignment information
    - `assignedTestKey` (string, nullable): Key of the assigned test
    - `status` (string, nullable): Internal status: "enqueued", "assigned", "in_progress", "blocked", "completed", "abandoned", "failed"
    - `nweaStatus` (string, nullable): NWEA status: "ENQUEUED", "AWAITING_STUDENT", "IN_PROGRESS", "PAUSED", "SUSPENDED", "TERMINATED", "ABANDONED", "COMPLETED", "FAILED"
  - `termId` (string): The term ID

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

# Get screening session for a user
session = client.powerpath.get_screening_session("user-sourced-id")

print(f"Session Status: {session.status}")
print(f"PIN: {session.pin}")
print(f"Password: {session.password}")

if session.assignment.status:
    print(f"Test Assignment: {session.assignment.assignedTestKey}")
    print(f"Assignment Status: {session.assignment.status}")
```

Notes:

- Use the `pin` and `password` to authenticate students for NWEA screening tests.
- The `assignment.status` tracks internal status while `assignment.nweaStatus` shows the NWEA-specific status.
- A `null` assignment status indicates no test has been assigned yet.

