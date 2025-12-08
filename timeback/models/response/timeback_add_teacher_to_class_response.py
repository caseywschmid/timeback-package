"""Response model for adding a teacher to a class.

POST /ims/oneroster/rostering/v1p2/classes/{classSourcedId}/teachers
"""

from pydantic import BaseModel, Field
from timeback.models.timeback_sourced_id_pairs import TimebackSourcedIdPairs


class TimebackAddTeacherToClassResponse(BaseModel):
    """Response model for adding a teacher to a class."""

    sourcedIdPairs: TimebackSourcedIdPairs = Field(..., description="SourcedId mapping")

