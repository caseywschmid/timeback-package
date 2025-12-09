"""Response model for making an external test assignment.

POST /powerpath/makeExternalTestAssignment
"""

from typing import Optional
from pydantic import BaseModel, Field

from timeback.models.response.timeback_import_external_test_assignment_results_response import (
    TimebackExternalTestCredentials,
)


class TimebackMakeExternalTestAssignmentResponse(BaseModel):
    """Response model for making an external test assignment.
    
    Contains the assignment details and credentials needed to access the test.
    
    Attributes:
        - toolProvider (str): The tool provider. Valid values: "edulastic", "mastery-track"
        - lessonType (str): The type of lesson. Valid values: "test-out", "placement", "unit-test"
        - attempt (int): The attempt number
        - credentials (TimebackExternalTestCredentials, optional): Credentials for external tool access
        - assignmentId (str, optional): The id of the assignment on external tool
        - classId (str, optional): The id of the class on external tool (may be empty)
        - testUrl (str, optional): The URL of the test on external tool
        - testId (str, optional): The id of the test on external tool
    """

    toolProvider: str = Field(..., description="The tool provider")
    lessonType: str = Field(..., description="The type of lesson")
    attempt: int = Field(..., description="The attempt number")
    credentials: Optional[TimebackExternalTestCredentials] = Field(
        None, description="Credentials for external tool access"
    )
    assignmentId: Optional[str] = Field(None, description="The assignment id on external tool")
    classId: Optional[str] = Field(None, description="The class id on external tool")
    testUrl: Optional[str] = Field(None, description="The URL of the test on external tool")
    testId: Optional[str] = Field(None, description="The test id on external tool")

