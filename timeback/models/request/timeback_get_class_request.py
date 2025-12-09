"""Request model for getting a class.

GET /ims/oneroster/rostering/v1p2/classes/{sourcedId}
"""

from typing import Optional
from pydantic import BaseModel, Field

from timeback.models.request.timeback_query_params import TimebackQueryParams


class TimebackGetClassRequest(BaseModel):
    """Request model for getting a class by sourcedId.
    
    Attributes:
        Required:
            - sourced_id (str): The sourcedId of the class to fetch
        
        Optional:
            - query_params (TimebackQueryParams, optional): Query parameters for filtering, pagination, etc.
              See TimebackQueryParams for available options.
    """

    sourced_id: str = Field(..., description="The sourcedId of the class to fetch")
    query_params: Optional[TimebackQueryParams] = Field(
        None, description="Optional query parameters (fields, etc.)"
    )

