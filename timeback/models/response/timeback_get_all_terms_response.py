"""Response model for getting all terms.

GET /ims/oneroster/rostering/v1p2/terms
"""

from typing import List
from pydantic import BaseModel, Field, ConfigDict
from timeback.models.timeback_academic_session import TimebackAcademicSession


class TimebackGetAllTermsResponse(BaseModel):
    """Response model for paginated terms list."""

    model_config = ConfigDict(populate_by_name=True)

    academicSessions: List[TimebackAcademicSession] = Field(..., description="List of terms/academic sessions")
    total_count: int = Field(..., alias="totalCount")
    page_count: int = Field(..., alias="pageCount")
    page_number: int = Field(..., alias="pageNumber")
    offset: int = Field(...)
    limit: int = Field(...)

