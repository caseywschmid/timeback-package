"""Request model for decrypting a user credential.

POST /ims/oneroster/rostering/v1p2/users/{userId}/credentials/{credentialId}/decrypt
"""

from pydantic import BaseModel, ConfigDict, Field


class TimebackDecryptCredentialRequest(BaseModel):
    """Request model for decrypting a user credential.
    
    Attributes:
        Required:
            - user_id (str): The sourcedId of the user
            - credential_id (str): The sourcedId of the credential to decrypt
    """
    
    model_config = ConfigDict(populate_by_name=True)
    
    user_id: str = Field(..., description="The sourcedId of the user", alias="userId")
    credential_id: str = Field(
        ..., description="The sourcedId of the credential to decrypt", alias="credentialId"
    )
