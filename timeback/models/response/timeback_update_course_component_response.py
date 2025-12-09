"""Response model for updating a course component.

PUT /ims/oneroster/rostering/v1p2/courses/components/{sourcedId}
"""

from pydantic import BaseModel, Field
from timeback.models.timeback_course_component import TimebackCourseComponent


class TimebackUpdateCourseComponentResponse(BaseModel):
    """Response model for updating a course component."""

    courseComponent: TimebackCourseComponent = Field(..., description="The updated course component")

