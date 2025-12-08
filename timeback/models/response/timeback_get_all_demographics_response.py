"""Response model for getting all demographics.

GET /ims/oneroster/rostering/v1p2/demographics
"""

from typing import List
from pydantic import BaseModel, Field, ConfigDict
from timeback.models.timeback_demographic import TimebackDemographic


class TimebackGetAllDemographicsResponse(BaseModel):
    """Response model for paginated demographics list."""

    model_config = ConfigDict(populate_by_name=True)

    demographics: List[TimebackDemographic] = Field(..., description="List of demographics")
    total_count: int = Field(..., alias="totalCount")
    page_count: int = Field(..., alias="pageCount")
    page_number: int = Field(..., alias="pageNumber")
    offset: int = Field(...)
    limit: int = Field(...)

