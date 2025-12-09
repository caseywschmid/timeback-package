"""Request model for getting a course.

GET /ims/oneroster/rostering/v1p2/courses/{sourcedId}
"""

from typing import Optional
from pydantic import BaseModel, Field
from timeback.models.request.timeback_query_params import TimebackQueryParams


class TimebackGetCourseRequest(BaseModel):
    """Request model for getting a course by sourcedId."""

    sourced_id: str = Field(..., description="The sourcedId of the course")
    query_params: Optional[TimebackQueryParams] = Field(None, description="Optional query parameters")

