"""Response model for getting next question.

GET /powerpath/getNextQuestion
"""

from pydantic import BaseModel, Field
from timeback.models.response.timeback_assessment_progress_response import TimebackTestQuestion


class TimebackNextQuestionResponse(BaseModel):
    """Response model for getting the next question in a PowerPath-100 lesson.
    
    Note: This endpoint only works with lessons of type 'powerpath-100'.
    
    Attributes:
        - score (float): Current PowerPath score in this lesson
        - question (TimebackTestQuestion): The next question data
    """

    score: float = Field(..., description="Current PowerPath score")
    question: TimebackTestQuestion = Field(..., description="Next question data")

