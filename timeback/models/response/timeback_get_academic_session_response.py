"""Response model for getting an academic session.

GET /ims/oneroster/rostering/v1p2/academicSessions/{sourcedId}
"""

from pydantic import BaseModel, Field
from timeback.models.timeback_academic_session import TimebackAcademicSession


class TimebackGetAcademicSessionResponse(BaseModel):
    """Response model for getting a single academic session."""

    academicSession: TimebackAcademicSession = Field(..., description="The academic session")

