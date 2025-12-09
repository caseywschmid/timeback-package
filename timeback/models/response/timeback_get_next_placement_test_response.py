"""Response model for getting the next placement test.

GET /powerpath/placement/getNextPlacementTest
"""

from typing import Optional
from pydantic import BaseModel, Field


class TimebackGetNextPlacementTestResponse(BaseModel):
    """Response model for getting the next placement test.
    
    Returns information about the next placement test a student should take.
    
    Attributes:
        - exhaustedTests (bool): Whether the student has exhausted all placement tests
        - gradeLevel (str, optional): The grade level of the next placement test.
          Can be null if no more tests to take. Valid values: "-1", "0"..."13"
        - lesson (str, optional): The sourcedId of the next placement test (ComponentResource).
          Null if student has completed all tests or scored < 90 on last test.
        - onboarded (bool): Whether the student has completed the onboarding process.
          True if they completed all tests or scored < 90 on last test.
          False if they haven't started or scored >= 90 and have more tests to take.
        - availableTests (int): The number of placement tests available for the subject.
    """

    exhaustedTests: bool = Field(
        ..., description="Whether the student has exhausted all placement tests"
    )
    gradeLevel: Optional[str] = Field(
        None, description="The grade level of the next placement test"
    )
    lesson: Optional[str] = Field(
        None, description="The sourcedId of the next placement test (ComponentResource)"
    )
    onboarded: bool = Field(
        ..., description="Whether the student has completed the onboarding process for the subject"
    )
    availableTests: int = Field(
        ..., description="The number of placement tests available for the subject"
    )

