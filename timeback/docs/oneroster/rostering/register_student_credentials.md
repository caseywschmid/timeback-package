## OneRoster — Rostering - Register Student Credentials

### POST /ims/oneroster/rostering/v1p2/users/{userId}/credentials

- Method: POST
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Register student credentials for third-party applications

Request model:

- `TimebackRegisterStudentCredentialsRequest` with required fields:
  - `user_id` (string) — The sourcedId of the user (used in path)
  - `application_name` (string) — The name of the third-party application (min length: 1)
  - `credentials` (TimebackCredentials) — Credentials object containing:
    - `username` (string) — The username for the third-party application
    - `password` (string) — The password for the third-party application

Path params (extracted from request):

- `userId` (string, required): The sourcedId of the user

Request body (application/json, extracted from request):

```json
{
  "applicationName": "string",
  "credentials": {
    "username": "string",
    "password": "string"
  }
}
```

Successful response (HTTP 200 or 201):

- HTTP 200: Student credentials updated successfully
- HTTP 201: Student credentials created successfully
- Body: `TimebackRegisterStudentCredentialsResponse` with fields:
  - `user_profile_id` (string) — The user profile ID
  - `credential_id` (string) — The credential ID
  - `message` (string) — Confirmation message

Error responses:

- 400: Invalid request → raises `RequestError`
- 401: Unauthorized → raises `AuthError`
- 403: Forbidden → raises `RequestError`
- 404: Not Found → raises `NotFoundError`
- 422: Unprocessable Entity / Validation Error → raises `RequestError`
- 429: Too Many Requests → raises `RateLimitError`
- 5xx: Server errors → raises `ServerError`

Python usage:

```python
from timeback import Timeback
from timeback.models.request import (
    TimebackRegisterStudentCredentialsRequest,
    TimebackCredentials,
)

client = Timeback()
user_id = "31129aea-12b2-4e9e-a6e5-f5c8b712d674"
application_name = "PowerPath"
credentials = TimebackCredentials(username="student123", password="securepass456")

request = TimebackRegisterStudentCredentialsRequest(
    user_id=user_id, 
    application_name=application_name, 
    credentials=credentials
)
resp = client.oneroster.rostering.register_student_credentials(request)

print(f"User Profile ID: {resp.user_profile_id}")
print(f"Credential ID: {resp.credential_id}")
print(f"Message: {resp.message}")
```

Notes:

- The endpoint returns HTTP 200 if credentials are updated, or HTTP 201 if credentials are created for the first time.
- The response includes a `user_profile_id`, `credential_id`, and a confirmation `message`.
- Credentials are securely stored for third-party application authentication.
- The `application_name` must be at least 1 character long.
