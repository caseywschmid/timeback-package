"""Request model for updating student item response.

POST /powerpath/lessonPlans/updateStudentItemResponse
"""

from typing import Optional, List, Dict, Any
from pydantic import BaseModel, ConfigDict, Field


class TimebackLearningObjectiveResultInput(BaseModel):
    """Learning objective result for input."""

    learningObjectiveId: str
    score: Optional[float] = None
    textScore: Optional[str] = None


class TimebackLearningObjectiveSetInput(BaseModel):
    """Learning objective set for input."""

    source: str
    learningObjectiveResults: List[TimebackLearningObjectiveResultInput]


class TimebackStudentItemResult(BaseModel):
    """The student's result for a component or resource.
    
    Attributes:
        Required:
            - status (str): "active" or "tobedeleted"
            - scoreDate (str): ISO date-time when scored
            - scoreStatus (str): One of: exempt, fully graded, not submitted,
              partially graded, submitted
        
        Optional:
            - metadata (dict): Additional metadata
            - score (float): Numeric score
            - textScore (str): Text-based score
            - scorePercentile (float): Percentile score
            - comment (str): Teacher/system comment
            - learningObjectiveSet (list): Learning objective results
            - inProgress (str): In-progress indicator
            - incomplete (str): Incomplete indicator
            - late (str): Late indicator
            - missing (str): Missing indicator
    """

    model_config = ConfigDict(populate_by_name=True)

    status: str = Field(..., description="active or tobedeleted")
    scoreDate: str = Field(..., description="ISO date-time when scored")
    scoreStatus: str = Field(
        ..., description="exempt, fully graded, not submitted, partially graded, submitted"
    )
    metadata: Optional[Dict[str, Any]] = None
    score: Optional[float] = None
    textScore: Optional[str] = None
    scorePercentile: Optional[float] = None
    comment: Optional[str] = None
    learningObjectiveSet: Optional[List[TimebackLearningObjectiveSetInput]] = None
    inProgress: Optional[str] = None
    incomplete: Optional[str] = None
    late: Optional[str] = None
    missing: Optional[str] = None


class TimebackUpdateStudentItemResponseRequest(BaseModel):
    """Request model for updating student item response.
    
    POST /powerpath/lessonPlans/updateStudentItemResponse
    
    Updates the student's response for a component or resource.
    
    Attributes:
        Required:
            - student_id (str): The sourcedId of the student
            - component_resource_id (str): The ID of the component or resource
            - result (TimebackStudentItemResult): The student's result data
    """

    model_config = ConfigDict(populate_by_name=True)

    student_id: str = Field(..., alias="studentId", description="Student sourcedId")
    component_resource_id: str = Field(
        ..., alias="componentResourceId", description="Component or resource ID"
    )
    result: TimebackStudentItemResult = Field(..., description="Student's result")

