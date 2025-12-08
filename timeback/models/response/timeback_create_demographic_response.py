"""Response model for creating a demographic.

POST /ims/oneroster/rostering/v1p2/demographics
"""

from pydantic import BaseModel, Field
from timeback.models.timeback_sourced_id_pairs import TimebackSourcedIdPairs


class TimebackCreateDemographicResponse(BaseModel):
    """Response model for creating a demographic."""

    sourcedIdPairs: TimebackSourcedIdPairs = Field(..., description="SourcedId mapping")

