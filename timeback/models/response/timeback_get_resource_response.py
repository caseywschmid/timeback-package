"""Response model for getting a resource.

GET /ims/oneroster/resources/v1p2/resources/{sourcedId}
"""

from pydantic import BaseModel, Field
from timeback.models.timeback_resource import TimebackResource


class TimebackGetResourceResponse(BaseModel):
    """Response model for getting a single resource."""

    resource: TimebackResource = Field(..., description="The requested resource")

