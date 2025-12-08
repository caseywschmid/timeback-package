"""Request model for getting a grading period.

GET /ims/oneroster/rostering/v1p2/gradingPeriods/{sourcedId}
"""

from typing import Optional
from pydantic import BaseModel, Field
from timeback.models.request.timeback_query_params import TimebackQueryParams


class TimebackGetGradingPeriodRequest(BaseModel):
    """Request model for getting a grading period by sourcedId."""

    sourced_id: str = Field(..., description="The sourcedId of the grading period")
    query_params: Optional[TimebackQueryParams] = Field(None, description="Optional query parameters")

