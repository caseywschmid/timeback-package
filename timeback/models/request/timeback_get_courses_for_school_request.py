"""Request model for getting courses for a school.

GET /ims/oneroster/rostering/v1p2/schools/{schoolSourcedId}/courses
"""

from typing import Optional
from pydantic import BaseModel, Field
from timeback.models.request.timeback_query_params import TimebackQueryParams


class TimebackGetCoursesForSchoolRequest(BaseModel):
    """Request model for getting all courses for a specific school."""

    school_sourced_id: str = Field(..., description="The sourcedId of the school")
    query_params: Optional[TimebackQueryParams] = Field(None, description="Optional query parameters")

