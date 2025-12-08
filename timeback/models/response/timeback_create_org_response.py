"""Response model for creating an org.

POST /ims/oneroster/rostering/v1p2/orgs
"""

from pydantic import BaseModel, Field
from timeback.models.timeback_sourced_id_pairs import TimebackSourcedIdPairs


class TimebackCreateOrgResponse(BaseModel):
    """Response model for creating an org."""

    sourcedIdPairs: TimebackSourcedIdPairs = Field(..., description="SourcedId mapping")

