"""Request models for creating an internal test.

POST /powerpath/createInternalTest

Supports two test types:
- QTI: Creates a single QTI resource
- Assessment Bank: Creates multiple QTI resources wrapped in an assessment bank
"""

from typing import Optional, List, Literal, Any, Dict, Union
from pydantic import BaseModel, Field


class TimebackQtiTestConfig(BaseModel):
    """Configuration for a single QTI test.
    
    Attributes:
        - url (str): The URL to the QTI test XML file (required)
        - title (str, optional): Title for the QTI test
        - metadata (dict, optional): Additional metadata for the QTI resource
    """

    url: str = Field(..., description="The URL to the QTI test XML file")
    title: Optional[str] = Field(None, description="Title for the QTI test")
    metadata: Optional[Dict[str, Any]] = Field(None, description="Additional metadata for the QTI resource")


class TimebackAssessmentBankResource(BaseModel):
    """A single resource within an assessment bank.
    
    Attributes:
        - url (str): The URL to the QTI test XML file (required)
        - title (str, optional): Title for this assessment bank resource
        - metadata (dict, optional): Additional metadata for the QTI resource
    """

    url: str = Field(..., description="The URL to the QTI test XML file")
    title: Optional[str] = Field(None, description="Title for this assessment bank resource")
    metadata: Optional[Dict[str, Any]] = Field(None, description="Additional metadata for the QTI resource")


class TimebackAssessmentBankConfig(BaseModel):
    """Configuration for an assessment bank test.
    
    Attributes:
        - resources (List[TimebackAssessmentBankResource]): Array of QTI resources 
          that will make up the assessment bank (at least 1 required)
    """

    resources: List[TimebackAssessmentBankResource] = Field(
        ..., min_length=1, description="Array of QTI resources for the assessment bank"
    )


class TimebackCreateInternalQtiTestRequest(BaseModel):
    """Request model for creating an internal QTI test.
    
    Creates a single QTI resource as an internal test lesson in a course.
    
    Attributes:
        Required:
            - courseId (str): The sourcedId of the Course
            - lessonType (str): The type of lesson. Valid values: "powerpath-100", "quiz", 
              "test-out", "placement", "unit-test", "alpha-read-article"
            - testType (Literal["qti"]): Must be "qti"
            - qti (TimebackQtiTestConfig): QTI configuration with url (required), title, metadata
            
        Optional:
            - lessonTitle (str): Title for the lesson (ComponentResource)
            - unitTitle (str): Title for the unit (CourseComponent)
            - courseComponentSourcedId (str): Reuse an existing CourseComponent
            - resourceMetadata (Any): Additional metadata for the resource
            - xp (int): XP value for the resource (for test-out lessons)
            - grades (List[str]): Grades for the resource (for placement tests)
            - courseIdOnFail (str): Course to enroll on failure (for placement tests)
    """

    # Required fields
    courseId: str = Field(..., description="The sourcedId of the Course")
    lessonType: Literal["powerpath-100", "quiz", "test-out", "placement", "unit-test", "alpha-read-article"] = Field(
        ..., description="The type of lesson to create"
    )
    testType: Literal["qti"] = Field(default="qti", description="Must be 'qti'")
    qti: TimebackQtiTestConfig = Field(..., description="QTI configuration")

    # Optional fields
    lessonTitle: Optional[str] = Field(None, description="Title for the lesson")
    unitTitle: Optional[str] = Field(None, description="Title for the unit")
    courseComponentSourcedId: Optional[str] = Field(None, description="Reuse existing CourseComponent")
    resourceMetadata: Optional[Any] = Field(None, description="Additional metadata")
    xp: Optional[int] = Field(None, description="XP value for test-out lessons")
    grades: Optional[List[str]] = Field(None, description="Grades for placement tests")
    courseIdOnFail: Optional[str] = Field(None, description="Course to enroll on failure")


class TimebackCreateInternalAssessmentBankTestRequest(BaseModel):
    """Request model for creating an internal assessment bank test.
    
    Creates multiple QTI resources wrapped in an assessment bank as an internal test lesson.
    
    Attributes:
        Required:
            - courseId (str): The sourcedId of the Course
            - lessonType (str): The type of lesson. Valid values: "powerpath-100", "quiz", 
              "test-out", "placement", "unit-test", "alpha-read-article"
            - testType (Literal["assessment-bank"]): Must be "assessment-bank"
            - assessmentBank (TimebackAssessmentBankConfig): Assessment bank configuration with resources
            
        Optional:
            - lessonTitle (str): Title for the lesson (ComponentResource)
            - unitTitle (str): Title for the unit (CourseComponent)
            - courseComponentSourcedId (str): Reuse an existing CourseComponent
            - resourceMetadata (Any): Additional metadata for the resource
            - xp (int): XP value for the resource (for test-out lessons)
            - grades (List[str]): Grades for the resource (for placement tests)
            - courseIdOnFail (str): Course to enroll on failure (for placement tests)
    """

    # Required fields
    courseId: str = Field(..., description="The sourcedId of the Course")
    lessonType: Literal["powerpath-100", "quiz", "test-out", "placement", "unit-test", "alpha-read-article"] = Field(
        ..., description="The type of lesson to create"
    )
    testType: Literal["assessment-bank"] = Field(default="assessment-bank", description="Must be 'assessment-bank'")
    assessmentBank: TimebackAssessmentBankConfig = Field(..., description="Assessment bank configuration")

    # Optional fields
    lessonTitle: Optional[str] = Field(None, description="Title for the lesson")
    unitTitle: Optional[str] = Field(None, description="Title for the unit")
    courseComponentSourcedId: Optional[str] = Field(None, description="Reuse existing CourseComponent")
    resourceMetadata: Optional[Any] = Field(None, description="Additional metadata")
    xp: Optional[int] = Field(None, description="XP value for test-out lessons")
    grades: Optional[List[str]] = Field(None, description="Grades for placement tests")
    courseIdOnFail: Optional[str] = Field(None, description="Course to enroll on failure")


# Union type for convenience
TimebackCreateInternalTestRequest = Union[
    TimebackCreateInternalQtiTestRequest,
    TimebackCreateInternalAssessmentBankTestRequest,
]

