"""Response model for getting a result.

Represents the body returned by:
- GET /ims/oneroster/gradebook/v1p2/results/{sourcedId}

Per spec: HTTP 200 with result object.
"""

from pydantic import BaseModel, Field
from timeback.models.timeback_result import TimebackResult


class TimebackGetResultResponse(BaseModel):
    """Response model for getting a single result.

    Attributes:
        - result (TimebackResult): The requested result. See TimebackResult for structure.
    """

    result: TimebackResult = Field(..., description="The requested result")

