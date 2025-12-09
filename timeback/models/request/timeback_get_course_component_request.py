"""Request model for getting a course component.

GET /ims/oneroster/rostering/v1p2/courses/components/{sourcedId}
"""

from typing import Optional
from pydantic import BaseModel, Field
from timeback.models.request.timeback_query_params import TimebackQueryParams


class TimebackGetCourseComponentRequest(BaseModel):
    """Request model for getting a course component by sourcedId."""

    sourced_id: str = Field(..., description="The sourcedId of the course component")
    query_params: Optional[TimebackQueryParams] = Field(None, description="Optional query parameters")

