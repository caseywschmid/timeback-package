"""Response model for getting all results.

Represents the body returned by:
- GET /ims/oneroster/gradebook/v1p2/results

Per spec: HTTP 200 with paginated list of results.
"""

from typing import List
from pydantic import BaseModel, Field
from timeback.models.timeback_result import TimebackResult


class TimebackGetAllResultsResponse(BaseModel):
    """Response model for paginated results list.

    Mirrors OneRoster list response envelope for results.
    
    Attributes:
        - results (List[TimebackResult]): List of results. See TimebackResult for structure.
        - total_count (int): Total number of results
        - page_count (int): Total number of pages
        - page_number (int): Current page number
        - offset (int): Offset for pagination
        - limit (int): Limit per page
    """

    results: List[TimebackResult] = Field(..., description="List of results")
    total_count: int = Field(..., description="Total number of results", alias="totalCount")
    page_count: int = Field(..., description="Total number of pages", alias="pageCount")
    page_number: int = Field(..., description="Current page number", alias="pageNumber")
    offset: int = Field(..., description="Offset for pagination")
    limit: int = Field(..., description="Limit per page")

