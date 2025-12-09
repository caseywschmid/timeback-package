"""Response model for getting all placement tests.

GET /powerpath/placement/getAllPlacementTests
"""

from typing import List
from pydantic import BaseModel, Field

from timeback.models.timeback_placement_test import TimebackPlacementTest


class TimebackGetAllPlacementTestsResponse(BaseModel):
    """Response model for getting all placement tests.
    
    Returns all placement tests for a subject, including available results for each.
    
    Attributes:
        - placementTests (List[TimebackPlacementTest]): List of placement tests.
          See TimebackPlacementTest for structure.
    """

    placementTests: List[TimebackPlacementTest] = Field(
        ..., description="List of placement tests"
    )

