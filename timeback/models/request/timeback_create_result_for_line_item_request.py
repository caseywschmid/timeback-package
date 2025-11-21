"""Request model for creating results for a line item.

POST /ims/oneroster/gradebook/v1p2/lineItems/{sourcedId}/results

The request body must include a results array with Result objects.
Each result must have: lineItem (with sourcedId), student (with sourcedId), scoreStatus, and scoreDate.
"""

from typing import List
from pydantic import BaseModel, Field
from timeback.models.request.timeback_create_result_request import TimebackCreateResultBody


class TimebackCreateResultForLineItemRequest(BaseModel):
    """Request model for POST /lineItems/{sourcedId}/results.
    
    Attributes:
        Required:
            - line_item_sourced_id (str): The sourcedId of the line item (path parameter)
            - results (List[TimebackCreateResultBody]): Array of result data to create. See TimebackCreateResultBody for structure.
    """
    
    line_item_sourced_id: str = Field(..., description="The sourcedId of the line item (path parameter)")
    results: List[TimebackCreateResultBody] = Field(..., description="Array of result data to create")

