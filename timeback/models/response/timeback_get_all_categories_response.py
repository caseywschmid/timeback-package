"""Response model for getting all categories (paginated list).

Used for endpoints that return a paginated list of categories.
"""

from typing import List
from pydantic import BaseModel, Field

from timeback.models.timeback_category import TimebackCategory


class TimebackGetAllCategoriesResponse(BaseModel):
    """Response model for paginated list of categories.
    
    Attributes:
        categories: List of category objects
        total_count: Total number of categories across all pages
        page_count: Total number of pages
        page_number: Current page number (1-indexed)
        offset: Offset for pagination
        limit: Limit per page
    """

    categories: List[TimebackCategory] = Field(..., description="List of categories")
    total_count: int = Field(..., alias="totalCount", description="Total number of categories")
    page_count: int = Field(..., alias="pageCount", description="Total number of pages")
    page_number: int = Field(..., alias="pageNumber", description="Current page number")
    offset: int = Field(..., description="Offset for pagination")
    limit: int = Field(..., description="Limit per page")

    model_config = {"populate_by_name": True}

