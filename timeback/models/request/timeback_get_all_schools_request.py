"""Request model for getting all schools.

GET /ims/oneroster/rostering/v1p2/schools
"""

from typing import Optional
from pydantic import BaseModel, Field

from timeback.models.request.timeback_query_params import TimebackQueryParams


class TimebackGetAllSchoolsRequest(BaseModel):
    """Request model for getting all schools.
    
    Attributes:
        Optional:
            - query_params (TimebackQueryParams, optional): Query parameters for filtering, pagination, etc.
              See TimebackQueryParams for available options.
    """

    query_params: Optional[TimebackQueryParams] = Field(
        None, description="Optional query parameters (limit, offset, filter, etc.)"
    )
