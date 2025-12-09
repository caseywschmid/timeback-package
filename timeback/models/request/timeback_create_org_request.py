"""Request model for creating an org.

POST /ims/oneroster/rostering/v1p2/orgs
"""

from pydantic import BaseModel, Field, ConfigDict
from timeback.models.timeback_org import TimebackOrg


class TimebackCreateOrgRequest(BaseModel):
    """Request model for creating an org."""

    model_config = ConfigDict(populate_by_name=True)

    org: TimebackOrg = Field(..., description="Org data to create")

