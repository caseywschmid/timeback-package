"""Response model for updating/creating an assessment line item.

PUT /ims/oneroster/gradebook/v1p2/assessmentLineItems/{sourcedId}
"""

from pydantic import BaseModel, Field
from timeback.models.line_item import LineItem


class TimebackPutAssessmentLineItemResponse(BaseModel):
    """Response model for PUT assessment line item."""

    assessmentLineItem: LineItem = Field(..., description="The updated/created assessment line item")

