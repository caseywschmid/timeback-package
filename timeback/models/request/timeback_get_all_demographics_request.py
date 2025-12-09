"""Request model for getting all demographics.

GET /ims/oneroster/rostering/v1p2/demographics
"""

from typing import Optional
from pydantic import BaseModel, Field
from timeback.models.request.timeback_query_params import TimebackQueryParams


class TimebackGetAllDemographicsRequest(BaseModel):
    """Request model for getting all demographics (paginated list)."""

    query_params: Optional[TimebackQueryParams] = Field(None, description="Optional query parameters")

