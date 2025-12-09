"""Request model for getting a student.

GET /ims/oneroster/rostering/v1p2/students/{sourcedId}
"""

from typing import Optional
from pydantic import BaseModel, Field
from timeback.models.request.timeback_query_params import TimebackQueryParams


class TimebackGetStudentRequest(BaseModel):
    """Request model for getting a student by sourcedId."""

    sourced_id: str = Field(..., description="The sourcedId of the student")
    query_params: Optional[TimebackQueryParams] = Field(None, description="Optional query parameters")

