"""Request model for partially updating an assessment line item.

PATCH /ims/oneroster/gradebook/v1p2/assessmentLineItems/{sourcedId}
"""

from typing import Any, Dict, Optional, List
from pydantic import BaseModel, Field, ConfigDict
from timeback.enums import TimebackStatus
from timeback.models.timeback_sourced_id_ref import TimebackSourcedIdReference


class TimebackPatchAssessmentLineItemBody(BaseModel):
    """Body payload for partial assessment line item update. All fields optional."""
    
    model_config = ConfigDict(populate_by_name=True)
    
    sourcedId: Optional[str] = Field(None, description="Unique identifier")
    title: Optional[str] = Field(None, description="Title")
    assignDate: Optional[str] = Field(None, description="Assignment date")
    dueDate: Optional[str] = Field(None, description="Due date")
    class_: Optional[TimebackSourcedIdReference] = Field(None, alias="class", description="Reference to class")
    school: Optional[TimebackSourcedIdReference] = Field(None, description="Reference to school")
    category: Optional[TimebackSourcedIdReference] = Field(None, description="Reference to category")
    status: Optional[TimebackStatus] = Field(None, description="Status")
    description: Optional[str] = Field(None, description="Description")
    metadata: Optional[Dict[str, Any]] = Field(None, description="Custom metadata (merged)")
    scoreScale: Optional[TimebackSourcedIdReference] = Field(None, description="Reference to score scale")
    resultValueMin: Optional[float] = Field(None, description="Minimum score value")
    resultValueMax: Optional[float] = Field(None, description="Maximum score value")
    component: Optional[TimebackSourcedIdReference] = Field(None, description="Reference to component")
    componentResource: Optional[TimebackSourcedIdReference] = Field(None, description="Reference to component resource")
    learningObjectiveSet: Optional[List[Dict[str, Any]]] = Field(None, description="Learning objectives")


class TimebackPatchAssessmentLineItemRequest(BaseModel):
    """Request model for PATCH /assessmentLineItems/{sourcedId}."""
    
    model_config = ConfigDict(populate_by_name=True)
    
    sourced_id: str = Field(..., description="The sourcedId (path parameter)")
    assessmentLineItem: TimebackPatchAssessmentLineItemBody = Field(..., description="Partial data")

