"""Response model for creating a grading period.

POST /ims/oneroster/rostering/v1p2/gradingPeriods
"""

from pydantic import BaseModel, Field
from timeback.models.timeback_sourced_id_pairs import TimebackSourcedIdPairs


class TimebackCreateGradingPeriodResponse(BaseModel):
    """Response model for creating a grading period."""

    sourcedIdPairs: TimebackSourcedIdPairs = Field(..., description="SourcedId mapping")

