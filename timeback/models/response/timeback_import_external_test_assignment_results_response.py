"""Response model for importing external test assignment results.

GET /powerpath/importExternalTestAssignmentResults
"""

from typing import Optional
from pydantic import BaseModel, Field


class TimebackExternalTestCredentials(BaseModel):
    """Credentials for accessing the assigned test on external tool.
    
    Attributes:
        - email (str): Email for authentication
        - password (str): Password for authentication
    """

    email: str = Field(..., description="Email for authentication")
    password: str = Field(..., description="Password for authentication")


class TimebackImportExternalTestAssignmentResultsResponse(BaseModel):
    """Response model for importing external test assignment results.
    
    Contains information about the test assignment and its current state.
    
    Attributes:
        - lessonType (str): The type of lesson. Valid values: "test-out", "placement", "unit-test"
        - lessonId (str, optional): The sourcedId of the lesson (ComponentResource)
        - toolProvider (str, optional): The tool provider for the lesson
        - finalized (bool): Whether the Test has been finalized in the current attempt
        - attempt (int): The attempt number
        - credentials (TimebackExternalTestCredentials, optional): Credentials for external tool access
        - assignmentId (str, optional): The id of the assignment on external tool
        - classId (str, optional): The id of the class on external tool
        - testUrl (str, optional): The URL of the test on external tool
        - testId (str, optional): The id of the test on external tool
    """

    lessonType: str = Field(..., description="The type of lesson")
    lessonId: Optional[str] = Field(None, description="The sourcedId of the lesson")
    toolProvider: Optional[str] = Field(None, description="The tool provider for the lesson")
    finalized: bool = Field(..., description="Whether the Test has been finalized")
    attempt: int = Field(..., description="The attempt number")
    credentials: Optional[TimebackExternalTestCredentials] = Field(
        None, description="Credentials for external tool access"
    )
    assignmentId: Optional[str] = Field(None, description="The assignment id on external tool")
    classId: Optional[str] = Field(None, description="The class id on external tool")
    testUrl: Optional[str] = Field(None, description="The URL of the test on external tool")
    testId: Optional[str] = Field(None, description="The test id on external tool")

