"""Request model for getting all teachers.

GET /ims/oneroster/rostering/v1p2/teachers
"""

from typing import Optional
from pydantic import BaseModel, Field
from timeback.models.request.timeback_query_params import TimebackQueryParams


class TimebackGetAllTeachersRequest(BaseModel):
    """Request model for getting all teachers (paginated list)."""

    query_params: Optional[TimebackQueryParams] = Field(None, description="Optional query parameters")

