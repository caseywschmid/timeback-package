"""Response model for getting score scales for a school.

Represents the body returned by:
- GET /ims/oneroster/gradebook/v1p2/schools/{sourcedId}/scoreScales

Per spec: HTTP 200 with scoreScales collection and pagination info.
"""

from typing import List
from pydantic import BaseModel, Field, ConfigDict
from timeback.models.timeback_score_scale import TimebackScoreScale


class TimebackGetScoreScalesForSchoolResponse(BaseModel):
    """Response model for getting score scales for a school.

    Attributes:
        - score_scales (List[TimebackScoreScale]): List of score scales.
        - total_count (int): Total number of records available.
        - page_count (int): Total number of pages.
        - page_number (int): Current page number.
        - offset (int): Current offset.
        - limit (int): Current limit.
    """

    model_config = ConfigDict(populate_by_name=True)

    score_scales: List[TimebackScoreScale] = Field(..., alias="scoreScales")
    total_count: int = Field(..., alias="totalCount")
    page_count: int = Field(..., alias="pageCount")
    page_number: int = Field(..., alias="pageNumber")
    offset: int = Field(..., alias="offset")
    limit: int = Field(..., alias="limit")
