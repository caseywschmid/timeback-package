"""Request model for searching QTI assessment items.

GET /assessment-items

Used by:
- timeback/services/qti/endpoints/search_assessment_items.py
"""

from typing import Optional
from pydantic import BaseModel, Field
from timeback.enums import TimebackQTIAssessmentItemSortField, TimebackSortOrder


class TimebackSearchAssessmentItemsRequest(BaseModel):
    """Request model for searching QTI assessment items.
    
    All parameters are optional query parameters for filtering and pagination.
    
    Attributes:
        Optional:
            - query (str, optional): Search term for fuzzy matching on title and identifier
            - page (int, optional): Page number for pagination (default: 1)
            - limit (int, optional): Number of items per page (default: 10)
            - sort (TimebackQTIAssessmentItemSortField, optional): Field to sort by.
              See TimebackQTIAssessmentItemSortField enum for options.
            - order (TimebackSortOrder, optional): Sort order (default: desc).
              See TimebackSortOrder enum for options.
            - filter (str, optional): Advanced filter expression using =, !=, >, >=, <, <=, ~
              and logical AND/OR. Example: type='choice'
    """
    
    query: Optional[str] = Field(
        None,
        description="Search term for fuzzy matching on title and identifier fields"
    )
    page: int = Field(
        default=1,
        ge=1,
        description="Page number for pagination (1-indexed)"
    )
    limit: int = Field(
        default=10,
        ge=1,
        le=100,
        description="Number of items per page"
    )
    sort: Optional[TimebackQTIAssessmentItemSortField] = Field(
        None,
        description="Field to sort results by"
    )
    order: TimebackSortOrder = Field(
        default=TimebackSortOrder.DESC,
        description="Sort order (asc or desc)"
    )
    filter: Optional[str] = Field(
        None,
        description="Advanced filter expression (e.g., type='choice')"
    )

