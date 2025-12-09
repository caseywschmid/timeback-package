"""Request model for updating a course component (PUT).

PUT /ims/oneroster/rostering/v1p2/courses/components/{sourcedId}
"""

from typing import Optional, Dict, Any, List
from pydantic import BaseModel, Field, ConfigDict
from timeback.enums import TimebackStatus
from timeback.models.timeback_sourced_id_ref import TimebackSourcedIdReference


class TimebackUpdateCourseComponentBody(BaseModel):
    """Body payload for course component update under the top-level 'courseComponent' key."""

    model_config = ConfigDict(populate_by_name=True)

    # Optional fields for update
    sourcedId: Optional[str] = Field(None, description="Unique identifier (should match path)")
    status: Optional[TimebackStatus] = Field(None, description="Status")
    metadata: Optional[Dict[str, Any]] = Field(None, description="Custom metadata")
    course: Optional[TimebackSourcedIdReference] = Field(None, description="Reference to parent course")
    parent: Optional[TimebackSourcedIdReference] = Field(None, description="Reference to parent component")
    title: Optional[str] = Field(None, description="Display title for the course component")
    sortOrder: Optional[int] = Field(None, description="Position within siblings")
    prerequisites: Optional[List[str]] = Field(None, description="List of prerequisite component sourcedIds")
    prerequisiteCriteria: Optional[str] = Field(None, description="Criteria for completing prerequisites")
    unlockDate: Optional[str] = Field(None, description="Date when the component becomes available")


class TimebackUpdateCourseComponentRequest(BaseModel):
    """Top-level request wrapper for PUT /courses/components/{sourcedId}."""

    model_config = ConfigDict(populate_by_name=True)

    sourced_id: str = Field(..., description="The sourcedId of the course component (path parameter)")
    courseComponent: TimebackUpdateCourseComponentBody = Field(..., description="Course component data to update")

