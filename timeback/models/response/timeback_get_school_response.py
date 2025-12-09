"""Response model for getting a OneRoster School.

Represents the body returned by:
- GET /ims/oneroster/rostering/v1p2/schools/{sourcedId}
"""

from pydantic import BaseModel, Field
from timeback.models.timeback_org import TimebackOrg


class TimebackGetSchoolResponse(BaseModel):
    """Response model for getting a OneRoster School.
    
    Attributes:
        - org (TimebackOrg): School (organization) object. See TimebackOrg for structure.
    """
    
    org: TimebackOrg = Field(..., description="School (organization) object")

