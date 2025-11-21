"""Request model for creating a OneRoster Line Item.

POST /ims/oneroster/gradebook/v1p2/lineItems

The request body must include a lineItem object with required fields:
title, assignDate, dueDate, class, school, and category.
"""

from typing import Any, Dict, Optional, List
from pydantic import BaseModel, Field, ConfigDict
from uuid import uuid4
from timeback.enums import TimebackStatus
from timeback.models.timeback_sourced_id_ref import TimebackSourcedIdReference


class TimebackCreateLineItemBody(BaseModel):
    """Body payload for line item creation under the top-level 'lineItem' key.
    
    Attributes:
        Required:
            - title (str): Title of the line item
            - assignDate (str): Assignment date (ISO 8601 format)
            - dueDate (str): Due date (ISO 8601 format)
            - class_ (TimebackSourcedIdReference): Reference to class (aliased as "class"). See TimebackSourcedIdReference for structure.
            - school (TimebackSourcedIdReference): Reference to school. See TimebackSourcedIdReference for structure.
            - category (TimebackSourcedIdReference): Reference to category. See TimebackSourcedIdReference for structure.
        
        Optional:
            - sourcedId (str, optional): Client-supplied sourcedId (auto-generated UUID if omitted)
            - status (TimebackStatus, optional): Line item status. Defaults to "active". See TimebackStatus enum.
            - description (str, optional): Description of the line item
            - metadata (Dict[str, Any], optional): Custom metadata
            - scoreScale (TimebackSourcedIdReference, optional): Reference to score scale
            - resultValueMin (float, optional): Minimum score value
            - resultValueMax (float, optional): Maximum score value
            - learningObjectiveSet (List[Dict[str, Any]], optional): Learning objective results
            - gradingPeriod (TimebackSourcedIdReference, optional): Reference to grading period (nullable)
            - academicSession (TimebackSourcedIdReference, optional): Reference to academic session (nullable)
    """
    
    model_config = ConfigDict(populate_by_name=True)
    
    # Optional client-supplied sourcedId; if omitted, auto-generate a UUID string
    sourcedId: Optional[str] = Field(default_factory=lambda: str(uuid4()), description="Unique identifier")
    
    # Required fields per spec
    title: str = Field(..., description="Title of the line item")
    assignDate: str = Field(..., description="Assignment date (ISO 8601 format)")
    dueDate: str = Field(..., description="Due date (ISO 8601 format)")
    class_: TimebackSourcedIdReference = Field(..., alias="class", description="Reference to class")
    school: TimebackSourcedIdReference = Field(..., description="Reference to school")
    category: TimebackSourcedIdReference = Field(..., description="Reference to category")
    
    # Optional fields
    status: Optional[TimebackStatus] = Field(default=TimebackStatus.ACTIVE, description="Line item status")
    description: Optional[str] = Field(None, description="Description of the line item")
    metadata: Optional[Dict[str, Any]] = Field(None, description="Custom metadata")
    scoreScale: Optional[TimebackSourcedIdReference] = Field(None, description="Reference to score scale")
    resultValueMin: Optional[float] = Field(None, description="Minimum score value")
    resultValueMax: Optional[float] = Field(None, description="Maximum score value")
    learningObjectiveSet: Optional[List[Dict[str, Any]]] = Field(None, description="Learning objective results")
    gradingPeriod: Optional[TimebackSourcedIdReference] = Field(None, description="Reference to grading period")
    academicSession: Optional[TimebackSourcedIdReference] = Field(None, description="Reference to academic session")


class TimebackCreateLineItemRequest(BaseModel):
    """Top-level request wrapper for POST /lineItems.
    
    Attributes:
        Required:
            - lineItem (TimebackCreateLineItemBody): Line item data to create. See TimebackCreateLineItemBody for structure.
    """
    
    lineItem: TimebackCreateLineItemBody

