"""Response model for getting a course component.

GET /ims/oneroster/rostering/v1p2/courses/components/{sourcedId}
"""

from pydantic import BaseModel, Field
from timeback.models.timeback_course_component import TimebackCourseComponent


class TimebackGetCourseComponentResponse(BaseModel):
    """Response model for getting a single course component."""

    courseComponent: TimebackCourseComponent = Field(..., description="The course component")

