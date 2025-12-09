"""Course Component model for the TimeBack API.

This module defines the CourseComponent model which represents a component or module
of a course, following the OneRoster 1.2 specification.
"""

from typing import Dict, Any, Optional, List
from datetime import datetime, timezone
from pydantic import BaseModel, Field, ConfigDict
from timeback.enums import TimebackStatus
from timeback.models.timeback_sourced_id_ref import TimebackSourcedIdReference


class TimebackCourseComponent(BaseModel):
    """Represents a component (module/unit/lesson) of a course.

    Required fields per OneRoster 1.2 spec:
    - sourcedId: Unique identifier for the course component
    - status: Current status ('active' or 'tobedeleted')
    - course: Reference to the parent course
    - title: Display title for the course component

    Optional fields:
    - dateLastModified: Timestamp of last modification (ISO string)
    - metadata: Additional metadata as key-value pairs
    - parent: Reference to parent component (for nested hierarchy)
    - sortOrder: Position within siblings (defaults to 0)
    - prerequisites: List of prerequisite component sourcedIds
    - prerequisiteCriteria: Criteria for completing prerequisites
    - unlockDate: Date when the component becomes available
    """

    model_config = ConfigDict(populate_by_name=True)

    # Required fields
    sourcedId: str = Field(..., description="Unique identifier for the course component")
    status: TimebackStatus = Field(TimebackStatus.ACTIVE, description="Status of the course component")
    course: TimebackSourcedIdReference = Field(..., description="Reference to the parent course")
    title: str = Field(..., description="Display title for the course component")

    # Optional fields
    dateLastModified: str = Field(
        default_factory=lambda: datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        description="Date last modified (ISO 8601 format)"
    )
    metadata: Optional[Dict[str, Any]] = Field(None, description="Custom metadata")
    parent: Optional[TimebackSourcedIdReference] = Field(None, description="Reference to parent component")
    sortOrder: Optional[int] = Field(0, description="Position within siblings")
    prerequisites: Optional[List[str]] = Field(None, description="List of prerequisite component sourcedIds")
    prerequisiteCriteria: Optional[str] = Field(None, description="Criteria for completing prerequisites")
    unlockDate: Optional[str] = Field(None, description="Date when the component becomes available")

