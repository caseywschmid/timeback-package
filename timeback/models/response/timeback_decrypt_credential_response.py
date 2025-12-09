"""Response model for decrypting a user credential.

Represents the body returned by:
- POST /ims/oneroster/rostering/v1p2/users/{userId}/credentials/{credentialId}/decrypt

Per spec: HTTP 200 with decrypted password.
"""

from pydantic import BaseModel, Field


class TimebackDecryptCredentialResponse(BaseModel):
    """Response model for decrypting a user credential.

    Attributes:
        - password (str): The decrypted password
    """

    password: str = Field(..., description="The decrypted password")
