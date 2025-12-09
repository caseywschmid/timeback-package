"""Response model for getting assessment progress.

GET /powerpath/getAssessmentProgress

Returns the progress a student has made in a PowerPath lesson.
"""

from typing import List, Optional, Any, Dict, Union
from pydantic import BaseModel, Field


class TimebackQuestionContent(BaseModel):
    """QTI content of a question."""

    type: Optional[str] = None
    rawXml: str = Field(..., description="Raw XML question in QTI format")


class TimebackQuestionResult(BaseModel):
    """Result of evaluating a question response."""

    outcomes: Optional[Dict[str, str]] = None
    score: float = Field(..., description="Score assigned to the question")
    feedback: str = Field(..., description="Feedback for the question")


class TimebackTestQuestion(BaseModel):
    """A PowerPath test question with response data.
    
    Attributes:
        - id (str): Question ID in the test
        - index (int): Question index in the test
        - title (str): Question title
        - url (str): URL of the QTI question
        - difficulty (str): easy, medium, or hard
        - humanApproved (bool, optional): Whether human approved
        - content (dict, optional): QTI content
        - response (Any, optional): Student's response
        - responses (dict, optional): Multiple response values
        - correct (bool, optional): Whether response is correct
        - result (dict, optional): Evaluation result
        - learningObjectives (list, optional): Associated learning objectives
    """

    id: str = Field(..., description="Question ID")
    index: int = Field(..., description="Question index")
    title: str = Field(..., description="Question title")
    url: str = Field(..., description="QTI question URL")
    difficulty: str = Field("medium", description="easy, medium, or hard")
    humanApproved: Optional[bool] = None
    content: Optional[TimebackQuestionContent] = None
    response: Optional[Any] = None
    responses: Optional[Dict[str, Any]] = None
    correct: Optional[bool] = None
    result: Optional[TimebackQuestionResult] = None
    learningObjectives: Optional[List[str]] = None


class TimebackRemainingQuestionsPerDifficulty(BaseModel):
    """Remaining questions by difficulty for PowerPath100."""

    easy: int
    medium: int
    hard: int


class TimebackAssessmentProgressResponse(BaseModel):
    """Response model for getting assessment progress.
    
    GET /powerpath/getAssessmentProgress
    
    Structure varies based on lessonType. Common fields include:
    - lessonType, attempt, score, xp, multiplier, accuracy, etc.
    
    For powerpath-100 lessons, includes remainingQuestionsPerDifficulty
    and seenQuestions. For other lessons, includes questions array.
    
    Attributes:
        - lessonType (str): quiz, test-out, placement, unit-test, or powerpath-100
        - finalized (bool, optional): Whether lesson is finalized
        - attempt (int): Attempt number
        - score (float, optional): Current score
        - xp (float, optional): XP earned
        - multiplier (float, optional): XP multiplier
        - accuracy (float, optional): Accuracy percentage
        - correctQuestions (int, optional): Correct questions count
        - totalQuestions (int, optional): Total questions count
        - questions (list, optional): Question data (non-powerpath-100)
        - toolProvider (str, optional): External tool provider
        - enrollmentFailed (bool, optional): Whether auto-enrollment failed
        - remainingQuestionsPerDifficulty (dict, optional): For powerpath-100
        - seenQuestions (list, optional): For powerpath-100
    """

    lessonType: str = Field(..., description="Lesson type")
    finalized: Optional[bool] = None
    attempt: int = Field(..., description="Attempt number")
    score: Optional[float] = None
    xp: Optional[float] = None
    multiplier: Optional[float] = None
    accuracy: Optional[float] = None
    correctQuestions: Optional[int] = None
    totalQuestions: Optional[int] = None
    questions: Optional[List[TimebackTestQuestion]] = None
    toolProvider: Optional[str] = None
    enrollmentFailed: Optional[bool] = None
    remainingQuestionsPerDifficulty: Optional[TimebackRemainingQuestionsPerDifficulty] = None
    seenQuestions: Optional[List[TimebackTestQuestion]] = None

