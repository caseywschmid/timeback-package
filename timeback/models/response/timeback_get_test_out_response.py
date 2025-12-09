"""Response model for getting test-out information.

GET /powerpath/testOut

**DEPRECATED**: This endpoint is deprecated. Use GET /powerpath/lessonPlans/getCourseProgress instead.
"""

from typing import Optional
from pydantic import BaseModel, Field

from timeback.models.response.timeback_import_external_test_assignment_results_response import (
    TimebackExternalTestCredentials,
)


class TimebackGetTestOutResponse(BaseModel):
    """Response model for getting test-out information.
    
    **DEPRECATED**: Use get_course_progress instead.
    
    Contains the test-out lesson reference and status for a student and course.
    
    Attributes:
        - lessonType (str): Always "test-out"
        - lessonId (str, optional): The id of the testOut lesson. Null if no test-out found.
        - finalized (bool): Whether the Test Out has been finalized
        - toolProvider (str, optional): The tool provider for the testOut lesson
        - attempt (int, optional): The attempt number
        - credentials (TimebackExternalTestCredentials, optional): Credentials for external tool
        - assignmentId (str, optional): The assignment id on external tool
        - classId (str, optional): The class id on external tool
        - testUrl (str, optional): The URL of the test on external tool
        - testId (str, optional): The test id on external tool
    """

    lessonType: str = Field(..., description="The lesson type (always 'test-out')")
    lessonId: Optional[str] = Field(None, description="The id of the testOut lesson")
    finalized: bool = Field(..., description="Whether the Test Out has been finalized")
    toolProvider: Optional[str] = Field(None, description="The tool provider for the testOut lesson")
    attempt: Optional[int] = Field(None, description="The attempt number")
    credentials: Optional[TimebackExternalTestCredentials] = Field(
        None, description="Credentials for external tool access"
    )
    assignmentId: Optional[str] = Field(None, description="The assignment id on external tool")
    classId: Optional[str] = Field(None, description="The class id on external tool")
    testUrl: Optional[str] = Field(None, description="The URL of the test on external tool")
    testId: Optional[str] = Field(None, description="The test id on external tool")

