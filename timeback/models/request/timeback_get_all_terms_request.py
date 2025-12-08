"""Request model for getting all terms.

GET /ims/oneroster/rostering/v1p2/terms
"""

from typing import Optional
from pydantic import BaseModel, Field
from timeback.models.request.timeback_query_params import TimebackQueryParams


class TimebackGetAllTermsRequest(BaseModel):
    """Request model for getting all terms (paginated list)."""

    query_params: Optional[TimebackQueryParams] = Field(None, description="Optional query parameters")

