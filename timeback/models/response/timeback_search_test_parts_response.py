"""Response model for searching test parts.

GET /assessment-tests/{assessmentTestIdentifier}/test-parts

Used by:
- timeback/services/qti/endpoints/search_test_parts.py
"""

from typing import List
from pydantic import BaseModel, Field
from timeback.models.timeback_qti_test_part import TimebackQTITestPart
from timeback.enums import TimebackSortOrder


class TimebackSearchTestPartsResponse(BaseModel):
    """Response model for searching test parts.
    
    Attributes:
        - items (List[TimebackQTITestPart]): List of test parts
        - total (int): Total number of test parts matching the search criteria
        - page (int): Current page number
        - pages (int): Total number of pages
        - limit (int): Number of items per page
        - sort (str): Field used for sorting
        - order (TimebackSortOrder): Sort order used
    """
    
    items: List[TimebackQTITestPart] = Field(
        ...,
        description="List of test parts."
    )
    total: int = Field(
        ...,
        description="Total number of test parts matching the search criteria."
    )
    page: int = Field(..., description="Current page number.")
    pages: int = Field(..., description="Total number of pages.")
    limit: int = Field(..., description="Number of items per page.")
    sort: str = Field(..., description="Field used for sorting.")
    order: TimebackSortOrder = Field(..., description="Sort order used.")

