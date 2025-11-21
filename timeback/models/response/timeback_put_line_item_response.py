"""Response model for updating/creating a line item.

Represents the body returned by:
- PUT /ims/oneroster/gradebook/v1p2/lineItems/{sourcedId}

Per spec: HTTP 201 with lineItem object.
"""

from pydantic import BaseModel, Field
from timeback.models.line_item import LineItem


class TimebackPutLineItemResponse(BaseModel):
    """Response model for PUT line item.

    Attributes:
        - line_item (LineItem): The updated/created line item. See LineItem for structure.
    """

    line_item: LineItem = Field(..., description="The updated/created line item", alias="lineItem")

