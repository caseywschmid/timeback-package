"""Response model for creating a course.

POST /ims/oneroster/rostering/v1p2/courses
"""

from pydantic import BaseModel, Field
from timeback.models.timeback_sourced_id_pairs import TimebackSourcedIdPairs


class TimebackCreateCourseResponse(BaseModel):
    """Response model for creating a course."""

    sourcedIdPairs: TimebackSourcedIdPairs = Field(..., description="SourcedId mapping")

