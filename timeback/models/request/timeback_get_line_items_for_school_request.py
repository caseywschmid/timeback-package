"""Request model for getting line items for a school.

GET /ims/oneroster/gradebook/v1p2/schools/{sourcedId}/lineItems
"""

from typing import Optional
from pydantic import BaseModel, Field

from timeback.models.request.timeback_query_params import TimebackQueryParams


class TimebackGetLineItemsForSchoolRequest(BaseModel):
    """Request model for getting line items for a school (paginated list).
    
    Attributes:
        Required:
            - school_sourced_id (str): The sourcedId of the school (path parameter)
        
        Optional:
            - query_params (TimebackQueryParams, optional): Query parameters for filtering, pagination, sorting, etc.
              See TimebackQueryParams for available options.
    """

    school_sourced_id: str = Field(..., description="The sourcedId of the school (path parameter)")
    query_params: Optional[TimebackQueryParams] = Field(
        None, description="Optional query parameters (fields, limit, offset, sort, filter, search, etc.)"
    )

