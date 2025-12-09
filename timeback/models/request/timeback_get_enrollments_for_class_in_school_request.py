"""Request model for getting enrollments for a class in a school.

GET /ims/oneroster/rostering/v1p2/schools/{schoolSourcedId}/classes/{classSourcedId}/enrollments
"""

from typing import Optional
from pydantic import BaseModel, Field
from timeback.models.request.timeback_query_params import TimebackQueryParams


class TimebackGetEnrollmentsForClassInSchoolRequest(BaseModel):
    """Request model for getting enrollments for a specific class in a school."""

    school_sourced_id: str = Field(..., description="The sourcedId of the school")
    class_sourced_id: str = Field(..., description="The sourcedId of the class")
    query_params: Optional[TimebackQueryParams] = Field(None, description="Optional query parameters")

