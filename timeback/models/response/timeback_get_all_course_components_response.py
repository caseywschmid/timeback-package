"""Response model for getting all course components.

GET /ims/oneroster/rostering/v1p2/courses/components
"""

from typing import List
from pydantic import BaseModel, Field, ConfigDict
from timeback.models.timeback_course_component import TimebackCourseComponent


class TimebackGetAllCourseComponentsResponse(BaseModel):
    """Response model for paginated course components list."""

    model_config = ConfigDict(populate_by_name=True)

    courseComponents: List[TimebackCourseComponent] = Field(..., description="List of course components")
    total_count: int = Field(..., alias="totalCount")
    page_count: int = Field(..., alias="pageCount")
    page_number: int = Field(..., alias="pageNumber")
    offset: int = Field(...)
    limit: int = Field(...)

