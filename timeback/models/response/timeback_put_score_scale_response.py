"""Response model for updating/creating a score scale.

Represents the body returned by:
- PUT /ims/oneroster/gradebook/v1p2/scoreScales/{sourcedId}

Per spec: HTTP 201 with scoreScale object.
"""

from pydantic import BaseModel, Field
from timeback.models.timeback_score_scale import TimebackScoreScale


class TimebackPutScoreScaleResponse(BaseModel):
    """Response model for PUT score scale.

    Attributes:
        - score_scale (TimebackScoreScale): The updated/created score scale.
    """

    score_scale: TimebackScoreScale = Field(..., description="The updated/created score scale", alias="scoreScale")
