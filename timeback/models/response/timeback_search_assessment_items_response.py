"""Response model for searching QTI assessment items.

GET /assessment-items

Used by:
- timeback/services/qti/endpoints/search_assessment_items.py
"""

from typing import List, Optional
from pydantic import BaseModel, Field
from timeback.models.timeback_qti_assessment_item import TimebackQTIAssessmentItem
from timeback.enums import TimebackSortOrder


class TimebackSearchAssessmentItemsResponse(BaseModel):
    """Response model for searching QTI assessment items.
    
    Paginated response containing assessment items that match the search criteria
    with navigation metadata.
    
    Attributes:
        - items (list): List of assessment items matching the search criteria.
          See TimebackQTIAssessmentItem for structure.
        - total (int): Total number of entities matching the search criteria
        - page (int): Current page number (1-indexed)
        - pages (int): Total number of pages
        - limit (int): Number of entities per page
        - sort (str, optional): Field the results are sorted by
        - order (str): Sort order (asc or desc)
    """
    
    items: List[TimebackQTIAssessmentItem] = Field(
        ...,
        description="List of assessment items matching the search criteria"
    )
    total: int = Field(
        ...,
        description="Total number of entities matching the search criteria"
    )
    page: int = Field(
        default=1,
        description="Current page number (1-indexed)"
    )
    pages: int = Field(
        ...,
        description="Total number of pages"
    )
    limit: int = Field(
        default=10,
        description="Number of entities per page"
    )
    sort: Optional[str] = Field(
        None,
        description="Field the results are sorted by"
    )
    order: TimebackSortOrder = Field(
        ...,
        description="Sort order (asc or desc)"
    )

