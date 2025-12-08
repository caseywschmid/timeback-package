"""Request model for getting all courses.

GET /ims/oneroster/rostering/v1p2/courses
"""

from typing import Optional
from pydantic import BaseModel, Field
from timeback.models.request.timeback_query_params import TimebackQueryParams


class TimebackGetAllCoursesRequest(BaseModel):
    """Request model for getting all courses (paginated list)."""

    query_params: Optional[TimebackQueryParams] = Field(None, description="Optional query parameters")

