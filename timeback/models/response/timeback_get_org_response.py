"""Response model for getting an org.

GET /ims/oneroster/rostering/v1p2/orgs/{sourcedId}
"""

from pydantic import BaseModel, Field
from timeback.models.timeback_org import TimebackOrg


class TimebackGetOrgResponse(BaseModel):
    """Response model for getting a single org."""

    org: TimebackOrg = Field(..., description="The requested org")

