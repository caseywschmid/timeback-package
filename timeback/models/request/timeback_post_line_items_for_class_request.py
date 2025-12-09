"""Request model for creating line items for a class.

POST /ims/oneroster/gradebook/v1p2/classes/{classSourcedId}/lineItems

The request body must include a lineItems array with LineItem objects.
Each line item must have: title, assignDate, dueDate, class, school, and category.
"""

from typing import List
from pydantic import BaseModel, Field
from timeback.models.request.timeback_create_line_item_request import TimebackCreateLineItemBody


class TimebackPostLineItemsForClassRequest(BaseModel):
    """Request model for POST /classes/{classSourcedId}/lineItems.
    
    Attributes:
        Required:
            - class_sourced_id (str): The sourcedId of the class (path parameter)
            - lineItems (List[TimebackCreateLineItemBody]): Array of line item data to create. See TimebackCreateLineItemBody for structure.
    """
    
    class_sourced_id: str = Field(..., description="The sourcedId of the class (path parameter)")
    lineItems: List[TimebackCreateLineItemBody] = Field(..., description="Array of line item data to create")

