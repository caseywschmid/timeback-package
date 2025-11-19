"""Request model for registering student credentials for third-party applications.

POST /ims/oneroster/rostering/v1p2/users/{userId}/credentials
"""

from pydantic import BaseModel, ConfigDict, Field


class TimebackCredentials(BaseModel):
    """Credentials object containing username and password.
    
    Attributes:
        - username (str): The username for the third-party application
        - password (str): The password for the third-party application
    """
    
    username: str = Field(..., description="The username for the third-party application")
    password: str = Field(..., description="The password for the third-party application")


class TimebackRegisterStudentCredentialsRequest(BaseModel):
    """Request model for registering student credentials for third-party applications.
    
    Attributes:
        Required:
            - user_id (str): The sourcedId of the user
            - application_name (str): The name of the third-party application
            - credentials (TimebackCredentials): The credentials object. See TimebackCredentials for structure.
    """
    
    model_config = ConfigDict(populate_by_name=True)
    
    user_id: str = Field(..., description="The sourcedId of the user", alias="userId")
    application_name: str = Field(
        ..., description="The name of the third-party application", alias="applicationName", min_length=1
    )
    credentials: TimebackCredentials = Field(
        ..., description="The credentials object containing username and password"
    )
