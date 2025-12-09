"""Response model for bulk test assignment operations.

POST /powerpath/test-assignments/bulk
POST /powerpath/test-assignments/import
"""

from typing import List
from pydantic import BaseModel, Field
from timeback.models.timeback_test_assignment import (
    TimebackTestAssignmentResult,
    TimebackTestAssignmentError,
)


class TimebackBulkTestAssignmentsResponse(BaseModel):
    """Response model for bulk test assignment operations.
    
    Used by both bulk create and import endpoints.
    
    Attributes:
        - success (bool): Whether all assignments succeeded
        - results (list): Successfully created assignments
        - errors (list): Errors that occurred
    """

    success: bool = Field(..., description="Whether all succeeded")
    results: List[TimebackTestAssignmentResult] = Field(
        ..., description="Successful results"
    )
    errors: List[TimebackTestAssignmentError] = Field(..., description="Errors")

