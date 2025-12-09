"""Response model for creating a component resource.

POST /ims/oneroster/rostering/v1p2/courses/component-resources
"""

from pydantic import BaseModel, Field
from timeback.models.timeback_sourced_id_pairs import TimebackSourcedIdPairs


class TimebackCreateComponentResourceResponse(BaseModel):
    """Response model for creating a component resource."""

    sourcedIdPairs: TimebackSourcedIdPairs = Field(..., description="SourcedId mapping")

