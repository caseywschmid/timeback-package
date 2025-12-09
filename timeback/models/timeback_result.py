"""Result models for the TimeBack API.

This module defines the data models for results following the OneRoster v1.2 specification.

API Endpoints:
- GET /ims/oneroster/gradebook/v1p2/results - List results
- GET /ims/oneroster/gradebook/v1p2/results/{sourcedId} - Get a specific result
- POST /ims/oneroster/gradebook/v1p2/results - Create a new result
- PUT /ims/oneroster/gradebook/v1p2/results/{sourcedId} - Update a result
- DELETE /ims/oneroster/gradebook/v1p2/results/{sourcedId} - Delete a result
"""

from typing import Optional, Dict, Any, List
from pydantic import BaseModel, Field, ConfigDict
from timeback.enums.timeback_status import TimebackStatus
from timeback.enums.timeback_score_status import TimebackScoreStatus
from timeback.models.timeback_sourced_id_ref import TimebackSourcedIdReference
from timeback.models.timeback_learning_objective_set import TimebackLearningObjectiveSet


class TimebackResult(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    """OneRoster Result model.
    
    Required Fields:
    - status: Status of the result (active or tobedeleted)
    - lineItem: Reference to the line item
    - student: Reference to the student
    - scoreStatus: Status of the score (exempt, fully graded, not submitted, partially graded, submitted)
    - scoreDate: Date when the score was recorded
    
    Optional Fields:
    - sourcedId: Unique identifier
    - dateLastModified: Last modification timestamp
    - metadata: Custom metadata
    - class: Reference to class (nullable)
    - scoreScale: Reference to score scale (nullable)
    - score: Numeric score value (nullable)
    - textScore: Text representation of the score (nullable)
    - comment: Comment about the result (nullable)
    - learningObjectiveSet: Learning objective results (nullable)
    - inProgress: In progress indicator (string)
    - incomplete: Incomplete indicator (string)
    - late: Late indicator (string)
    - missing: Missing indicator (string)
    """
    
    # Required fields
    status: TimebackStatus = Field(..., description="Status of the result")
    lineItem: TimebackSourcedIdReference = Field(..., description="Reference to the line item")
    student: TimebackSourcedIdReference = Field(..., description="Reference to the student")
    scoreStatus: TimebackScoreStatus = Field(..., description="Status of the score")
    scoreDate: str = Field(..., description="Date when the score was recorded (ISO 8601 format)")
    
    # Optional fields
    sourcedId: Optional[str] = Field(None, description="Unique identifier")
    dateLastModified: Optional[str] = Field(None, description="Last modification timestamp")
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

