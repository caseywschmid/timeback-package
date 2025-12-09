"""Request model for updating/creating an assessment result.

PUT /ims/oneroster/gradebook/v1p2/assessmentResults/{sourcedId}
"""

from typing import Any, Dict, Optional, List
from pydantic import BaseModel, Field, ConfigDict
from timeback.enums import TimebackStatus, TimebackScoreStatus
from timeback.models.timeback_assessment_line_item_ref import TimebackAssessmentLineItemRef
from timeback.models.timeback_student_ref import TimebackStudentRef
from timeback.models.timeback_score_scale_ref import TimebackScoreScaleRef
from timeback.models.timeback_learning_objective_set import TimebackLearningObjectiveSet


class TimebackPutAssessmentResultBody(BaseModel):
    """Body payload for assessment result update/create under the top-level 'assessmentResult' key.
    
    Attributes:
        Required:
            - assessmentLineItem (TimebackAssessmentLineItemRef): Reference to the assessment line item
            - student (TimebackStudentRef): Reference to the student
            - scoreStatus (TimebackScoreStatus): Status of the score
            - scoreDate (str): Date when the score was recorded (ISO 8601 format)
        
        Optional:
            - sourcedId (str, optional): The sourcedId (should match path parameter)
            - status (TimebackStatus, optional): Result status. Defaults to "active"
            - metadata (Dict[str, Any], optional): Custom metadata
            - scoreScale (TimebackScoreScaleRef, optional): Reference to score scale
            - score (float, optional): Numeric score value
            - textScore (str, optional): Text representation of the score
            - scorePercentile (float, optional): Percentile rank of the score
            - comment (str, optional): Comment about the result
            - learningObjectiveSet (List[TimebackLearningObjectiveSet], optional): Learning objective results
            - inProgress, incomplete, late, missing (str, optional): Status indicators
    """
    
    model_config = ConfigDict(populate_by_name=True)
    
    # Optional sourcedId; should match path parameter if provided
    sourcedId: Optional[str] = Field(None, description="Unique identifier (should match path parameter)")
    
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


class TimebackPutAssessmentResultRequest(BaseModel):
    """Request model for PUT /assessmentResults/{sourcedId}.
    
    Attributes:
        Required:
            - sourced_id (str): The sourcedId of the assessment result (path parameter)
            - assessmentResult (TimebackPutAssessmentResultBody): Assessment result data to update/create
    """
    
    model_config = ConfigDict(populate_by_name=True)
    
    sourced_id: str = Field(..., description="The sourcedId of the assessment result (path parameter)")
    assessmentResult: TimebackPutAssessmentResultBody = Field(..., description="Assessment result data to update/create")

