"""Response model for registering student credentials for third-party applications.

Represents the body returned by:
- POST /ims/oneroster/rostering/v1p2/users/{userId}/credentials

Per spec: HTTP 200 (update) or 201 (create) with userProfileId, credentialId, and message.
"""

from pydantic import BaseModel, ConfigDict, Field


class TimebackRegisterStudentCredentialsResponse(BaseModel):
    """Response model for registering student credentials for third-party applications.

    Attributes:
        - user_profile_id (str): The user profile ID
        - credential_id (str): The credential ID
        - message (str): Confirmation message
    """

    model_config = ConfigDict(populate_by_name=True)

    user_profile_id: str = Field(..., description="The user profile ID", alias="userProfileId")
    credential_id: str = Field(..., description="The credential ID", alias="credentialId")
    message: str = Field(..., description="Confirmation message")

