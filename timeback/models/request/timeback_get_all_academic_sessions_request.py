"""Request model for getting all academic sessions.

GET /ims/oneroster/rostering/v1p2/academicSessions
"""

from typing import Optional
from pydantic import BaseModel, Field
from timeback.models.request.timeback_query_params import TimebackQueryParams


class TimebackGetAllAcademicSessionsRequest(BaseModel):
    """Request model for getting all academic sessions (paginated list)."""

    query_params: Optional[TimebackQueryParams] = Field(None, description="Optional query parameters")

