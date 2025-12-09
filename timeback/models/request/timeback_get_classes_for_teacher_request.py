"""Request model for getting classes for a teacher.

GET /ims/oneroster/rostering/v1p2/teachers/{teacherSourcedId}/classes
"""

from typing import Optional
from pydantic import BaseModel, Field
from timeback.models.request.timeback_query_params import TimebackQueryParams


class TimebackGetClassesForTeacherRequest(BaseModel):
    """Request model for getting classes for a specific teacher."""

    teacher_sourced_id: str = Field(..., description="The sourcedId of the teacher")
    query_params: Optional[TimebackQueryParams] = Field(None, description="Optional query parameters")

