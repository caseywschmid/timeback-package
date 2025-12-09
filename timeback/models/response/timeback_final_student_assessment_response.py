"""Response model for finalizing student assessment.

POST /powerpath/finalStudentAssessmentResponse
"""

from pydantic import BaseModel, Field


class TimebackFinalStudentAssessmentResponse(BaseModel):
    """Response model for finalizing a student assessment.
    
    Attributes:
        - lessonType (str): Type of lesson (quiz, test-out, placement, unit-test)
        - finalized (bool): Whether the lesson was finalized in current attempt
        - attempt (int): The attempt number
    """

    lessonType: str = Field(
        ..., description="quiz, test-out, placement, or unit-test"
    )
    finalized: bool = Field(
        ..., description="Whether lesson was finalized in current attempt"
    )
    attempt: int = Field(..., description="Attempt number")

