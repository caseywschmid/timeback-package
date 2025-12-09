"""Response model for updating an academic session.

PUT /ims/oneroster/rostering/v1p2/academicSessions/{sourcedId}
"""

from pydantic import BaseModel, Field
from timeback.models.timeback_academic_session import TimebackAcademicSession


class TimebackUpdateAcademicSessionResponse(BaseModel):
    """Response model for updating an academic session."""

    academicSession: TimebackAcademicSession = Field(..., description="The updated academic session")

