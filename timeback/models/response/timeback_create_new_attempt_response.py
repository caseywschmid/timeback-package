"""Response model for creating a new attempt.

POST /powerpath/createNewAttempt
"""

from typing import Optional
from pydantic import BaseModel, Field


class TimebackAttemptData(BaseModel):
    """Data about a single attempt.
    
    Attributes:
        - attempt (int, optional): The attempt number
        - score (float): The current score for this attempt
        - scoreStatus (str): Status of this attempt
        - xp (float, optional): XP earned in this attempt
        - startedAt (str, optional): When this attempt was started
        - completedAt (str, optional): When this attempt was completed
    """

    attempt: Optional[int] = Field(None, description="Attempt number")
    score: float = Field(..., description="Current score")
    scoreStatus: str = Field(
        ..., description="exempt, fully graded, not submitted, partially graded, submitted"
    )
    xp: Optional[float] = Field(None, description="XP earned")
    startedAt: Optional[str] = Field(None, description="Start timestamp")
    completedAt: Optional[str] = Field(None, description="Completion timestamp")


class TimebackCreateNewAttemptResponse(BaseModel):
    """Response model for creating a new attempt.
    
    Attributes:
        - attempt (TimebackAttemptData): The new attempt data
    """

    attempt: TimebackAttemptData = Field(..., description="The new attempt data")

