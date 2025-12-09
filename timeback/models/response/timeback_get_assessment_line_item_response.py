"""Response model for getting an assessment line item.

GET /ims/oneroster/gradebook/v1p2/assessmentLineItems/{sourcedId}
"""

from pydantic import BaseModel, Field
from timeback.models.line_item import LineItem


class TimebackGetAssessmentLineItemResponse(BaseModel):
    """Response model for getting a single assessment line item."""

    assessmentLineItem: LineItem = Field(..., description="The requested assessment line item")

