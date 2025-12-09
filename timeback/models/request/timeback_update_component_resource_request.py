"""Request model for updating a component resource (PUT).

PUT /ims/oneroster/rostering/v1p2/courses/component-resources/{sourcedId}
"""

from typing import Optional, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from timeback.enums import TimebackStatus
from timeback.models.timeback_sourced_id_ref import TimebackSourcedIdReference


class TimebackUpdateComponentResourceBody(BaseModel):
    """Body payload for component resource update under the top-level 'componentResource' key."""
    
    model_config = ConfigDict(populate_by_name=True)
    
    # Optional fields for update
    sourcedId: Optional[str] = Field(None, description="Unique identifier (should match path)")
    status: Optional[TimebackStatus] = Field(None, description="Status")
    metadata: Optional[Dict[str, Any]] = Field(None, description="Custom metadata")
    courseComponent: Optional[TimebackSourcedIdReference] = Field(None, description="Reference to course component")
    resource: Optional[TimebackSourcedIdReference] = Field(None, description="Reference to resource")
    title: Optional[str] = Field(None, description="Display title for the component resource")
    sortOrder: Optional[int] = Field(None, description="Position within siblings")
    lessonType: Optional[Literal["powerpath-100", "quiz", "test-out", "placement", "unit-test", "alpha-read-article"]] = Field(None, description="Lesson type")


class TimebackUpdateComponentResourceRequest(BaseModel):
    """Top-level request wrapper for PUT /courses/component-resources/{sourcedId}."""
    
    model_config = ConfigDict(populate_by_name=True)
    
    sourced_id: str = Field(..., description="The sourcedId of the component resource (path parameter)")
    componentResource: TimebackUpdateComponentResourceBody = Field(..., description="Component resource data to update")

