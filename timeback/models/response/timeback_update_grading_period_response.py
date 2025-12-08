"""Response model for updating a grading period.

PUT /ims/oneroster/rostering/v1p2/gradingPeriods/{sourcedId}
"""

from pydantic import BaseModel, Field
from timeback.models.timeback_academic_session import TimebackAcademicSession


class TimebackUpdateGradingPeriodResponse(BaseModel):
    """Response model for updating a grading period."""

    academicSession: TimebackAcademicSession = Field(..., description="The updated grading period")

