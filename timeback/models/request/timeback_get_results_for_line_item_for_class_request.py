"""Request model for getting results for a line item for a class.

GET /ims/oneroster/gradebook/v1p2/classes/{classSourcedId}/lineItems/{lineItemSourcedId}/results
"""

from typing import Optional
from pydantic import BaseModel, Field

from timeback.models.request.timeback_query_params import TimebackQueryParams


class TimebackGetResultsForLineItemForClassRequest(BaseModel):
    """Request model for getting results for a line item for a class (paginated list).
    
    Attributes:
        Required:
            - class_sourced_id (str): The sourcedId of the class (path parameter)
            - line_item_sourced_id (str): The sourcedId of the line item (path parameter)
        
        Optional:
            - query_params (TimebackQueryParams, optional): Query parameters for filtering, pagination, sorting, etc.
              See TimebackQueryParams for available options.
    """

    class_sourced_id: str = Field(..., description="The sourcedId of the class (path parameter)")
    line_item_sourced_id: str = Field(..., description="The sourcedId of the line item (path parameter)")
    query_params: Optional[TimebackQueryParams] = Field(
        None, description="Optional query parameters (fields, limit, offset, sort, filter, search, etc.)"
    )

