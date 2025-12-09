"""Request model for getting all resources.

GET /ims/oneroster/resources/v1p2/resources
"""

from typing import Optional
from pydantic import BaseModel, Field
from timeback.models.request.timeback_query_params import TimebackQueryParams


class TimebackGetAllResourcesRequest(BaseModel):
    """Request model for getting all resources (paginated list)."""

    query_params: Optional[TimebackQueryParams] = Field(
        None, description="Optional query parameters (fields, limit, offset, sort, filter, search, etc.)"
    )

