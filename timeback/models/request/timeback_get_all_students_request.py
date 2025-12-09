"""Request model for getting all students.

GET /ims/oneroster/rostering/v1p2/students
"""

from typing import Optional
from pydantic import BaseModel, Field
from timeback.models.request.timeback_query_params import TimebackQueryParams


class TimebackGetAllStudentsRequest(BaseModel):
    """Request model for getting all students (paginated list)."""

    query_params: Optional[TimebackQueryParams] = Field(None, description="Optional query parameters")

