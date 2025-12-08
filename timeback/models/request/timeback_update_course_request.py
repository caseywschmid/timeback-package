"""Request model for updating a course (PUT).

PUT /ims/oneroster/rostering/v1p2/courses/{sourcedId}
"""

from typing import Optional, Dict, Any, List
from pydantic import BaseModel, Field, ConfigDict
from timeback.enums import TimebackStatus


class TimebackUpdateCourseBody(BaseModel):
    """Body payload for course update under the top-level 'course' key."""
    
    model_config = ConfigDict(populate_by_name=True)
    
    # Optional fields for update
    sourcedId: Optional[str] = Field(None, description="Unique identifier (should match path)")
    status: Optional[TimebackStatus] = Field(None, description="Course status")
    metadata: Optional[Dict[str, Any]] = Field(None, description="Custom metadata")
    title: Optional[str] = Field(None, description="Title of the course")
    orgSourcedId: Optional[str] = Field(None, description="SourcedId of the organization")
    courseCode: Optional[str] = Field(None, description="Course code")
    grades: Optional[List[str]] = Field(None, description="List of grade levels")
    subjects: Optional[List[str]] = Field(None, description="List of subjects")
    subjectCodes: Optional[List[str]] = Field(None, description="List of subject codes")
    description: Optional[str] = Field(None, description="Course description")
    displayName: Optional[str] = Field(None, description="Display name")


class TimebackUpdateCourseRequest(BaseModel):
    """Top-level request wrapper for PUT /courses/{sourcedId}."""
    
    model_config = ConfigDict(populate_by_name=True)
    
    sourced_id: str = Field(..., description="The sourcedId of the course (path parameter)")
    course: TimebackUpdateCourseBody = Field(..., description="Course data to update")

