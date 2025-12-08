"""Response model for getting a course.

GET /ims/oneroster/rostering/v1p2/courses/{sourcedId}
"""

from pydantic import BaseModel, Field
from timeback.models.timeback_course import TimebackCourse


class TimebackGetCourseResponse(BaseModel):
    """Response model for getting a single course."""

    course: TimebackCourse = Field(..., description="The course")

