"""Request model for making an external test assignment.

POST /powerpath/makeExternalTestAssignment
"""

from typing import Optional
from pydantic import BaseModel, Field


class TimebackMakeExternalTestAssignmentRequest(BaseModel):
    """Request model for making an external test assignment.
    
    Makes an external test assignment for a student. Applies to 'test-out', 
    'placement', and 'unit-test' lessons.
    
    Attributes:
        Required:
            - student (str): The sourcedId of the student
            - lesson (str): The sourcedId of the lesson (ComponentResource)
            
        Optional:
            - applicationName (str): The name of the application to use for 
              authenticating on the external tool
            - testId (str): The specific test ID to assign for MasteryTrack tool provider.
              If provided, overrides subject+grade selection.
            - skipCourseEnrollment (bool): When true, skips automatic course enrollment 
              after test completion. Only applies to the current attempt.
    """

    student: str = Field(..., description="The sourcedId of the student")
    lesson: str = Field(..., description="The sourcedId of the lesson (ComponentResource)")
    applicationName: Optional[str] = Field(
        None, description="The name of the application for authenticating on the external tool"
    )
    testId: Optional[str] = Field(
        None, description="The specific test ID to assign (for MasteryTrack, overrides subject+grade)"
    )
    skipCourseEnrollment: Optional[bool] = Field(
        None, description="When true, skips automatic course enrollment after test completion"
    )

