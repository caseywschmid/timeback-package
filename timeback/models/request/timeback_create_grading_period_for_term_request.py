"""Request model for creating a grading period for a term.

POST /ims/oneroster/rostering/v1p2/terms/{termSourcedId}/gradingPeriods
"""

from pydantic import BaseModel, Field, ConfigDict
from timeback.models.timeback_academic_session import TimebackAcademicSession


class TimebackCreateGradingPeriodForTermRequest(BaseModel):
    """Request model for creating a grading period for a specific term."""

    model_config = ConfigDict(populate_by_name=True)

    term_sourced_id: str = Field(..., description="The sourcedId of the term (path parameter)")
    academic_session: TimebackAcademicSession = Field(
        ..., alias="academicSession", description="Grading period data"
    )

