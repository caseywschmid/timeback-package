"""Response model for creating a OneRoster Assessment Result.

Represents the body returned by:
- POST /ims/oneroster/gradebook/v1p2/assessmentResults

Per spec: HTTP 201 with `sourcedIdPairs` mapping supplied→allocated.
"""

from pydantic import BaseModel, Field

from timeback.models.timeback_sourced_id_pairs import TimebackSourcedIdPairs


class TimebackCreateAssessmentResultResponse(BaseModel):
    """Response model for creating a OneRoster Assessment Result.

    Attributes:
        - sourcedIdPairs (TimebackSourcedIdPairs): SourcedId mapping. See TimebackSourcedIdPairs for structure.
    """

    sourcedIdPairs: TimebackSourcedIdPairs = Field(
        ..., description="Mapping from supplied to allocated sourcedId"
    )

