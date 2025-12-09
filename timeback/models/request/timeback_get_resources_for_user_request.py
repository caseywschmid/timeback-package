"""Request model for getting resources for a user.

GET /ims/oneroster/resources/v1p2/users/{userSourcedId}/resources
"""

from typing import Optional
from pydantic import BaseModel, Field
from timeback.models.request.timeback_query_params import TimebackQueryParams


class TimebackGetResourcesForUserRequest(BaseModel):
    """Request model for getting resources for a user."""

    user_sourced_id: str = Field(..., description="The sourcedId of the user")
    query_params: Optional[TimebackQueryParams] = Field(None, description="Optional query parameters")

