"""Response model for creating an enrollment.

POST /ims/oneroster/rostering/v1p2/enrollments
"""

from pydantic import BaseModel, Field
from timeback.models.timeback_sourced_id_pairs import TimebackSourcedIdPairs


class TimebackCreateEnrollmentResponse(BaseModel):
    """Response model for creating an enrollment."""

    sourcedIdPairs: TimebackSourcedIdPairs = Field(..., description="SourcedId mapping")

