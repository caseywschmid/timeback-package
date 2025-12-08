"""Request model for getting a demographic.

GET /ims/oneroster/rostering/v1p2/demographics/{sourcedId}
"""

from typing import Optional
from pydantic import BaseModel, Field
from timeback.models.request.timeback_query_params import TimebackQueryParams


class TimebackGetDemographicRequest(BaseModel):
    """Request model for getting a demographic by sourcedId."""

    sourced_id: str = Field(..., description="The sourcedId of the demographic")
    query_params: Optional[TimebackQueryParams] = Field(None, description="Optional query parameters")

