"""Request model for getting classes for a course.

GET /ims/oneroster/rostering/v1p2/courses/{courseSourcedId}/classes
"""

from typing import Optional
from pydantic import BaseModel, Field
from timeback.models.request.timeback_query_params import TimebackQueryParams


class TimebackGetClassesForCourseRequest(BaseModel):
    """Request model for getting classes for a specific course."""

    course_sourced_id: str = Field(..., description="The sourcedId of the course")
    query_params: Optional[TimebackQueryParams] = Field(None, description="Optional query parameters")

