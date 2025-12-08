"""Request model for getting teachers for a school.

GET /ims/oneroster/rostering/v1p2/schools/{schoolSourcedId}/teachers
"""

from typing import Optional
from pydantic import BaseModel, Field
from timeback.models.request.timeback_query_params import TimebackQueryParams


class TimebackGetTeachersForSchoolRequest(BaseModel):
    """Request model for getting teachers for a specific school."""

    school_sourced_id: str = Field(..., description="The sourcedId of the school")
    query_params: Optional[TimebackQueryParams] = Field(None, description="Optional query parameters")

