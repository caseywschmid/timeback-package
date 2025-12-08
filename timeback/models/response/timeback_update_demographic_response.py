"""Response model for updating a demographic.

PUT /ims/oneroster/rostering/v1p2/demographics/{sourcedId}
"""

from pydantic import BaseModel, Field
from timeback.models.timeback_demographic import TimebackDemographic


class TimebackUpdateDemographicResponse(BaseModel):
    """Response model for updating a demographic."""

    demographics: TimebackDemographic = Field(..., description="The updated demographic")

