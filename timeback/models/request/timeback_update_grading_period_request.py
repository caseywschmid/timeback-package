"""Request model for updating a grading period.

PUT /ims/oneroster/rostering/v1p2/gradingPeriods/{sourcedId}
"""

from pydantic import BaseModel, Field, ConfigDict
from timeback.models.timeback_academic_session import TimebackAcademicSession


class TimebackUpdateGradingPeriodRequest(BaseModel):
    """Request model for updating a grading period."""

    model_config = ConfigDict(populate_by_name=True)

    sourced_id: str = Field(..., description="The sourcedId of the grading period (path parameter)")
    academic_session: TimebackAcademicSession = Field(
        ..., alias="academicSession", description="Grading period data"
    )

