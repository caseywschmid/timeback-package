"""Response model for updating a OneRoster School.

Represents the body returned by:
- PUT /ims/oneroster/rostering/v1p2/schools/{sourcedId}
"""

from pydantic import BaseModel, Field
from timeback.models.timeback_org import TimebackOrg


class TimebackUpdateSchoolResponse(BaseModel):
    """Response model for updating a OneRoster School.
    
    Attributes:
        - org (TimebackOrg): Updated school (organization) object. See TimebackOrg for structure.
    """
    
    org: TimebackOrg = Field(..., description="Updated school (organization) object")

