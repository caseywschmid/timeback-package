"""Response model for getting a term.

GET /ims/oneroster/rostering/v1p2/terms/{sourcedId}
"""

from pydantic import BaseModel, Field
from timeback.models.timeback_academic_session import TimebackAcademicSession


class TimebackGetTermResponse(BaseModel):
    """Response model for getting a single term/academic session."""

    academicSession: TimebackAcademicSession = Field(..., description="The requested term")

