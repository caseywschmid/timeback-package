"""Request model for updating an enrollment (PUT).

PUT /ims/oneroster/rostering/v1p2/enrollments/{sourcedId}
"""

from typing import Optional, Dict, Any
from pydantic import BaseModel, Field, ConfigDict
from timeback.enums import TimebackStatus, TimebackEnrollmentRole
from timeback.models.timeback_sourced_id_ref import TimebackSourcedIdReference


class TimebackUpdateEnrollmentBody(BaseModel):
    """Body payload for enrollment update under the top-level 'enrollment' key.
    
    All fields are optional for PUT - only include what you want to update.
    """
    
    model_config = ConfigDict(populate_by_name=True)
    
    status: Optional[TimebackStatus] = Field(None, description="Enrollment status")
    metadata: Optional[Dict[str, Any]] = Field(None, description="Custom metadata")
    role: Optional[TimebackEnrollmentRole] = Field(None, description="Role of the user in the class")
    primary: Optional[bool] = Field(None, description="Whether this is the primary enrollment")
    beginDate: Optional[str] = Field(None, description="Start date of enrollment (YYYY-MM-DD)")
    endDate: Optional[str] = Field(None, description="End date of enrollment (YYYY-MM-DD)")
    user: Optional[TimebackSourcedIdReference] = Field(None, description="Reference to the user")
    class_: Optional[TimebackSourcedIdReference] = Field(None, alias="class", description="Reference to the class")
    school: Optional[TimebackSourcedIdReference] = Field(None, description="Reference to school")


class TimebackUpdateEnrollmentRequest(BaseModel):
    """Top-level request wrapper for PUT /enrollments/{sourcedId}."""
    
    model_config = ConfigDict(populate_by_name=True)
    
    sourced_id: str = Field(..., description="The sourcedId of the enrollment (path parameter)")
    enrollment: TimebackUpdateEnrollmentBody = Field(..., description="Enrollment data to update")

