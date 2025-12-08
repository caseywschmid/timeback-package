"""Response model for getting all courses.

GET /ims/oneroster/rostering/v1p2/courses
"""

from typing import List
from pydantic import BaseModel, Field, ConfigDict
from timeback.models.timeback_course import TimebackCourse


class TimebackGetAllCoursesResponse(BaseModel):
    """Response model for paginated courses list."""

    model_config = ConfigDict(populate_by_name=True)

    courses: List[TimebackCourse] = Field(..., description="List of courses")
    total_count: int = Field(..., alias="totalCount")
    page_count: int = Field(..., alias="pageCount")
    page_number: int = Field(..., alias="pageNumber")
    offset: int = Field(...)
    limit: int = Field(...)

