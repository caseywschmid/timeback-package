"""Response model for resetting an attempt.

POST /powerpath/resetAttempt
"""

from pydantic import BaseModel, Field


class TimebackResetAttemptResponse(BaseModel):
    """Response model for resetting a student's attempt.
    
    Attributes:
        - success (bool): Whether the reset was successful
        - score (float): The reset score (always 0)
    """

    success: bool = Field(..., description="Whether reset was successful")
    score: float = Field(..., description="Reset score (always 0)")

