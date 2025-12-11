"""Request model for searching test parts within an assessment test.

GET /assessment-tests/{assessmentTestIdentifier}/test-parts

Used by:
- timeback/services/qti/endpoints/search_test_parts.py
"""

from typing import Optional
from pydantic import BaseModel, Field, ConfigDict
from timeback.enums import (
    TimebackSortOrder,
    TimebackQTINavigationMode,
    TimebackQTISubmissionMode,
)


class TimebackSearchTestPartsRequest(BaseModel):
    """Request model for searching test parts within an assessment test.
    
    Attributes:
        Optional:
            - query (str, optional): Search term for title and identifier fields (fuzzy search)
            - page (int, optional): Page number for pagination (default: 1)
            - limit (int, optional): Number of items per page (default: 10)
            - sort (str, optional): Field to sort by
            - order (TimebackSortOrder, optional): Sort order (default: desc)
            - navigation_mode (TimebackQTINavigationMode, optional): Filter by navigation mode
            - submission_mode (TimebackQTISubmissionMode, optional): Filter by submission mode
            - filter (str, optional): Advanced filter expression
    """
    
    model_config = ConfigDict(populate_by_name=True)
    
    query: Optional[str] = Field(
        None,
        description="Search title and identifier fields using a search term (fuzzy search)."
    )
    page: int = Field(1, description="Page number for pagination.", ge=1)
    limit: int = Field(10, description="Number of items per page.", ge=1, le=3000)
    sort: Optional[str] = Field(
        None,
        description="Field to sort by."
    )
    order: TimebackSortOrder = Field(
        TimebackSortOrder.DESC,
        description="Sort order (asc or desc)."
    )
    navigation_mode: Optional[TimebackQTINavigationMode] = Field(
        None,
        description="Filter by navigation mode (linear or nonlinear).",
        alias="navigationMode"
    )
    submission_mode: Optional[TimebackQTISubmissionMode] = Field(
        None,
        description="Filter by submission mode (individual or simultaneous).",
        alias="submissionMode"
    )
    filter: Optional[str] = Field(
        None,
        description="Advanced filter expression."
    )

