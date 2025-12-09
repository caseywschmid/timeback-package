"""Request model for getting an enrollment.

GET /ims/oneroster/rostering/v1p2/enrollments/{sourcedId}
"""

from typing import Optional
from pydantic import BaseModel, Field
from timeback.models.request.timeback_query_params import TimebackQueryParams


class TimebackGetEnrollmentRequest(BaseModel):
    """Request model for getting an enrollment by sourcedId."""

    sourced_id: str = Field(..., description="The sourcedId of the enrollment")
    query_params: Optional[TimebackQueryParams] = Field(None, description="Optional query parameters")

