"""Request model for finalizing student assessment.

POST /powerpath/finalStudentAssessmentResponse
"""

from pydantic import BaseModel, ConfigDict, Field


class TimebackFinalStudentAssessmentRequest(BaseModel):
    """Request model for finalizing a student assessment.
    
    Finalizes a lesson of type quiz, test-out, or placement after
    all questions have been answered. Evaluates responses and
    updates scores.
    
    Attributes:
        - student (str): The sourcedId of the student
        - lesson (str): The sourcedId of the lesson (ComponentResource)
    """

    model_config = ConfigDict(populate_by_name=True)

    student: str = Field(..., description="Student sourcedId")
    lesson: str = Field(..., description="Lesson (ComponentResource) sourcedId")

