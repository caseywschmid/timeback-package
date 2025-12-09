"""Request model for getting score scales for a school.

GET /ims/oneroster/gradebook/v1p2/schools/{sourcedId}/scoreScales
"""

from typing import Optional
from pydantic import BaseModel, Field

from timeback.models.request.timeback_query_params import TimebackQueryParams


class TimebackGetScoreScalesForSchoolRequest(BaseModel):
    """Request model for getting score scales for a specific school.
    
    Attributes:
        Required:
            - sourced_id (str): The sourcedId of the school to fetch score scales for
        
        Optional:
            - query_params (TimebackQueryParams, optional): Query parameters for filtering, pagination, etc.
              See TimebackQueryParams for available options.
    """

    sourced_id: str = Field(..., description="The sourcedId of the school")
    query_params: Optional[TimebackQueryParams] = Field(
        None, description="Optional query parameters (limit, offset, filter, etc.)"
    )
