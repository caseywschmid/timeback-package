"""Response model for getting a score scale.

Represents the body returned by:
- GET /ims/oneroster/gradebook/v1p2/scoreScales/{sourcedId}

Per spec: HTTP 200 with scoreScale object.
"""

from pydantic import BaseModel, Field
from timeback.models.timeback_score_scale import TimebackScoreScale


class TimebackGetScoreScaleResponse(BaseModel):
    """Response model for getting a single score scale.

    Attributes:
        - score_scale (TimebackScoreScale): The requested score scale. See TimebackScoreScale for structure.
    """

    score_scale: TimebackScoreScale = Field(..., description="The requested score scale", alias="scoreScale")
