"""Response model for searching sections.

GET /assessment-tests/{assessmentTestIdentifier}/test-parts/{testPartIdentifier}/sections

Used by:
- timeback/services/qti/endpoints/search_sections.py
"""

from typing import List
from pydantic import BaseModel, Field
from timeback.models.timeback_qti_section import TimebackQTISection
from timeback.enums import TimebackSortOrder


class TimebackSearchSectionsResponse(BaseModel):
    """Response model for searching sections within a test part.
    
    Attributes:
        - items (List[TimebackQTISection]): List of sections
        - total (int): Total number of sections matching the search criteria
        - page (int): Current page number
        - pages (int): Total number of pages
        - limit (int): Number of items per page
        - sort (str): Field used for sorting
        - order (TimebackSortOrder): Sort order used
    """
    
    items: List[TimebackQTISection] = Field(
        ...,
        description="List of sections."
    )
    total: int = Field(
        ...,
        description="Total number of sections matching the search criteria."
    )
    page: int = Field(..., description="Current page number.")
    pages: int = Field(..., description="Total number of pages.")
    limit: int = Field(..., description="Number of items per page.")
    sort: str = Field(..., description="Field used for sorting.")
    order: TimebackSortOrder = Field(..., description="Sort order used.")

