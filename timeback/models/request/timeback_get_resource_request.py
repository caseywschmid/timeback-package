"""Request model for getting a resource.

GET /ims/oneroster/resources/v1p2/resources/{sourcedId}
"""

from typing import Optional
from pydantic import BaseModel, Field
from timeback.models.request.timeback_query_params import TimebackQueryParams


class TimebackGetResourceRequest(BaseModel):
    """Request model for getting a resource by sourcedId."""

    sourced_id: str = Field(..., description="The sourcedId of the resource")
    query_params: Optional[TimebackQueryParams] = Field(None, description="Optional query parameters")

