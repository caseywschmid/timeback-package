"""Response model for getting all attempts.

GET /powerpath/getAttempts
"""

from typing import List
from pydantic import BaseModel, Field
from timeback.models.response.timeback_create_new_attempt_response import TimebackAttemptData


class TimebackGetAttemptsResponse(BaseModel):
    """Response model for getting all attempts for a student in a lesson.
    
    For Assessment Bank lessons, each attempt may represent a different
    sub-test of the bank.
    
    Attributes:
        - attempts (List[TimebackAttemptData]): List of all attempts
    """

    attempts: List[TimebackAttemptData] = Field(..., description="List of all attempts")

