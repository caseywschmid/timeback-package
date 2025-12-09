"""Response model for getting a component resource.

GET /ims/oneroster/rostering/v1p2/courses/component-resources/{sourcedId}
"""

from pydantic import BaseModel, Field
from timeback.models.timeback_component_resource import TimebackComponentResource


class TimebackGetComponentResourceResponse(BaseModel):
    """Response model for getting a single component resource."""

    componentResource: TimebackComponentResource = Field(..., description="The component resource")

