"""Request model for creating line items for a school.

POST /ims/oneroster/gradebook/v1p2/schools/{sourcedId}/lineItems

The request body must include a lineItems array with LineItem objects.
Each line item must have: title, assignDate, dueDate, class, school, and category.
"""

from typing import List
from pydantic import BaseModel, Field
from timeback.models.request.timeback_create_line_item_request import TimebackCreateLineItemBody


class TimebackCreateLineItemsForSchoolRequest(BaseModel):
    """Request model for POST /schools/{sourcedId}/lineItems.
    
    Attributes:
        Required:
            - school_sourced_id (str): The sourcedId of the school (path parameter)
            - lineItems (List[TimebackCreateLineItemBody]): Array of line item data to create. See TimebackCreateLineItemBody for structure.
    """
    
    school_sourced_id: str = Field(..., description="The sourcedId of the school (path parameter)")
    lineItems: List[TimebackCreateLineItemBody] = Field(..., description="Array of line item data to create")

