"""Request model for partially updating an assessment result.

PATCH /ims/oneroster/gradebook/v1p2/assessmentResults/{sourcedId}
"""

from typing import Any, Dict, Optional, List
from pydantic import BaseModel, Field, ConfigDict
from timeback.enums import TimebackStatus, TimebackScoreStatus
from timeback.models.timeback_assessment_line_item_ref import TimebackAssessmentLineItemRef
from timeback.models.timeback_student_ref import TimebackStudentRef
from timeback.models.timeback_score_scale_ref import TimebackScoreScaleRef
from timeback.models.timeback_learning_objective_set import TimebackLearningObjectiveSet


class TimebackPatchAssessmentResultBody(BaseModel):
    """Body payload for partial assessment result update under 'assessmentResult' key.
    
    All fields are optional for partial updates. Only provided fields will be updated.
    Metadata merging is supported.
    """
    
    model_config = ConfigDict(populate_by_name=True)
    
    # All fields optional for partial update
    sourcedId: Optional[str] = Field(None, description="Unique identifier")
    status: Optional[TimebackStatus] = Field(None, description="Assessment result status")
    metadata: Optional[Dict[str, Any]] = Field(None, description="Custom metadata (merged with existing)")
    assessmentLineItem: Optional[TimebackAssessmentLineItemRef] = Field(None, description="Reference to assessment line item")
    student: Optional[TimebackStudentRef] = Field(None, description="Reference to student")
    scoreStatus: Optional[TimebackScoreStatus] = Field(None, description="Status of the score")
    scoreDate: Optional[str] = Field(None, description="Date when the score was recorded")
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


class TimebackPatchAssessmentResultRequest(BaseModel):
    """Request model for PATCH /assessmentResults/{sourcedId}.
    
    Attributes:
        Required:
            - sourced_id (str): The sourcedId of the assessment result (path parameter)
            - assessmentResult (TimebackPatchAssessmentResultBody): Partial assessment result data
    """
    
    model_config = ConfigDict(populate_by_name=True)
    
    sourced_id: str = Field(..., description="The sourcedId of the assessment result (path parameter)")
    assessmentResult: TimebackPatchAssessmentResultBody = Field(..., description="Partial assessment result data")

