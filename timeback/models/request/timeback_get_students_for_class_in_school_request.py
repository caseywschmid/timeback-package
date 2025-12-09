"""Request model for getting students for a class in a school.

GET /ims/oneroster/rostering/v1p2/schools/{schoolSourcedId}/classes/{classSourcedId}/students
"""

from typing import Optional
from pydantic import BaseModel, Field
from timeback.models.request.timeback_query_params import TimebackQueryParams


class TimebackGetStudentsForClassInSchoolRequest(BaseModel):
    """Request model for getting students for a class in a specific school."""

    school_sourced_id: str = Field(..., description="The sourcedId of the school")
    class_sourced_id: str = Field(..., description="The sourcedId of the class")
    query_params: Optional[TimebackQueryParams] = Field(None, description="Optional query parameters")

