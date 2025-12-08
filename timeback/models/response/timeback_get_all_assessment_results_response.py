"""Response model for getting all assessment results.

Represents the body returned by:
- GET /ims/oneroster/gradebook/v1p2/assessmentResults

Per spec: HTTP 200 with paginated list of assessment results.
"""

from typing import List
from pydantic import BaseModel, Field
from timeback.models.timeback_assessment_result import TimebackAssessmentResult


class TimebackGetAllAssessmentResultsResponse(BaseModel):
    """Response model for paginated assessment results list.

    Mirrors OneRoster list response envelope for assessment results.
    
    Attributes:
        - assessmentResults (List[TimebackAssessmentResult]): List of assessment results. See TimebackAssessmentResult for structure.
        - total_count (int): Total number of assessment results
        - page_count (int): Total number of pages
        - page_number (int): Current page number
        - offset (int): Offset for pagination
        - limit (int): Limit per page
    """

    assessmentResults: List[TimebackAssessmentResult] = Field(..., description="List of assessment results")
    total_count: int = Field(..., description="Total number of assessment results", alias="totalCount")
    page_count: int = Field(..., description="Total number of pages", alias="pageCount")
    page_number: int = Field(..., description="Current page number", alias="pageNumber")
    offset: int = Field(..., description="Offset for pagination")
    limit: int = Field(..., description="Limit per page")

