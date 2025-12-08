"""Request model for getting all enrollments.

GET /ims/oneroster/rostering/v1p2/enrollments
"""

from typing import Optional
from pydantic import BaseModel, Field
from timeback.models.request.timeback_query_params import TimebackQueryParams


class TimebackGetAllEnrollmentsRequest(BaseModel):
    """Request model for getting all enrollments (paginated list)."""

    query_params: Optional[TimebackQueryParams] = Field(None, description="Optional query parameters")

