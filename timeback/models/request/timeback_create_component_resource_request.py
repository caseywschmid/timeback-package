"""Request model for creating a component resource.

POST /ims/oneroster/rostering/v1p2/courses/component-resources
"""

from typing import Optional, Dict, Any, Literal
from uuid import uuid4
from pydantic import BaseModel, Field, ConfigDict
from timeback.enums import TimebackStatus
from timeback.models.timeback_sourced_id_ref import TimebackSourcedIdReference


class TimebackCreateComponentResourceBody(BaseModel):
    """Body payload for component resource creation under the top-level 'componentResource' key.
    
    Attributes:
        Required:
            - courseComponent (TimebackSourcedIdReference): Reference to course component
            - resource (TimebackSourcedIdReference): Reference to resource
            - title (str): Display title for the component resource
        
        Optional:
            - sourcedId (str, optional): Client-supplied sourcedId (auto-generated UUID if omitted)
            - status (TimebackStatus, optional): Status. Defaults to "active".
            - metadata (Dict[str, Any], optional): Custom metadata
            - sortOrder (int, optional): Position within siblings. Defaults to 0.
            - lessonType (str, optional): Lesson type enum
    """
    
    model_config = ConfigDict(populate_by_name=True)
    
    # Required fields
    courseComponent: TimebackSourcedIdReference = Field(..., description="Reference to course component")
    resource: TimebackSourcedIdReference = Field(..., description="Reference to resource")
    title: str = Field(..., description="Display title for the component resource")
    
    # Optional fields
    sourcedId: Optional[str] = Field(default_factory=lambda: str(uuid4()), description="Unique identifier")
    status: Optional[TimebackStatus] = Field(default=TimebackStatus.ACTIVE, description="Status")
    metadata: Optional[Dict[str, Any]] = Field(None, description="Custom metadata")
    sortOrder: Optional[int] = Field(default=0, description="Position within siblings")
    lessonType: Optional[Literal["powerpath-100", "quiz", "test-out", "placement", "unit-test", "alpha-read-article"]] = Field(None, description="Lesson type")


class TimebackCreateComponentResourceRequest(BaseModel):
    """Top-level request wrapper for POST /courses/component-resources."""
    
    model_config = ConfigDict(populate_by_name=True)
    componentResource: TimebackCreateComponentResourceBody = Field(..., description="Component resource data to create")

