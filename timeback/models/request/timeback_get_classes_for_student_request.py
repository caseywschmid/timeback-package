"""Request model for getting classes for a student.

GET /ims/oneroster/rostering/v1p2/students/{studentSourcedId}/classes
"""

from typing import Optional
from pydantic import BaseModel, Field
from timeback.models.request.timeback_query_params import TimebackQueryParams


class TimebackGetClassesForStudentRequest(BaseModel):
    """Request model for getting classes for a specific student."""

    student_sourced_id: str = Field(..., description="The sourcedId of the student")
    query_params: Optional[TimebackQueryParams] = Field(None, description="Optional query parameters")

