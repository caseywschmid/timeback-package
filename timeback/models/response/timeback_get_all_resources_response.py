"""Response model for getting all resources.

GET /ims/oneroster/resources/v1p2/resources
"""

from typing import List
from pydantic import BaseModel, Field
from timeback.models.timeback_resource import TimebackResource


class TimebackGetAllResourcesResponse(BaseModel):
    """Response model for paginated resources list."""

    resources: List[TimebackResource] = Field(..., description="List of resources")
    totalCount: int = Field(..., description="Total number of resources")
    pageCount: int = Field(..., description="Total number of pages")
    pageNumber: int = Field(..., description="Current page number")
    offset: int = Field(..., description="Offset for pagination")
    limit: int = Field(..., description="Limit per page")

