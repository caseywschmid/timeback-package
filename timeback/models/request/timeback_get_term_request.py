"""Request model for getting a term.

GET /ims/oneroster/rostering/v1p2/terms/{sourcedId}
"""

from typing import Optional
from pydantic import BaseModel, Field
from timeback.models.request.timeback_query_params import TimebackQueryParams


class TimebackGetTermRequest(BaseModel):
    """Request model for getting a term by sourcedId."""

    sourced_id: str = Field(..., description="The sourcedId of the term")
    query_params: Optional[TimebackQueryParams] = Field(None, description="Optional query parameters")

