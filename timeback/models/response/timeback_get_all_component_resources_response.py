"""Response model for getting all component resources.

GET /ims/oneroster/rostering/v1p2/courses/component-resources
"""

from typing import List
from pydantic import BaseModel, Field, ConfigDict
from timeback.models.timeback_component_resource import TimebackComponentResource


class TimebackGetAllComponentResourcesResponse(BaseModel):
    """Response model for paginated component resources list."""

    model_config = ConfigDict(populate_by_name=True)

    componentResources: List[TimebackComponentResource] = Field(..., description="List of component resources")
    total_count: int = Field(..., alias="totalCount")
    page_count: int = Field(..., alias="pageCount")
    page_number: int = Field(..., alias="pageNumber")
    offset: int = Field(...)
    limit: int = Field(...)

