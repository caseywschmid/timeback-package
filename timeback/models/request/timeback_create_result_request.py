"""Request model for creating a OneRoster Result.

POST /ims/oneroster/gradebook/v1p2/results

The request body must include a result object with required fields:
lineItem (with sourcedId), student (with sourcedId), scoreStatus, and scoreDate.
"""

from typing import Any, Dict, Optional, List
from pydantic import BaseModel, Field, ConfigDict
from uuid import uuid4
from timeback.enums import TimebackStatus, TimebackScoreStatus
from timeback.models.timeback_sourced_id_ref import TimebackSourcedIdReference
from timeback.models.timeback_learning_objective_set import TimebackLearningObjectiveSet


class TimebackCreateResultBody(BaseModel):
    """Body payload for result creation under the top-level 'result' key.
    
    Attributes:
        Required:
            - lineItem (TimebackSourcedIdReference): Reference to the line item. See TimebackSourcedIdReference for structure.
            - student (TimebackSourcedIdReference): Reference to the student. See TimebackSourcedIdReference for structure.
            - scoreStatus (TimebackScoreStatus): Status of the score. See TimebackScoreStatus enum.
            - scoreDate (str): Date when the score was recorded (ISO 8601 format)
        
        Optional:
            - sourcedId (str, optional): Client-supplied sourcedId (auto-generated UUID if omitted)
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
    
    # Optional client-supplied sourcedId; if omitted, auto-generate a UUID string
    sourcedId: Optional[str] = Field(default_factory=lambda: str(uuid4()), description="Unique identifier")
    
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


class TimebackCreateResultRequest(BaseModel):
    """Top-level request wrapper for POST /results.
    
    Attributes:
        Required:
            - result (TimebackCreateResultBody): Result data to create. See TimebackCreateResultBody for structure.
    """
    
    result: TimebackCreateResultBody

