"""Response model for updating a course.

PUT /ims/oneroster/rostering/v1p2/courses/{sourcedId}
"""

from pydantic import BaseModel, Field
from timeback.models.timeback_course import TimebackCourse


class TimebackUpdateCourseResponse(BaseModel):
    """Response model for updating a course."""

    course: TimebackCourse = Field(..., description="The updated course")

