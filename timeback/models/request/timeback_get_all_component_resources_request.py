"""Request model for getting all component resources.

GET /ims/oneroster/rostering/v1p2/courses/component-resources
"""

from typing import Optional
from pydantic import BaseModel, Field
from timeback.models.request.timeback_query_params import TimebackQueryParams


class TimebackGetAllComponentResourcesRequest(BaseModel):
    """Request model for getting all component resources (paginated list)."""

    query_params: Optional[TimebackQueryParams] = Field(None, description="Optional query parameters")

