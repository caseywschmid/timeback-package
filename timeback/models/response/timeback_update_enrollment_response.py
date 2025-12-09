"""Response model for updating an enrollment.

PUT/PATCH /ims/oneroster/rostering/v1p2/enrollments/{sourcedId}
"""

from pydantic import BaseModel, Field
from timeback.models.timeback_enrollment import TimebackEnrollment


class TimebackUpdateEnrollmentResponse(BaseModel):
    """Response model for updating an enrollment."""

    enrollment: TimebackEnrollment = Field(..., description="The updated enrollment")

