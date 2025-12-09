"""Request model for creating an enrollment.

POST /ims/oneroster/rostering/v1p2/enrollments
"""

from typing import Optional, Dict, Any
from uuid import uuid4
from pydantic import BaseModel, Field, ConfigDict
from timeback.enums import TimebackStatus, TimebackEnrollmentRole
from timeback.models.timeback_sourced_id_ref import TimebackSourcedIdReference


class TimebackCreateEnrollmentBody(BaseModel):
    """Body payload for enrollment creation under the top-level 'enrollment' key.
    
    Attributes:
        Required:
            - role (TimebackEnrollmentRole): Role of the user in the class
            - user (TimebackSourcedIdReference): Reference to the user
            - class_ (TimebackSourcedIdReference): Reference to the class (aliased as "class")
        
        Optional:
            - sourcedId (str, optional): Client-supplied sourcedId (auto-generated UUID if omitted)
            - status (TimebackStatus, optional): Enrollment status. Defaults to "active".
            - metadata (Dict[str, Any], optional): Custom metadata
            - primary (bool, optional): Whether this is the primary enrollment. Defaults to False.
            - beginDate (str, optional): Start date of enrollment (YYYY-MM-DD)
            - endDate (str, optional): End date of enrollment (YYYY-MM-DD)
            - school (TimebackSourcedIdReference, optional): Reference to school
    """
    
    model_config = ConfigDict(populate_by_name=True)
    
    # Required fields
    role: TimebackEnrollmentRole = Field(..., description="Role of the user in the class")
    user: TimebackSourcedIdReference = Field(..., description="Reference to the user")
    class_: TimebackSourcedIdReference = Field(..., alias="class", description="Reference to the class")
    
    # Optional fields
    sourcedId: Optional[str] = Field(default_factory=lambda: str(uuid4()), description="Unique identifier")
    status: Optional[TimebackStatus] = Field(default=TimebackStatus.ACTIVE, description="Enrollment status")
    metadata: Optional[Dict[str, Any]] = Field(None, description="Custom metadata")
    primary: Optional[bool] = Field(default=False, description="Whether this is the primary enrollment")
    beginDate: Optional[str] = Field(None, description="Start date of enrollment (YYYY-MM-DD)")
    endDate: Optional[str] = Field(None, description="End date of enrollment (YYYY-MM-DD)")
    school: Optional[TimebackSourcedIdReference] = Field(None, description="Reference to school")


class TimebackCreateEnrollmentRequest(BaseModel):
    """Top-level request wrapper for POST /enrollments.
    
    Attributes:
        Required:
            - enrollment (TimebackCreateEnrollmentBody): Enrollment data to create.
    """
    model_config = ConfigDict(populate_by_name=True)
    enrollment: TimebackCreateEnrollmentBody = Field(..., description="Enrollment data to create")

