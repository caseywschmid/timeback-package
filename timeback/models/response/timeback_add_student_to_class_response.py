"""Response model for adding a student to a class.

POST /ims/oneroster/rostering/v1p2/classes/{classSourcedId}/students
"""

from pydantic import BaseModel, Field
from timeback.models.timeback_sourced_id_pairs import TimebackSourcedIdPairs


class TimebackAddStudentToClassResponse(BaseModel):
    """Response model for adding a student to a class."""

    sourcedIdPairs: TimebackSourcedIdPairs = Field(..., description="SourcedId mapping")

