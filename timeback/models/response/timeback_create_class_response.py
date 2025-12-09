"""Response model for creating a OneRoster Class.

Represents the body returned by:
- POST /ims/oneroster/rostering/v1p2/classes

Per spec: HTTP 201 with `sourcedIdPairs` mapping supplied→allocated.
"""

from pydantic import BaseModel, Field

from timeback.models.timeback_sourced_id_pairs import TimebackSourcedIdPairs


class TimebackCreateClassResponse(BaseModel):
    """Response model for creating a OneRoster Class.

    Attributes:
        - sourcedIdPairs (TimebackSourcedIdPairs): SourcedId mapping. See TimebackSourcedIdPairs for structure.
    """

    sourcedIdPairs: TimebackSourcedIdPairs = Field(
        ..., description="Mapping from supplied to allocated sourcedId"
    )

