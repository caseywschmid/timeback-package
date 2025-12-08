"""Request model for creating a OneRoster Assessment Line Item.

POST /ims/oneroster/gradebook/v1p2/assessmentLineItems

The request body must include an assessmentLineItem object with required field: title.
"""

from typing import Any, Dict, Optional, List
from pydantic import BaseModel, Field, ConfigDict
from uuid import uuid4
from timeback.enums import TimebackStatus
from timeback.models.timeback_sourced_id_ref import TimebackSourcedIdReference


class TimebackCreateAssessmentLineItemBody(BaseModel):
    """Body payload for assessment line item creation under 'assessmentLineItem' key.
    
    Attributes:
        Required:
            - title (str): Title of the assessment line item
            - assignDate (str): Assignment date (ISO 8601 format)
            - dueDate (str): Due date (ISO 8601 format)
            - class_ (TimebackSourcedIdReference): Reference to class (aliased as "class")
            - school (TimebackSourcedIdReference): Reference to school
            - category (TimebackSourcedIdReference): Reference to category
        
        Optional:
            - sourcedId (str, optional): Client-supplied sourcedId (auto-generated UUID if omitted)
            - status (TimebackStatus, optional): Status. Defaults to "active"
            - description (str, optional): Description
            - metadata (Dict[str, Any], optional): Custom metadata
            - scoreScale (TimebackSourcedIdReference, optional): Reference to score scale
            - resultValueMin (float, optional): Minimum score value
            - resultValueMax (float, optional): Maximum score value
            - component (TimebackSourcedIdReference, optional): Reference to component (proprietary)
            - componentResource (TimebackSourcedIdReference, optional): Reference to component resource (proprietary)
    """
    
    model_config = ConfigDict(populate_by_name=True)
    
    sourcedId: Optional[str] = Field(default_factory=lambda: str(uuid4()), description="Unique identifier")
    
    # Required fields
    title: str = Field(..., description="Title of the assessment line item")
    assignDate: str = Field(..., description="Assignment date (ISO 8601 format)")
    dueDate: str = Field(..., description="Due date (ISO 8601 format)")
    class_: TimebackSourcedIdReference = Field(..., alias="class", description="Reference to class")
    school: TimebackSourcedIdReference = Field(..., description="Reference to school")
    category: TimebackSourcedIdReference = Field(..., description="Reference to category")
    
    # Optional fields
    status: Optional[TimebackStatus] = Field(default=TimebackStatus.ACTIVE, description="Status")
    description: Optional[str] = Field(None, description="Description")
    metadata: Optional[Dict[str, Any]] = Field(None, description="Custom metadata")
    scoreScale: Optional[TimebackSourcedIdReference] = Field(None, description="Reference to score scale")
    resultValueMin: Optional[float] = Field(None, description="Minimum score value")
    resultValueMax: Optional[float] = Field(None, description="Maximum score value")
    component: Optional[TimebackSourcedIdReference] = Field(None, description="Reference to component (proprietary)")
    componentResource: Optional[TimebackSourcedIdReference] = Field(None, description="Reference to component resource (proprietary)")
    learningObjectiveSet: Optional[List[Dict[str, Any]]] = Field(None, description="Learning objectives")


class TimebackCreateAssessmentLineItemRequest(BaseModel):
    """Top-level request wrapper for POST /assessmentLineItems."""
    
    assessmentLineItem: TimebackCreateAssessmentLineItemBody

