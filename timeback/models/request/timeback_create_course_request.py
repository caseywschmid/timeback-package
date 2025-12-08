"""Request model for creating a course.

POST /ims/oneroster/rostering/v1p2/courses
"""

from typing import Optional, Dict, Any, List
from uuid import uuid4
from pydantic import BaseModel, Field, ConfigDict
from timeback.enums import TimebackStatus
from timeback.models.timeback_sourced_id_ref import TimebackSourcedIdReference


class TimebackCreateCourseBody(BaseModel):
    """Body payload for course creation under the top-level 'course' key.
    
    Attributes:
        Required:
            - title (str): Title of the course
            - orgSourcedId (str): SourcedId of the organization
        
        Optional:
            - sourcedId (str, optional): Client-supplied sourcedId (auto-generated UUID if omitted)
            - status (TimebackStatus, optional): Course status. Defaults to "active".
            - metadata (Dict[str, Any], optional): Custom metadata
            - courseCode (str, optional): Course code
            - grades (List[str], optional): List of grade levels
            - subjects (List[str], optional): List of subjects
            - subjectCodes (List[str], optional): List of subject codes
            - description (str, optional): Course description
            - displayName (str, optional): Display name
    """
    
    model_config = ConfigDict(populate_by_name=True)
    
    # Required fields
    title: str = Field(..., description="Title of the course")
    orgSourcedId: str = Field(..., description="SourcedId of the organization")
    
    # Optional fields
    sourcedId: Optional[str] = Field(default_factory=lambda: str(uuid4()), description="Unique identifier")
    status: Optional[TimebackStatus] = Field(default=TimebackStatus.ACTIVE, description="Course status")
    metadata: Optional[Dict[str, Any]] = Field(None, description="Custom metadata")
    courseCode: Optional[str] = Field(None, description="Course code")
    grades: Optional[List[str]] = Field(None, description="List of grade levels")
    subjects: Optional[List[str]] = Field(None, description="List of subjects")
    subjectCodes: Optional[List[str]] = Field(None, description="List of subject codes")
    description: Optional[str] = Field(None, description="Course description")
    displayName: Optional[str] = Field(None, description="Display name")


class TimebackCreateCourseRequest(BaseModel):
    """Top-level request wrapper for POST /courses."""
    
    model_config = ConfigDict(populate_by_name=True)
    course: TimebackCreateCourseBody = Field(..., description="Course data to create")

