"""Request model for getting an assessment line item.

GET /ims/oneroster/gradebook/v1p2/assessmentLineItems/{sourcedId}
"""

from typing import Optional
from pydantic import BaseModel, Field
from timeback.models.request.timeback_query_params import TimebackQueryParams


class TimebackGetAssessmentLineItemRequest(BaseModel):
    """Request model for getting an assessment line item by sourcedId."""

    sourced_id: str = Field(..., description="The sourcedId of the assessment line item")
    query_params: Optional[TimebackQueryParams] = Field(None, description="Optional query parameters (fields, etc.)")

