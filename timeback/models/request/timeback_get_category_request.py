"""Request model for getting a category.

GET /ims/oneroster/gradebook/v1p2/categories/{sourcedId}
"""

from typing import Optional
from pydantic import BaseModel, Field

from timeback.models.request.timeback_query_params import TimebackQueryParams


class TimebackGetCategoryRequest(BaseModel):
    """Request model for getting a category by sourcedId.
    
    Attributes:
        Required:
            - sourced_id (str): The sourcedId of the category to fetch
        
        Optional:
            - query_params (TimebackQueryParams, optional): Query parameters (fields, etc.)
              See TimebackQueryParams for available options.
    """

    sourced_id: str = Field(..., description="The sourcedId of the category to fetch")
    query_params: Optional[TimebackQueryParams] = Field(
        None, description="Optional query parameters (fields, etc.)"
    )

