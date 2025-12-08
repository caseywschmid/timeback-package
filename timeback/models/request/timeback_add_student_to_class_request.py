"""Request model for adding a student to a class.

POST /ims/oneroster/rostering/v1p2/classes/{classSourcedId}/students
"""

from pydantic import BaseModel, Field, ConfigDict
from timeback.models.timeback_sourced_id_ref import TimebackSourcedIdReference


class TimebackAddStudentToClassRequest(BaseModel):
    """Request model for adding a student to a class."""

    model_config = ConfigDict(populate_by_name=True)

    class_sourced_id: str = Field(..., description="The sourcedId of the class")
    student: TimebackSourcedIdReference = Field(..., description="Reference to the student to add")

