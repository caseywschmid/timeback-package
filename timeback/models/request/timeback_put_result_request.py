"""Request model for updating/creating a result.

PUT /ims/oneroster/gradebook/v1p2/results/{sourcedId}
"""

from typing import Any, Dict, Optional, List
from pydantic import BaseModel, Field, ConfigDict
from timeback.enums import TimebackStatus, TimebackScoreStatus
from timeback.models.timeback_sourced_id_ref import TimebackSourcedIdReference
from timeback.models.timeback_learning_objective_set import TimebackLearningObjectiveSet


class TimebackPutResultBody(BaseModel):
    """Body payload for result update/create under the top-level 'result' key.
    
    Attributes:
        Required:
            - lineItem (TimebackSourcedIdReference): Reference to the line item. See TimebackSourcedIdReference for structure.
            - student (TimebackSourcedIdReference): Reference to the student. See TimebackSourcedIdReference for structure.
            - scoreStatus (TimebackScoreStatus): Status of the score. See TimebackScoreStatus enum.
            - scoreDate (str): Date when the score was recorded (ISO 8601 format)
        
        Optional:
            - sourcedId (str, optional): The sourcedId of the result (should match path parameter)
            - status (TimebackStatus, optional): Result status. Defaults to "active". See TimebackStatus enum.
            - metadata (Dict[str, Any], optional): Custom metadata
            - class_ (TimebackSourcedIdReference, optional): Reference to class (aliased as "class")
            - scoreScale (TimebackSourcedIdReference, optional): Reference to score scale
            - score (float, optional): Numeric score value
            - textScore (str, optional): Text representation of the score
            - comment (str, optional): Comment about the result
            - learningObjectiveSet (List[TimebackLearningObjectiveSet], optional): Learning objective results
            - inProgress (str, optional): In progress indicator
            - incomplete (str, optional): Incomplete indicator
            - late (str, optional): Late indicator
            - missing (str, optional): Missing indicator
    """
    
    model_config = ConfigDict(populate_by_name=True)
    
    # Optional sourcedId; should match path parameter if provided
    sourcedId: Optional[str] = Field(None, description="Unique identifier (should match path parameter)")
    
    # Required fields per spec
    lineItem: TimebackSourcedIdReference = Field(..., description="Reference to the line item")
    student: TimebackSourcedIdReference = Field(..., description="Reference to the student")
    scoreStatus: TimebackScoreStatus = Field(..., description="Status of the score")
    scoreDate: str = Field(..., description="Date when the score was recorded (ISO 8601 format)")
    
    # Optional fields
    status: Optional[TimebackStatus] = Field(default=TimebackStatus.ACTIVE, description="Result status")
    metadata: Optional[Dict[str, Any]] = Field(None, description="Custom metadata")
    class_: Optional[TimebackSourcedIdReference] = Field(None, alias="class", description="Reference to class")
    scoreScale: Optional[TimebackSourcedIdReference] = Field(None, description="Reference to score scale")
    score: Optional[float] = Field(None, description="Numeric score value")
    textScore: Optional[str] = Field(None, description="Text representation of the score")
    comment: Optional[str] = Field(None, description="Comment about the result")
    learningObjectiveSet: Optional[List[TimebackLearningObjectiveSet]] = Field(None, description="Learning objective results")
    inProgress: Optional[str] = Field(None, description="In progress indicator")
    incomplete: Optional[str] = Field(None, description="Incomplete indicator")
    late: Optional[str] = Field(None, description="Late indicator")
    missing: Optional[str] = Field(None, description="Missing indicator")


class TimebackPutResultRequest(BaseModel):
    """Request model for PUT /results/{sourcedId}.
    
    Attributes:
        Required:
            - sourced_id (str): The sourcedId of the result (path parameter)
            - result (TimebackPutResultBody): Result data to update/create. See TimebackPutResultBody for structure.
    """
    
    model_config = ConfigDict(populate_by_name=True)
    
    sourced_id: str = Field(..., description="The sourcedId of the result (path parameter)")
    result: TimebackPutResultBody = Field(..., description="Result data to update/create")

