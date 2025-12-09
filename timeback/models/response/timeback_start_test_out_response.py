"""Response model for starting a test-out assignment.

POST /powerpath/lessonPlans/startTestOut
"""

from typing import Literal
from pydantic import BaseModel, Field


class TimebackStartTestOutResponse(BaseModel):
    """Response model for starting a test-out assignment.
    
    Returns assignment info for the created or existing test-out assignment.
    
    Attributes:
        - assignmentId (str): The test assignment ID
        - lessonId (str): The component resource ID (lesson)
        - resourceId (str): The resource ID
        - status (str): Whether assignment was "created" or "existing" (reused)
    """

    assignmentId: str = Field(..., description="The test assignment ID")
    lessonId: str = Field(..., description="The component resource ID (lesson)")
    resourceId: str = Field(..., description="The resource ID")
    status: Literal["created", "existing"] = Field(
        ..., description="Whether a new assignment was created or existing was reused"
    )

