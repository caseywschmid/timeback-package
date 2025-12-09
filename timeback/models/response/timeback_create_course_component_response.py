"""Response model for creating a course component.

POST /ims/oneroster/rostering/v1p2/courses/components
"""

from pydantic import BaseModel, Field
from timeback.models.timeback_sourced_id_pairs import TimebackSourcedIdPairs


class TimebackCreateCourseComponentResponse(BaseModel):
    """Response model for creating a course component."""

    sourcedIdPairs: TimebackSourcedIdPairs = Field(..., description="SourcedId mapping")

