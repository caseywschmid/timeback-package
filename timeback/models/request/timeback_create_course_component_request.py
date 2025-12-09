"""Request model for creating a course component.

POST /ims/oneroster/rostering/v1p2/courses/components
"""

from typing import Optional, Dict, Any, List
from uuid import uuid4
from pydantic import BaseModel, Field, ConfigDict
from timeback.enums import TimebackStatus
from timeback.models.timeback_sourced_id_ref import TimebackSourcedIdReference


class TimebackCreateCourseComponentBody(BaseModel):
    """Body payload for course component creation under the top-level 'courseComponent' key.

    Attributes:
        Required:
            - course (TimebackSourcedIdReference): Reference to parent course
            - title (str): Display title for the course component

        Optional:
            - sourcedId (str, optional): Client-supplied sourcedId (auto-generated UUID if omitted)
            - status (TimebackStatus, optional): Status. Defaults to "active".
            - metadata (Dict[str, Any], optional): Custom metadata
            - parent (TimebackSourcedIdReference, optional): Reference to parent component
            - sortOrder (int, optional): Position within siblings. Defaults to 0.
            - prerequisites (List[str], optional): List of prerequisite component sourcedIds
            - prerequisiteCriteria (str, optional): Criteria for completing prerequisites
            - unlockDate (str, optional): Date when the component becomes available
    """

    model_config = ConfigDict(populate_by_name=True)

    # Required fields
    course: TimebackSourcedIdReference = Field(..., description="Reference to parent course")
    title: str = Field(..., description="Display title for the course component")

    # Optional fields
    sourcedId: Optional[str] = Field(default_factory=lambda: str(uuid4()), description="Unique identifier")
    status: Optional[TimebackStatus] = Field(default=TimebackStatus.ACTIVE, description="Status")
    metadata: Optional[Dict[str, Any]] = Field(None, description="Custom metadata")
    parent: Optional[TimebackSourcedIdReference] = Field(None, description="Reference to parent component")
    sortOrder: Optional[int] = Field(default=0, description="Position within siblings")
    prerequisites: Optional[List[str]] = Field(None, description="List of prerequisite component sourcedIds")
    prerequisiteCriteria: Optional[str] = Field(None, description="Criteria for completing prerequisites")
    unlockDate: Optional[str] = Field(None, description="Date when the component becomes available")


class TimebackCreateCourseComponentRequest(BaseModel):
    """Top-level request wrapper for POST /courses/components."""

    model_config = ConfigDict(populate_by_name=True)
    courseComponent: TimebackCreateCourseComponentBody = Field(..., description="Course component data to create")

