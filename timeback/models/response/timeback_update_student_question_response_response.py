"""Response model for updating student question response.

PUT /powerpath/updateStudentQuestionResponse

Response varies by lessonType (discriminated union).
"""

from typing import Optional, Any
from pydantic import BaseModel, Field


class TimebackResponseResult(BaseModel):
    """Result of processing the student's response.
    
    Attributes:
        - isCorrect (bool): Whether the response is correct
        - score (float): Score for this response (0 or 1)
        - feedback (Any, optional): Optional feedback
    """

    isCorrect: bool = Field(..., description="Whether response is correct")
    score: float = Field(..., description="Score for this response")
    feedback: Optional[Any] = None


class TimebackUpdateStudentQuestionResponseResponse(BaseModel):
    """Response model for updating a student's question response.
    
    PUT /powerpath/updateStudentQuestionResponse
    
    Response structure varies by lessonType. Common fields for all:
    - lessonType: Type of lesson
    - questionResult: Assessment result for debugging
    
    Additional fields for powerpath-100:
    - powerpathScore, responseResult, accuracy, correctQuestions, etc.
    
    Attributes:
        - lessonType (str): quiz, test-out, placement, unit-test, or powerpath-100
        - questionResult (Any, optional): Assessment result for debugging
        - testResult (Any, optional): Test result for debugging (powerpath-100)
        - powerpathScore (float, optional): Updated PowerPath score (powerpath-100)
        - responseResult (TimebackResponseResult, optional): Response details (powerpath-100)
        - accuracy (float, optional): Accuracy percentage (powerpath-100)
        - correctQuestions (int, optional): Correct count (powerpath-100)
        - totalQuestions (int, optional): Total count (powerpath-100)
        - xp (float, optional): XP earned (powerpath-100)
        - multiplier (float, optional): XP multiplier (powerpath-100)
    """

    lessonType: str = Field(
        ..., description="quiz, test-out, placement, unit-test, or powerpath-100"
    )
    questionResult: Optional[Any] = Field(None, description="Assessment result for debugging")
    testResult: Optional[Any] = Field(None, description="Test result (powerpath-100)")
    powerpathScore: Optional[float] = Field(None, description="Updated PowerPath score")
    responseResult: Optional[TimebackResponseResult] = Field(
        None, description="Response result details"
    )
    accuracy: Optional[float] = Field(None, description="Accuracy percentage")
    correctQuestions: Optional[int] = Field(None, description="Correct questions count")
    totalQuestions: Optional[int] = Field(None, description="Total questions count")
    xp: Optional[float] = Field(None, description="XP earned")
    multiplier: Optional[float] = Field(None, description="XP multiplier")

