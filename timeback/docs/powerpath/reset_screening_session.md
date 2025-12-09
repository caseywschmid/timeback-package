## PowerPath — Screening - Reset Screening Session

### POST /powerpath/screening/session/reset

- Method: POST
- Auth: OAuth2 Client Credentials (Bearer token)

Resets the screening session for a user, allowing them to restart screening tests.

### Request Body

```json
{
  "userId": "user-sourced-id"
}
```

**Required fields:**
- `userId` (string): The sourcedId of the user

### Response

- HTTP 204 No Content (no response body)

### Python Usage

```python
from timeback import Timeback

client = Timeback()

# Reset screening session for a user
client.powerpath.reset_screening_session("user-sourced-id")

# Returns None (204 No Content)
```

### Notes

- This operation allows a user to restart screening tests
- After reset, the user's screening session state is cleared
- This does not delete historical screening results

