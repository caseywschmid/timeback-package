"""Request model for getting terms for a school.

GET /ims/oneroster/rostering/v1p2/schools/{schoolSourcedId}/terms
"""

from typing import Optional
from pydantic import BaseModel, Field
from timeback.models.request.timeback_query_params import TimebackQueryParams


class TimebackGetTermsForSchoolRequest(BaseModel):
    """Request model for getting terms for a specific school."""

    school_sourced_id: str = Field(..., description="The sourcedId of the school")
    query_params: Optional[TimebackQueryParams] = Field(None, description="Optional query parameters")

