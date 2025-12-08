"""Request model for getting a teacher.

GET /ims/oneroster/rostering/v1p2/teachers/{sourcedId}
"""

from typing import Optional
from pydantic import BaseModel, Field
from timeback.models.request.timeback_query_params import TimebackQueryParams


class TimebackGetTeacherRequest(BaseModel):
    """Request model for getting a teacher by sourcedId."""

    sourced_id: str = Field(..., description="The sourcedId of the teacher")
    query_params: Optional[TimebackQueryParams] = Field(None, description="Optional query parameters")

