"""Request model for getting classes for a term.

GET /ims/oneroster/rostering/v1p2/terms/{termSourcedId}/classes
"""

from typing import Optional
from pydantic import BaseModel, Field
from timeback.models.request.timeback_query_params import TimebackQueryParams


class TimebackGetClassesForTermRequest(BaseModel):
    """Request model for getting classes for a specific term."""

    term_sourced_id: str = Field(..., description="The sourcedId of the term")
    query_params: Optional[TimebackQueryParams] = Field(None, description="Optional query parameters")

