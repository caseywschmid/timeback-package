"""Request model for getting an assessment result.

GET /ims/oneroster/gradebook/v1p2/assessmentResults/{sourcedId}
"""

from typing import Optional
from pydantic import BaseModel, Field

from timeback.models.request.timeback_query_params import TimebackQueryParams


class TimebackGetAssessmentResultRequest(BaseModel):
    """Request model for getting an assessment result by sourcedId.
    
    Attributes:
        Required:
            - sourced_id (str): The sourcedId of the assessment result to fetch
        
        Optional:
            - query_params (TimebackQueryParams, optional): Query parameters (fields, etc.)
              See TimebackQueryParams for available options.
    """

    sourced_id: str = Field(..., description="The sourcedId of the assessment result to fetch")
    query_params: Optional[TimebackQueryParams] = Field(
        None, description="Optional query parameters (fields, etc.)"
    )

