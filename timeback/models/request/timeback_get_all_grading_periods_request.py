"""Request model for getting all grading periods.

GET /ims/oneroster/rostering/v1p2/gradingPeriods
"""

from typing import Optional
from pydantic import BaseModel, Field
from timeback.models.request.timeback_query_params import TimebackQueryParams


class TimebackGetAllGradingPeriodsRequest(BaseModel):
    """Request model for getting all grading periods (paginated list)."""

    query_params: Optional[TimebackQueryParams] = Field(None, description="Optional query parameters")

