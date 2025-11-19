"""Request model for updating/creating a score scale.

PUT /ims/oneroster/gradebook/v1p2/scoreScales/{sourcedId}
"""

from typing import Any, Dict
from pydantic import BaseModel, Field, ConfigDict
from timeback.models.timeback_score_scale import TimebackScoreScale


class TimebackPutScoreScaleRequest(BaseModel):
    """Request model for PUT /scoreScales/{sourcedId}.
    
    Attributes:
        Required:
            - sourced_id (str): The sourcedId of the score scale (path parameter)
            - score_scale (TimebackScoreScale): Score scale data to update/create
    """
    
    model_config = ConfigDict(populate_by_name=True)

    sourced_id: str = Field(..., description="The sourcedId of the score scale (path parameter)")
    score_scale: TimebackScoreScale = Field(..., alias="scoreScale", description="Score scale data")

    def to_dict(self) -> Dict[str, Any]:
        """Convert to API request body format.
        
        Returns:
            Dictionary with 'scoreScale' key containing the score scale data
        """
        # Only return the body part, sourced_id is used in the URL
        return {"scoreScale": self.score_scale.model_dump(exclude_none=True, by_alias=True)}
