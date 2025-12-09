"""Request model for getting a component resource.

GET /ims/oneroster/rostering/v1p2/courses/component-resources/{sourcedId}
"""

from typing import Optional
from pydantic import BaseModel, Field
from timeback.models.request.timeback_query_params import TimebackQueryParams


class TimebackGetComponentResourceRequest(BaseModel):
    """Request model for getting a component resource by sourcedId."""

    sourced_id: str = Field(..., description="The sourcedId of the component resource")
    query_params: Optional[TimebackQueryParams] = Field(None, description="Optional query parameters")

