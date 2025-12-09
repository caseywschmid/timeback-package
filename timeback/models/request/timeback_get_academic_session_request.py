"""Request model for getting an academic session.

GET /ims/oneroster/rostering/v1p2/academicSessions/{sourcedId}
"""

from typing import Optional
from pydantic import BaseModel, Field
from timeback.models.request.timeback_query_params import TimebackQueryParams


class TimebackGetAcademicSessionRequest(BaseModel):
    """Request model for getting an academic session by sourcedId."""

    sourced_id: str = Field(..., description="The sourcedId of the academic session")
    query_params: Optional[TimebackQueryParams] = Field(None, description="Optional query parameters")

