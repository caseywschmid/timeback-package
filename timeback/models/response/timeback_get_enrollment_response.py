"""Response model for getting an enrollment.

GET /ims/oneroster/rostering/v1p2/enrollments/{sourcedId}
"""

from pydantic import BaseModel, Field
from timeback.models.timeback_enrollment import TimebackEnrollment


class TimebackGetEnrollmentResponse(BaseModel):
    """Response model for getting a single enrollment."""

    enrollment: TimebackEnrollment = Field(..., description="The enrollment")

