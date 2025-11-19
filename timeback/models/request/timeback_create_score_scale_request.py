"""Request model for creating a Score Scale.

POST /ims/oneroster/gradebook/v1p2/scoreScales
"""

from typing import Any, Dict
from pydantic import BaseModel, Field, ConfigDict
from timeback.models.timeback_score_scale import TimebackScoreScale


class TimebackCreateScoreScaleRequest(BaseModel):
    """Top-level request wrapper for POST /scoreScales.
    
    Attributes:
        Required:
            - score_scale (TimebackScoreScale): Score scale data to create. See TimebackScoreScale for structure.
    """
    
    model_config = ConfigDict(populate_by_name=True)

    score_scale: TimebackScoreScale = Field(..., alias="scoreScale")

