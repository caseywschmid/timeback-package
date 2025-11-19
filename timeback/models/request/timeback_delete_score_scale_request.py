"""Request model for deleting a score scale.

DELETE /ims/oneroster/gradebook/v1p2/scoreScales/{sourcedId}
"""

from pydantic import BaseModel, Field


class TimebackDeleteScoreScaleRequest(BaseModel):
    """Request model for DELETE /scoreScales/{sourcedId}.
    
    Attributes:
        Required:
            - sourced_id (str): The sourcedId of the score scale to delete (path parameter)
    """

    sourced_id: str = Field(..., description="The sourcedId of the score scale to delete")
