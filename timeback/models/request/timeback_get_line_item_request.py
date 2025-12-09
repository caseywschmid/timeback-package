"""Request model for getting a line item.

GET /ims/oneroster/gradebook/v1p2/lineItems/{sourcedId}
"""

from typing import Optional
from pydantic import BaseModel, Field

from timeback.models.request.timeback_query_params import TimebackQueryParams


class TimebackGetLineItemRequest(BaseModel):
    """Request model for getting a line item by sourcedId.
    
    Attributes:
        Required:
            - sourced_id (str): The sourcedId of the line item to fetch
        
        Optional:
            - query_params (TimebackQueryParams, optional): Query parameters (fields, etc.)
              See TimebackQueryParams for available options.
    """

    sourced_id: str = Field(..., description="The sourcedId of the line item to fetch")
    query_params: Optional[TimebackQueryParams] = Field(
        None, description="Optional query parameters (fields, etc.)"
    )

