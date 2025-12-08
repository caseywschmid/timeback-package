"""Request model for getting classes for a user.

GET /ims/oneroster/rostering/v1p2/users/{userSourcedId}/classes
"""

from typing import Optional
from pydantic import BaseModel, Field
from timeback.models.request.timeback_query_params import TimebackQueryParams


class TimebackGetClassesForUserRequest(BaseModel):
    """Request model for getting classes for a specific user."""

    user_sourced_id: str = Field(..., description="The sourcedId of the user")
    query_params: Optional[TimebackQueryParams] = Field(None, description="Optional query parameters")

