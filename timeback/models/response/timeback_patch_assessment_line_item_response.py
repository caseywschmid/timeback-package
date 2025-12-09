"""Response model for partially updating an assessment line item.

PATCH /ims/oneroster/gradebook/v1p2/assessmentLineItems/{sourcedId}
"""

from pydantic import BaseModel, Field
from timeback.models.line_item import LineItem


class TimebackPatchAssessmentLineItemResponse(BaseModel):
    """Response model for PATCH assessment line item."""

    assessmentLineItem: LineItem = Field(..., description="The updated assessment line item")

