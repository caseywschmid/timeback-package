"""Response model for creating a resource.

POST /ims/oneroster/resources/v1p2/resources
"""

from pydantic import BaseModel, Field
from timeback.models.timeback_sourced_id_pairs import TimebackSourcedIdPairs


class TimebackCreateResourceResponse(BaseModel):
    """Response model for creating a OneRoster Resource."""

    sourcedIdPairs: TimebackSourcedIdPairs = Field(
        ..., description="Mapping from supplied to allocated sourcedId"
    )

