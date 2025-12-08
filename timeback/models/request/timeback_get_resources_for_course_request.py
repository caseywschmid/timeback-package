"""Request model for getting resources for a course.

GET /ims/oneroster/resources/v1p2/courses/{courseSourcedId}/resources
"""

from typing import Optional
from pydantic import BaseModel, Field
from timeback.models.request.timeback_query_params import TimebackQueryParams


class TimebackGetResourcesForCourseRequest(BaseModel):
    """Request model for getting resources for a course."""

    course_sourced_id: str = Field(..., description="The sourcedId of the course")
    query_params: Optional[TimebackQueryParams] = Field(None, description="Optional query parameters")

