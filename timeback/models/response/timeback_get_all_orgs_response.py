"""Response model for getting all orgs.

GET /ims/oneroster/rostering/v1p2/orgs
"""

from typing import List
from pydantic import BaseModel, Field, ConfigDict
from timeback.models.timeback_org import TimebackOrg


class TimebackGetAllOrgsResponse(BaseModel):
    """Response model for paginated orgs list."""

    model_config = ConfigDict(populate_by_name=True)

    orgs: List[TimebackOrg] = Field(..., description="List of orgs")
    total_count: int = Field(..., alias="totalCount")
    page_count: int = Field(..., alias="pageCount")
    page_number: int = Field(..., alias="pageNumber")
    offset: int = Field(...)
    limit: int = Field(...)

