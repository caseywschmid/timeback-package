"""Request model for getting teachers for a class in a school.

GET /ims/oneroster/rostering/v1p2/schools/{schoolSourcedId}/classes/{classSourcedId}/teachers
"""

from typing import Optional
from pydantic import BaseModel, Field
from timeback.models.request.timeback_query_params import TimebackQueryParams


class TimebackGetTeachersForClassInSchoolRequest(BaseModel):
    """Request model for getting teachers for a class in a specific school."""

    school_sourced_id: str = Field(..., description="The sourcedId of the school")
    class_sourced_id: str = Field(..., description="The sourcedId of the class")
    query_params: Optional[TimebackQueryParams] = Field(None, description="Optional query parameters")

