"""Request model for getting all classes for a school.

GET /ims/oneroster/rostering/v1p2/schools/{schoolSourcedId}/classes
"""

from typing import Optional
from pydantic import BaseModel, Field

from timeback.models.request.timeback_query_params import TimebackQueryParams


class TimebackGetClassesForSchoolRequest(BaseModel):
    """Request model for getting all classes for a specific school.
    
    Attributes:
        Required:
            - school_sourced_id (str): The sourcedId of the school to get classes for
        
        Optional:
            - query_params (TimebackQueryParams, optional): Query parameters for filtering, pagination, sorting, etc.
              See TimebackQueryParams for available options.
    """

    school_sourced_id: str = Field(..., description="The sourcedId of the school to get classes for")
    query_params: Optional[TimebackQueryParams] = Field(
        None, description="Optional query parameters (fields, limit, offset, sort, filter, search, etc.)"
    )

