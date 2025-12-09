"""Response model for creating a OneRoster Assessment Line Item.

Represents the body returned by:
- POST /ims/oneroster/gradebook/v1p2/assessmentLineItems

Per spec: HTTP 201 with `sourcedIdPairs` mapping supplied→allocated.
"""

from pydantic import BaseModel, Field
from timeback.models.timeback_sourced_id_pairs import TimebackSourcedIdPairs


class TimebackCreateAssessmentLineItemResponse(BaseModel):
    """Response model for creating a OneRoster Assessment Line Item."""

    sourcedIdPairs: TimebackSourcedIdPairs = Field(
        ..., description="Mapping from supplied to allocated sourcedId"
    )

