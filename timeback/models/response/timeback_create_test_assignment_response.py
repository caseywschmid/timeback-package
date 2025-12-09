"""Response model for creating a test assignment.

POST /powerpath/test-assignments
"""

from pydantic import BaseModel, Field


class TimebackCreateTestAssignmentResponse(BaseModel):
    """Response model for creating a test assignment.
    
    Attributes:
        - assignmentId (str): The test assignment ID
        - lessonId (str): The component resource ID (unlisted lesson)
        - resourceId (str): The resource ID created
    """

    assignmentId: str = Field(..., description="Test assignment ID")
    lessonId: str = Field(..., description="Component resource ID")
    resourceId: str = Field(..., description="Resource ID")

