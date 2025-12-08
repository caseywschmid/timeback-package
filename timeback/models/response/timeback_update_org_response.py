"""Response model for updating an org.

PUT /ims/oneroster/rostering/v1p2/orgs/{sourcedId}
"""

from pydantic import BaseModel, Field
from timeback.models.timeback_org import TimebackOrg


class TimebackUpdateOrgResponse(BaseModel):
    """Response model for updating an org."""

    org: TimebackOrg = Field(..., description="The updated org")

