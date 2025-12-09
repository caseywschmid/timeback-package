"""Response model for updating a component resource.

PUT /ims/oneroster/rostering/v1p2/courses/component-resources/{sourcedId}
"""

from pydantic import BaseModel, Field
from timeback.models.timeback_component_resource import TimebackComponentResource


class TimebackUpdateComponentResourceResponse(BaseModel):
    """Response model for updating a component resource."""

    componentResource: TimebackComponentResource = Field(..., description="The updated component resource")

