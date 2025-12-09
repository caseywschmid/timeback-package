"""Request model for deleting a line item.

DELETE /ims/oneroster/gradebook/v1p2/lineItems/{sourcedId}
"""

from pydantic import BaseModel, Field


class TimebackDeleteLineItemRequest(BaseModel):
    """Request model for DELETE /lineItems/{sourcedId}.
    
    Attributes:
        Required:
            - sourced_id (str): The sourcedId of the line item to delete (path parameter)
    """

    sourced_id: str = Field(..., description="The sourcedId of the line item to delete")

