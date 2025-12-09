"""Response model for getting current level.

GET /powerpath/placement/getCurrentLevel
"""

from typing import Optional
from pydantic import BaseModel, Field


class TimebackGetCurrentLevelResponse(BaseModel):
    """Response model for getting the current level of a student in placement.
    
    The level is determined by the last completed placement test's grade level,
    starting from the lowest grade level available for the subject's placement tests.
    
    Attributes:
        - gradeLevel (str, optional): The grade level of the current level in the subject.
          Can be null if no level has been determined yet.
          Valid values: "-1", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"
        - onboarded (bool): Whether the student has completed the onboarding process for the subject.
          True means they either completed and passed all placement tests or got a score < 90 on last test.
          False means they haven't completed tests yet or scored >= 90 and have more tests to take.
        - availableTests (int): The number of placement tests available for the subject.
    """

    gradeLevel: Optional[str] = Field(
        None, description="The grade level of the current level in the subject"
    )
    onboarded: bool = Field(
        ..., description="Whether the student has completed the onboarding process for the subject"
    )
    availableTests: int = Field(
        ..., description="The number of placement tests available for the subject"
    )

