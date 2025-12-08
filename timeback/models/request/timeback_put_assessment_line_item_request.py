"""Request model for updating/creating an assessment line item.

PUT /ims/oneroster/gradebook/v1p2/assessmentLineItems/{sourcedId}
"""

from typing import Any, Dict, Optional, List
from pydantic import BaseModel, Field, ConfigDict
from timeback.enums import TimebackStatus
from timeback.models.timeback_sourced_id_ref import TimebackSourcedIdReference


class TimebackPutAssessmentLineItemBody(BaseModel):
    """Body payload for assessment line item update/create."""
    
    model_config = ConfigDict(populate_by_name=True)
    
    sourcedId: Optional[str] = Field(None, description="Unique identifier (should match path)")
    title: str = Field(..., description="Title")
    assignDate: str = Field(..., description="Assignment date (ISO 8601)")
    dueDate: str = Field(..., description="Due date (ISO 8601)")
    class_: TimebackSourcedIdReference = Field(..., alias="class", description="Reference to class")
    school: TimebackSourcedIdReference = Field(..., description="Reference to school")
    category: TimebackSourcedIdReference = Field(..., description="Reference to category")
    
    status: Optional[TimebackStatus] = Field(default=TimebackStatus.ACTIVE, description="Status")
    description: Optional[str] = Field(None, description="Description")
    metadata: Optional[Dict[str, Any]] = Field(None, description="Custom metadata")
    scoreScale: Optional[TimebackSourcedIdReference] = Field(None, description="Reference to score scale")
    resultValueMin: Optional[float] = Field(None, description="Minimum score value")
    resultValueMax: Optional[float] = Field(None, description="Maximum score value")
    component: Optional[TimebackSourcedIdReference] = Field(None, description="Reference to component")
    componentResource: Optional[TimebackSourcedIdReference] = Field(None, description="Reference to component resource")
    learningObjectiveSet: Optional[List[Dict[str, Any]]] = Field(None, description="Learning objectives")


class TimebackPutAssessmentLineItemRequest(BaseModel):
    """Request model for PUT /assessmentLineItems/{sourcedId}."""
    
    model_config = ConfigDict(populate_by_name=True)
    
    sourced_id: str = Field(..., description="The sourcedId (path parameter)")
    assessmentLineItem: TimebackPutAssessmentLineItemBody = Field(..., description="Assessment line item data")

