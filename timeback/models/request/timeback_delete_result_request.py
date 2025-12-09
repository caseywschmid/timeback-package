"""Request model for deleting a result.

DELETE /ims/oneroster/gradebook/v1p2/results/{sourcedId}
"""

from pydantic import BaseModel, Field


class TimebackDeleteResultRequest(BaseModel):
    """Request model for DELETE /results/{sourcedId}.
    
    Attributes:
        Required:
            - sourced_id (str): The sourcedId of the result to delete (path parameter)
    """

    sourced_id: str = Field(..., description="The sourcedId of the result to delete")

