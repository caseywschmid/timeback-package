"""Request model for updating/creating a line item.

PUT /ims/oneroster/gradebook/v1p2/lineItems/{sourcedId}
"""

from typing import Any, Dict, Optional, List
from pydantic import BaseModel, Field, ConfigDict
from timeback.enums import TimebackStatus
from timeback.models.timeback_sourced_id_ref import TimebackSourcedIdReference


class TimebackPutLineItemBody(BaseModel):
    """Body payload for line item update/create under the top-level 'lineItem' key.
    
    Attributes:
        Required:
            - title (str): Title of the line item
            - assignDate (str): Assignment date (ISO 8601 format)
            - dueDate (str): Due date (ISO 8601 format)
            - class_ (TimebackSourcedIdReference): Reference to class (aliased as "class"). See TimebackSourcedIdReference for structure.
            - school (TimebackSourcedIdReference): Reference to school. See TimebackSourcedIdReference for structure.
            - category (TimebackSourcedIdReference): Reference to category. See TimebackSourcedIdReference for structure.
        
        Optional:
            - sourcedId (str, optional): The sourcedId of the line item (should match path parameter)
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
    
    # Optional sourcedId; should match path parameter if provided
    sourcedId: Optional[str] = Field(None, description="Unique identifier (should match path parameter)")
    
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


class TimebackPutLineItemRequest(BaseModel):
    """Request model for PUT /lineItems/{sourcedId}.
    
    Attributes:
        Required:
            - sourced_id (str): The sourcedId of the line item (path parameter)
            - lineItem (TimebackPutLineItemBody): Line item data to update/create. See TimebackPutLineItemBody for structure.
    """
    
    model_config = ConfigDict(populate_by_name=True)
    
    sourced_id: str = Field(..., description="The sourcedId of the line item (path parameter)")
    lineItem: TimebackPutLineItemBody = Field(..., description="Line item data to update/create")

