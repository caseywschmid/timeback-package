## OneRoster — Rostering - Decrypt Credential

### POST /ims/oneroster/rostering/v1p2/users/{userId}/credentials/{credentialId}/decrypt

- Method: POST
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Decrypt and return the password for a specific user credential

Request model:

- `TimebackDecryptCredentialRequest` with required fields:
  - `user_id` (string) — The sourcedId of the user (used in path)
  - `credential_id` (string) — The sourcedId of the credential to decrypt (used in path)

Path params (extracted from request):

- `userId` (string, required): The sourcedId of the user
- `credentialId` (string, required): The sourcedId of the credential to decrypt

Request body:

- None (this endpoint does not require a request body)

Successful response (HTTP 200):

- Body: `TimebackDecryptCredentialResponse` with fields:
  - `password` (string) — The decrypted password

Error responses:

- 400: Invalid request → raises `RequestError`
- 401: Unauthorized → raises `AuthError`
- 403: Forbidden → raises `RequestError`
- 404: Credential not found → raises `NotFoundError`
- 422: Unprocessable Entity / Validation Error → raises `RequestError`
- 429: Too Many Requests → raises `RateLimitError`
- 5xx: Server errors → raises `ServerError`

Python usage:

```python
from timeback import Timeback
from timeback.models.request import TimebackDecryptCredentialRequest

client = Timeback()
user_id = "31129aea-12b2-4e9e-a6e5-f5c8b712d674"
credential_id = "cred-123-456-789"

request = TimebackDecryptCredentialRequest(
    user_id=user_id, 
    credential_id=credential_id
)
resp = client.oneroster.rostering.decrypt_credential(request)

print(f"Decrypted Password: {resp.password}")
```

Notes:

- This endpoint decrypts and returns the password for a previously registered credential.
- The credential must have been registered using the `register_student_credentials` endpoint.
- The response contains only the decrypted password as a string.
- This is a sensitive operation and should be used with appropriate security measures.
- A 404 error will be raised if the credential is not found for the specified user.

Security Considerations:

- Ensure proper authentication and authorization before calling this endpoint.
- The decrypted password should be handled securely and not logged or stored in plain text.
- Consider using this endpoint only when absolutely necessary for third-party application integration.
