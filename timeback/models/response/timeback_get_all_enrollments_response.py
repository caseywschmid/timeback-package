"""Response model for getting all enrollments.

GET /ims/oneroster/rostering/v1p2/enrollments
"""

from typing import List
from pydantic import BaseModel, Field, ConfigDict
from timeback.models.timeback_enrollment import TimebackEnrollment


class TimebackGetAllEnrollmentsResponse(BaseModel):
    """Response model for paginated enrollments list."""

    model_config = ConfigDict(populate_by_name=True)

    enrollments: List[TimebackEnrollment] = Field(..., description="List of enrollments")
    total_count: int = Field(..., alias="totalCount")
    page_count: int = Field(..., alias="pageCount")
    page_number: int = Field(..., alias="pageNumber")
    offset: int = Field(...)
    limit: int = Field(...)

