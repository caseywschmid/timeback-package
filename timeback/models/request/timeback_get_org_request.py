"""Request model for getting an org.

GET /ims/oneroster/rostering/v1p2/orgs/{sourcedId}
"""

from typing import Optional
from pydantic import BaseModel, Field
from timeback.models.request.timeback_query_params import TimebackQueryParams


class TimebackGetOrgRequest(BaseModel):
    """Request model for getting an org by sourcedId."""

    sourced_id: str = Field(..., description="The sourcedId of the org")
    query_params: Optional[TimebackQueryParams] = Field(None, description="Optional query parameters")

