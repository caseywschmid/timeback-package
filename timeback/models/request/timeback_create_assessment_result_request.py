"""Request model for creating a OneRoster Assessment Result.

POST /ims/oneroster/gradebook/v1p2/assessmentResults

The request body must include an assessmentResult object with required fields:
assessmentLineItem (with sourcedId), student (with sourcedId), scoreStatus, and scoreDate.
"""

from typing import Any, Dict, Optional, List
from pydantic import BaseModel, Field, ConfigDict
from uuid import uuid4
from timeback.enums import TimebackStatus, TimebackScoreStatus
from timeback.models.timeback_assessment_line_item_ref import TimebackAssessmentLineItemRef
from timeback.models.timeback_student_ref import TimebackStudentRef
from timeback.models.timeback_score_scale_ref import TimebackScoreScaleRef
from timeback.models.timeback_learning_objective_set import TimebackLearningObjectiveSet


class TimebackCreateAssessmentResultBody(BaseModel):
    """Body payload for assessment result creation under the top-level 'assessmentResult' key.
    
    Attributes:
        Required:
            - assessmentLineItem (TimebackAssessmentLineItemRef): Reference to the assessment line item. See TimebackAssessmentLineItemRef for structure.
            - student (TimebackStudentRef): Reference to the student. See TimebackStudentRef for structure.
            - scoreStatus (TimebackScoreStatus): Status of the score. See TimebackScoreStatus enum.
            - scoreDate (str): Date when the score was recorded (ISO 8601 format)
        
        Optional:
            - sourcedId (str, optional): Client-supplied sourcedId (auto-generated UUID if omitted)
            - status (TimebackStatus, optional): Result status. Defaults to "active". See TimebackStatus enum.
            - metadata (Dict[str, Any], optional): Custom metadata
            - scoreScale (TimebackScoreScaleRef, optional): Reference to score scale
            - score (float, optional): Numeric score value
            - textScore (str, optional): Text representation of the score
            - scorePercentile (float, optional): Percentile rank of the score
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
    assessmentLineItem: TimebackAssessmentLineItemRef = Field(..., description="Reference to the assessment line item")
    student: TimebackStudentRef = Field(..., description="Reference to the student")
    scoreStatus: TimebackScoreStatus = Field(..., description="Status of the score")
    scoreDate: str = Field(..., description="Date when the score was recorded (ISO 8601 format)")
    
    # Optional fields
    status: Optional[TimebackStatus] = Field(default=TimebackStatus.ACTIVE, description="Assessment result status")
    metadata: Optional[Dict[str, Any]] = Field(None, description="Custom metadata")
    scoreScale: Optional[TimebackScoreScaleRef] = Field(None, description="Reference to score scale")
    score: Optional[float] = Field(None, description="Numeric score value")
    textScore: Optional[str] = Field(None, description="Text representation of the score")
    scorePercentile: Optional[float] = Field(None, description="Percentile rank of the score")
    comment: Optional[str] = Field(None, description="Comment about the assessment result")
    learningObjectiveSet: Optional[List[TimebackLearningObjectiveSet]] = Field(None, description="Learning objective results")
    inProgress: Optional[str] = Field(None, description="In progress indicator")
    incomplete: Optional[str] = Field(None, description="Incomplete indicator")
    late: Optional[str] = Field(None, description="Late indicator")
    missing: Optional[str] = Field(None, description="Missing indicator")


class TimebackCreateAssessmentResultRequest(BaseModel):
    """Top-level request wrapper for POST /assessmentResults.
    
    Attributes:
        Required:
            - assessmentResult (TimebackCreateAssessmentResultBody): Assessment result data to create. See TimebackCreateAssessmentResultBody for structure.
    """
    
    assessmentResult: TimebackCreateAssessmentResultBody

