"""Response model for getting all score scales.

Represents the body returned by:
- GET /ims/oneroster/gradebook/v1p2/scoreScales

Per spec: HTTP 200 with paginated list of score scales.
"""

from typing import List
from pydantic import BaseModel, Field
from timeback.models.timeback_score_scale import TimebackScoreScale


class TimebackGetAllScoreScalesResponse(BaseModel):
    """Response model for paginated score scales list.

    Mirrors OneRoster list response envelope for score scales.
    
    Attributes:
        - score_scales (List[TimebackScoreScale]): List of score scales. See TimebackScoreScale for structure.
        - total_count (int): Total number of results
        - page_count (int): Total number of pages
        - page_number (int): Current page number
        - offset (int): Offset for pagination
        - limit (int): Limit per page
    """

    score_scales: List[TimebackScoreScale] = Field(..., description="List of score scales", alias="scoreScales")
    total_count: int = Field(..., description="Total number of results", alias="totalCount")
    page_count: int = Field(..., description="Total number of pages", alias="pageCount")
    page_number: int = Field(..., description="Current page number", alias="pageNumber")
    offset: int = Field(..., description="Offset for pagination")
    limit: int = Field(..., description="Limit per page")
