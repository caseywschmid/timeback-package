"""Response model for updating/creating a result.

Represents the body returned by:
- PUT /ims/oneroster/gradebook/v1p2/results/{sourcedId}

Per spec: HTTP 201 with result object.
"""

from pydantic import BaseModel, Field
from timeback.models.timeback_result import TimebackResult


class TimebackPutResultResponse(BaseModel):
    """Response model for PUT result.

    Attributes:
        - result (TimebackResult): The updated/created result. See TimebackResult for structure.
    """

    result: TimebackResult = Field(..., description="The updated/created result")

