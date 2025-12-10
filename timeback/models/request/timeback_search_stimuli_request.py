"""Request model for searching QTI stimuli.

GET /stimuli

Used by:
- timeback/services/qti/endpoints/search_stimuli.py
"""

from typing import Optional
from pydantic import BaseModel, Field
from timeback.enums import TimebackQTISortField, TimebackSortOrder


class TimebackSearchStimuliRequest(BaseModel):
    """Request model for searching QTI stimuli.
    
    All parameters are optional query parameters for filtering and pagination.
    
    Attributes:
        Optional:
            - query (str, optional): Search term for fuzzy matching on title and identifier
            - page (int, optional): Page number for pagination (default: 1)
            - limit (int, optional): Number of items per page (default: 10)
            - sort (TimebackQTISortField, optional): Field to sort by.
              See TimebackQTISortField enum for options.
            - order (TimebackSortOrder, optional): Sort order (default: desc).
              See TimebackSortOrder enum for options.
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
    sort: Optional[TimebackQTISortField] = Field(
        None,
        description="Field to sort results by"
    )
    order: TimebackSortOrder = Field(
        default=TimebackSortOrder.DESC,
        description="Sort order (asc or desc)"
    )

