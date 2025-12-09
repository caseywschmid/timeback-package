"""Screening Result model for the PowerPath API.

This module defines models for screening results from the PowerPath API.
"""

from typing import Optional
from pydantic import BaseModel, Field


class TimebackScreeningResult(BaseModel):
    """Individual screening result for a subject.
    
    Attributes:
        - grade (str): The grade level determined by the screening test.
          Valid values: "-1", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"
        - ritScore (float): The RIT score achieved on the screening test
        - testName (str): The name of the screening test
        - completedAt (str): ISO timestamp when the test was completed
    """

    grade: str = Field(..., description="The grade level determined by the screening test")
    ritScore: float = Field(..., description="The RIT score achieved on the screening test")
    testName: str = Field(..., description="The name of the screening test")
    completedAt: str = Field(..., description="ISO timestamp when the test was completed")

