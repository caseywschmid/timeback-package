"""Response model for listing test assignments.

GET /powerpath/test-assignments
GET /powerpath/test-assignments/admin
"""

from typing import List
from pydantic import BaseModel, Field
from timeback.models.timeback_test_assignment import TimebackTestAssignment


class TimebackListTestAssignmentsResponse(BaseModel):
    """Response model for listing test assignments.
    
    Used by both student-specific and admin list endpoints.
    
    Attributes:
        - testAssignments (list): List of test assignments
        - totalCount (int): Total number of assignments
        - pageCount (int): Total number of pages
        - pageNumber (int): Current page number
        - offset (int): Current offset
        - limit (int): Items per page
    """

    testAssignments: List[TimebackTestAssignment] = Field(
        ..., description="Test assignments list"
    )
    totalCount: int = Field(..., description="Total count")
    pageCount: int = Field(..., description="Total pages")
    pageNumber: int = Field(..., description="Current page")
    offset: int = Field(..., description="Current offset")
    limit: int = Field(..., description="Items per page")

