"""Request model for searching QTI assessment tests.

GET /assessment-tests

Used by:
- timeback/services/qti/endpoints/search_assessment_tests.py
"""

from typing import Optional
from pydantic import BaseModel, ConfigDict, Field
from timeback.enums import (
    TimebackQTIAssessmentTestSortField,
    TimebackSortOrder,
    TimebackQTINavigationMode,
    TimebackQTISubmissionMode,
)


class TimebackSearchAssessmentTestsRequest(BaseModel):
    """Request model for searching QTI assessment tests.
    
    All parameters are optional query parameters for filtering and pagination.
    
    Attributes:
        Optional:
            - query (str, optional): Search term for fuzzy matching on title and identifier
            - page (int, optional): Page number for pagination (default: 1)
            - limit (int, optional): Number of items per page (default: 10)
            - sort (TimebackQTIAssessmentTestSortField, optional): Field to sort by.
              See TimebackQTIAssessmentTestSortField enum for options.
            - order (TimebackSortOrder, optional): Sort order (default: desc).
              See TimebackSortOrder enum for options.
            - navigation_mode (TimebackQTINavigationMode, optional): Filter by navigation mode.
              See TimebackQTINavigationMode enum for options.
            - submission_mode (TimebackQTISubmissionMode, optional): Filter by submission mode.
              See TimebackQTISubmissionMode enum for options.
            - filter (str, optional): Advanced filter expression using =, !=, >, >=, <, <=, ~
              and logical AND/OR.
    """
    
    model_config = ConfigDict(populate_by_name=True)
    
    query: Optional[str] = Field(
        None,
        description="Search term for fuzzy matching on title and identifier fields"
    )
    page: int = Field(
        default=1,
        ge=1,
        description="Page number for pagination (1-indexed)"
    )
    limit: int = Field(
        default=10,
        ge=1,
        le=100,
        description="Number of items per page"
    )
    sort: Optional[TimebackQTIAssessmentTestSortField] = Field(
        None,
        description="Field to sort results by"
    )
    order: TimebackSortOrder = Field(
        default=TimebackSortOrder.DESC,
        description="Sort order (asc or desc)"
    )
    navigation_mode: Optional[TimebackQTINavigationMode] = Field(
        None,
        alias="navigationMode",
        description="Filter by navigation mode (linear or nonlinear)"
    )
    submission_mode: Optional[TimebackQTISubmissionMode] = Field(
        None,
        alias="submissionMode",
        description="Filter by submission mode (individual or simultaneous)"
    )
    filter: Optional[str] = Field(
        None,
        description="Advanced filter expression"
    )

