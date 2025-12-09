"""Request model for getting resources for a class.

GET /ims/oneroster/resources/v1p2/classes/{classSourcedId}/resources
"""

from typing import Optional
from pydantic import BaseModel, Field
from timeback.models.request.timeback_query_params import TimebackQueryParams


class TimebackGetResourcesForClassRequest(BaseModel):
    """Request model for getting resources for a class."""

    class_sourced_id: str = Field(..., description="The sourcedId of the class")
    query_params: Optional[TimebackQueryParams] = Field(None, description="Optional query parameters")

