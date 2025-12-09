"""Response model for getting course progress.

GET /powerpath/lessonPlans/getCourseProgress/{courseId}/student/{studentId}

Returns assessment line items and test-out status for a student in a course.
"""

from typing import List, Optional, Any, Dict, Literal, Union
from pydantic import BaseModel, Field


class TimebackScoreScale(BaseModel):
    """Score scale reference."""

    sourcedId: str


class TimebackLearningObjectiveResult(BaseModel):
    """Individual learning objective result."""

    learningObjectiveId: str
    score: Optional[float] = None
    textScore: Optional[str] = None


class TimebackLearningObjectiveSet(BaseModel):
    """Learning objective set with results."""

    source: str
    learningObjectiveResults: List[TimebackLearningObjectiveResult]


class TimebackAssessmentResult(BaseModel):
    """Assessment result for a line item.
    
    Attributes:
        - sourcedId (str, optional): Result ID
        - status (str): "active" or "tobedeleted"
        - dateLastModified (str, optional): Last modification timestamp
        - metadata (dict, optional): Additional metadata
        - score (float, optional): Numeric score
        - textScore (str, optional): Text-based score
        - scoreDate (str): Date when scored
        - scoreScale (dict, optional): Score scale reference
        - scorePercentile (float, optional): Percentile score
        - scoreStatus (str): Score status enum
        - comment (str, optional): Teacher/system comment
        - learningObjectiveSet (list, optional): Learning objective results
        - inProgress (str, optional): In-progress flag
        - incomplete (str, optional): Incomplete flag
        - late (str, optional): Late flag
        - missing (str, optional): Missing flag
    """

    sourcedId: Optional[str] = None
    status: str = Field(..., description="active or tobedeleted")
    dateLastModified: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    score: Optional[float] = None
    textScore: Optional[str] = None
    scoreDate: str
    scoreScale: Optional[TimebackScoreScale] = None
    scorePercentile: Optional[float] = None
    scoreStatus: str = Field(
        ..., description="exempt, fully graded, not submitted, partially graded, submitted"
    )
    comment: Optional[str] = None
    learningObjectiveSet: Optional[List[TimebackLearningObjectiveSet]] = None
    inProgress: Optional[str] = None
    incomplete: Optional[str] = None
    late: Optional[str] = None
    missing: Optional[str] = None


class TimebackComponentLineItem(BaseModel):
    """Assessment line item for a component (unit, lesson)."""

    type: Literal["component"] = "component"
    assessmentLineItemSourcedId: str
    courseComponentSourcedId: str
    title: str
    results: List[TimebackAssessmentResult]


class TimebackResourceLineItem(BaseModel):
    """Assessment line item for a resource (video, quiz, etc)."""

    type: Literal["resource"] = "resource"
    assessmentLineItemSourcedId: str
    courseComponentResourceSourcedId: str
    title: str
    results: List[TimebackAssessmentResult]


# Union type for line items
TimebackProgressLineItem = Union[TimebackComponentLineItem, TimebackResourceLineItem]


class TimebackTestOutNotEligible(BaseModel):
    """Test-out status: not eligible."""

    status: Literal["not_eligible"] = "not_eligible"


class TimebackTestOutAvailable(BaseModel):
    """Test-out status: available to take."""

    status: Literal["available"] = "available"


class TimebackTestOutInProgress(BaseModel):
    """Test-out status: in progress."""

    status: Literal["in_progress"] = "in_progress"
    assignmentId: str
    lessonId: str


class TimebackTestOutCompleted(BaseModel):
    """Test-out status: completed successfully."""

    status: Literal["completed"] = "completed"
    assignmentId: str
    lessonId: str


class TimebackTestOutFailed(BaseModel):
    """Test-out status: failed."""

    status: Literal["failed"] = "failed"
    assignmentId: str
    lessonId: str


# Union type for test-out status
TimebackTestOutStatus = Union[
    TimebackTestOutNotEligible,
    TimebackTestOutAvailable,
    TimebackTestOutInProgress,
    TimebackTestOutCompleted,
    TimebackTestOutFailed,
]


class TimebackCourseProgressResponse(BaseModel):
    """Response model for getting course progress.
    
    GET /powerpath/lessonPlans/getCourseProgress/{courseId}/student/{studentId}
    
    Attributes:
        - lineItems (list): Assessment line items (component or resource type)
        - testOut (object): Test-out status for the student
    """

    lineItems: List[Dict[str, Any]] = Field(
        ..., description="Assessment line items (component or resource)"
    )
    testOut: Dict[str, Any] = Field(..., description="Test-out status")

