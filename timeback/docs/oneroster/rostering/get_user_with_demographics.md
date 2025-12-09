## OneRoster — Rostering - Get User with Demographics

### GET /ims/oneroster/rostering/v1p2/users/{sourcedId}/demographics

- Method: GET
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Fetch a specific OneRoster user with demographics data by `sourcedId`. If the corresponding record cannot be located, the API will return a 404 error code and message 'User not found.'
- Query params:
- `fields` (string, optional): Comma-separated field list (e.g., `sourcedId,username`)

Path params:

- `sourcedId` (string, required): The user's sourcedId

Successful response (HTTP 200):

- Body: `{ "user": User }`
- The `User` object includes (non-exhaustive):
  - required: `sourcedId`, `status`, `enabledUser`, `givenName`, `familyName`, `roles`, `agents`, `userProfiles`
  - optional: `username`, `userIds`, `middleName`, `primaryOrg`, `email`, `grades`, `dateLastModified`, `metadata`, etc.
- The user object will include demographics data associated with the user

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
from timeback.models.request import TimebackGetUserRequest, TimebackQueryParams

client = Timeback()

# Basic request without query params
request = TimebackGetUserRequest(sourced_id="<sourcedId>")
response = client.oneroster.rostering.get_user_with_demographics(request)

# With fields filter
query_params = TimebackQueryParams(fields=["sourcedId", "username"])
request_with_fields = TimebackGetUserRequest(
    sourced_id="<sourcedId>", 
    query_params=query_params
)
response_min = client.oneroster.rostering.get_user_with_demographics(request_with_fields)

print(response.user.sourcedId, response.user.givenName, response.user.familyName)
```

Notes:

- The client returns the full API response as `TimebackGetUserResponse` which contains a `user` field.
- The response model mirrors the API structure: `{ "user": User }`.
- This endpoint returns the same user structure as `get_user`, but includes demographics data.
- If the API omits required fields, validation will fail with a `ParseError`.

