"""Request model for creating a grading period.

POST /ims/oneroster/rostering/v1p2/gradingPeriods
"""

from pydantic import BaseModel, Field, ConfigDict
from timeback.models.timeback_academic_session import TimebackAcademicSession


class TimebackCreateGradingPeriodRequest(BaseModel):
    """Request model for creating a grading period.
    
    Attributes:
        Required:
            - academic_session (TimebackAcademicSession): The grading period data.
              The `type` field should be set to `gradingPeriod`.
    """

    model_config = ConfigDict(populate_by_name=True)

    academic_session: TimebackAcademicSession = Field(
        ..., alias="academicSession", description="Grading period data"
    )

