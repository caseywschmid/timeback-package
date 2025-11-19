"""Request model for getting all score scales.

GET /ims/oneroster/gradebook/v1p2/scoreScales
"""

from typing import Optional
from pydantic import BaseModel, Field

from timeback.models.request.timeback_query_params import TimebackQueryParams


class TimebackGetAllScoreScalesRequest(BaseModel):
    """Request model for getting all score scales (paginated list).
    
    Attributes:
        Optional:
            - query_params (TimebackQueryParams, optional): Query parameters for filtering, pagination, sorting, etc.
              See TimebackQueryParams for available options.
    """

    query_params: Optional[TimebackQueryParams] = Field(
        None, description="Optional query parameters (fields, limit, offset, sort, filter, search, etc.)"
    )
