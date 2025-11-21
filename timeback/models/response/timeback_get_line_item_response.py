"""Response model for getting a line item.

Represents the body returned by:
- GET /ims/oneroster/gradebook/v1p2/lineItems/{sourcedId}

Per spec: HTTP 200 with lineItem object.
"""

from pydantic import BaseModel, Field
from timeback.models.line_item import LineItem


class TimebackGetLineItemResponse(BaseModel):
    """Response model for getting a single line item.

    Attributes:
        - line_item (LineItem): The requested line item. See LineItem for structure.
    """

    line_item: LineItem = Field(..., description="The requested line item", alias="lineItem")

