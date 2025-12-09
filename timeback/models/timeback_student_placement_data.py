"""Models for student placement data.

GET /powerpath/placement/{studentId}

Contains nested models for RIT scores, test results, and subject placement data.
"""

from typing import Optional, List
from pydantic import BaseModel, Field
from enum import Enum


class TimebackPlacementTestStatus(str, Enum):
    """Status values for placement test results."""

    PASSED = "PASSED"
    FAILED = "FAILED"
    STARTED = "STARTED"
    NOT_STARTED = "NOT_STARTED"
    SKIP = "SKIP"


class TimebackPlacementTestSource(str, Enum):
    """Source values for placement test results."""

    PLACEMENT = "PLACEMENT"
    EDULASTIC = "EDULASTIC"


class TimebackRitScoreData(BaseModel):
    """RIT score data (GROWTH or SCREENING).
    
    Attributes:
        - score (int): The RIT score value
        - grade (int): The grade level associated with this score
    """

    score: int = Field(..., description="The RIT score value")
    grade: int = Field(..., description="The grade level associated with this score")


class TimebackRitScores(BaseModel):
    """RIT scores for GROWTH and SCREENING tests.
    
    Attributes:
        - GROWTH (TimebackRitScoreData, optional): Growth test RIT score data
        - SCREENING (TimebackRitScoreData, optional): Screening test RIT score data
    """

    GROWTH: Optional[TimebackRitScoreData] = Field(None, description="Growth test RIT score data")
    SCREENING: Optional[TimebackRitScoreData] = Field(None, description="Screening test RIT score data")


class TimebackPlacementTestResult(BaseModel):
    """A single placement test result.
    
    Attributes:
        - testId (str): The test identifier
        - title (str): The test title
        - subject (str): The subject of the test
        - grade (int): The grade level of the test
        - status (TimebackPlacementTestStatus): Test status (PASSED, FAILED, STARTED, NOT_STARTED, SKIP)
        - source (TimebackPlacementTestSource): Source of the test (PLACEMENT, EDULASTIC)
        - score (float, optional): The test score (if completed)
        - completedAt (str, optional): Timestamp when test was completed
        - masteryTrackProcessed (bool, optional): Whether MasteryTrack has processed the result
    """

    testId: str = Field(..., description="The test identifier")
    title: str = Field(..., description="The test title")
    subject: str = Field(..., description="The subject of the test")
    grade: int = Field(..., description="The grade level of the test")
    status: TimebackPlacementTestStatus = Field(..., description="Test status")
    source: TimebackPlacementTestSource = Field(..., description="Source of the test")
    score: Optional[float] = Field(None, description="The test score")
    completedAt: Optional[str] = Field(None, description="Timestamp when test was completed")
    masteryTrackProcessed: Optional[bool] = Field(
        None, description="Whether MasteryTrack has processed the result"
    )


class TimebackSubjectPlacementData(BaseModel):
    """Placement data for a single subject.
    
    Attributes:
        - startingGrade (int): The grade level where placement started
        - currentGrade (int): The current grade level after placement
        - subjectLowestGrade (int): The lowest grade available for this subject
        - subjectHighestGrade (int): The highest grade available for this subject
        - RIT (TimebackRitScores): RIT scores for GROWTH and SCREENING tests
        - results (List[TimebackPlacementTestResult]): List of test results
        - status (str): Overall placement status for this subject
        - nextTestId (str, optional): The ID of the next test to take (null if complete)
    """

    startingGrade: int = Field(..., description="The grade level where placement started")
    currentGrade: int = Field(..., description="The current grade level after placement")
    subjectLowestGrade: int = Field(..., description="The lowest grade available for this subject")
    subjectHighestGrade: int = Field(..., description="The highest grade available for this subject")
    RIT: TimebackRitScores = Field(..., description="RIT scores for GROWTH and SCREENING tests")
    results: List[TimebackPlacementTestResult] = Field(..., description="List of test results")
    status: str = Field(..., description="Overall placement status for this subject")
    nextTestId: Optional[str] = Field(None, description="The ID of the next test to take")

