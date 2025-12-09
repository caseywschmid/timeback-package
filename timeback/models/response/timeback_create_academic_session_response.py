"""Response model for creating an academic session.

POST /ims/oneroster/rostering/v1p2/academicSessions
"""

from pydantic import BaseModel, Field
from timeback.models.timeback_sourced_id_pairs import TimebackSourcedIdPairs


class TimebackCreateAcademicSessionResponse(BaseModel):
    """Response model for creating an academic session."""

    sourcedIdPairs: TimebackSourcedIdPairs = Field(..., description="SourcedId mapping")

