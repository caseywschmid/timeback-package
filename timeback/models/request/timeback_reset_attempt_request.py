"""Request model for resetting an attempt.

POST /powerpath/resetAttempt
"""

from pydantic import BaseModel, ConfigDict, Field


class TimebackResetAttemptRequest(BaseModel):
    """Request model for resetting a student's attempt.
    
    Resets the attempt for the given PowerPath lesson:
    - Soft-deletes previous question responses
    - Resets test score to 0
    - Updates scoreStatus to "not submitted"
    
    For Assessment Bank lessons, this keeps the user state in the
    same bank test for the current attempt.
    
    Attributes:
        - student (str): The sourcedId of the student
        - lesson (str): The sourcedId of the lesson (ComponentResource)
    """

    model_config = ConfigDict(populate_by_name=True)

    student: str = Field(..., description="Student sourcedId")
    lesson: str = Field(..., description="Lesson (ComponentResource) sourcedId")

