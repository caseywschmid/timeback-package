"""Response model for getting a demographic.

GET /ims/oneroster/rostering/v1p2/demographics/{sourcedId}
"""

from pydantic import BaseModel, Field
from timeback.models.timeback_demographic import TimebackDemographic


class TimebackGetDemographicResponse(BaseModel):
    """Response model for getting a single demographic."""

    demographics: TimebackDemographic = Field(..., description="The demographic")

