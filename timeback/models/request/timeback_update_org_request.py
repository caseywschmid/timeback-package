"""Request model for updating an org.

PUT /ims/oneroster/rostering/v1p2/orgs/{sourcedId}
"""

from pydantic import BaseModel, Field, ConfigDict
from timeback.models.timeback_org import TimebackOrg


class TimebackUpdateOrgRequest(BaseModel):
    """Request model for updating an org."""

    model_config = ConfigDict(populate_by_name=True)

    sourced_id: str = Field(..., description="The sourcedId of the org (path parameter)")
    org: TimebackOrg = Field(..., description="Org data to update")

