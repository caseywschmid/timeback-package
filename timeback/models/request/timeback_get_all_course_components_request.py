"""Request model for getting all course components.

GET /ims/oneroster/rostering/v1p2/courses/components
"""

from typing import Optional
from pydantic import BaseModel, Field
from timeback.models.request.timeback_query_params import TimebackQueryParams


class TimebackGetAllCourseComponentsRequest(BaseModel):
    """Request model for getting all course components (paginated list)."""

    query_params: Optional[TimebackQueryParams] = Field(None, description="Optional query parameters")

