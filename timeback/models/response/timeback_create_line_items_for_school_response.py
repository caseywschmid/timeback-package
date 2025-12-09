"""Response model for creating line items for a school.

Represents the body returned by:
- POST /ims/oneroster/gradebook/v1p2/schools/{sourcedId}/lineItems

Per spec: HTTP 201 with `sourcedIdPairs` mapping supplied→allocated.
"""

from pydantic import BaseModel, Field
from timeback.models.timeback_sourced_id_pairs import TimebackSourcedIdPairs


class TimebackCreateLineItemsForSchoolResponse(BaseModel):
    """Response model for creating line items for a school.

    Attributes:
        - sourcedIdPairs (TimebackSourcedIdPairs): SourcedId mapping. See TimebackSourcedIdPairs for structure.
    """

    sourcedIdPairs: TimebackSourcedIdPairs = Field(
        ..., description="Mapping from supplied to allocated sourcedId"
    )

