"""Response model for updating a resource.

PUT /ims/oneroster/resources/v1p2/resources/{sourcedId}
"""

from pydantic import BaseModel, Field
from timeback.models.timeback_resource import TimebackResource


class TimebackUpdateResourceResponse(BaseModel):
    """Response model for updating a resource."""

    resource: TimebackResource = Field(..., description="The updated resource")

