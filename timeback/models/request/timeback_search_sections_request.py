"""Request model for searching sections within a test part.

GET /assessment-tests/{assessmentTestIdentifier}/test-parts/{testPartIdentifier}/sections

Used by:
- timeback/services/qti/endpoints/search_sections.py
"""

from typing import Optional
from pydantic import BaseModel, Field, ConfigDict
from timeback.enums import TimebackSortOrder


class TimebackSearchSectionsRequest(BaseModel):
    """Request model for searching sections within a test part.
    
    Attributes:
        Optional:
            - query (str, optional): Search term for title and identifier fields (fuzzy search)
            - page (int, optional): Page number for pagination (default: 1)
            - limit (int, optional): Number of items per page (default: 10)
            - sort (str, optional): Field to sort by
            - order (TimebackSortOrder, optional): Sort order (default: desc)
    """
    
    model_config = ConfigDict(populate_by_name=True)
    
    query: Optional[str] = Field(
        None,
        description="Search title and identifier fields using a search term (fuzzy search)."
    )
    page: int = Field(1, description="Page number for pagination.", ge=1)
    limit: int = Field(10, description="Number of items per page.", ge=1, le=3000)
    sort: Optional[str] = Field(
        None,
        description="Field to sort by."
    )
    order: TimebackSortOrder = Field(
        TimebackSortOrder.DESC,
        description="Sort order (asc or desc)."
    )

