"""Response model for creating internal tests.

POST /powerpath/createInternalTest
"""

from typing import Optional, List
from pydantic import BaseModel, Field


class TimebackCreateInternalTestResponse(BaseModel):
    """Response model for creating internal tests.
    
    Attributes:
        - lessonType (str): The type of lesson created.
          Valid values: "powerpath-100", "quiz", "test-out", "placement", "unit-test", "alpha-read-article"
        - testType (str): The type of test. Valid values: "qti", "assessment-bank"
        - lessonId (str): The sourcedId of the created internal test lesson (ComponentResource)
        - courseComponentId (str): The sourcedId of the component (unit) containing the test
        - resourceId (str): The sourcedId of the main resource (parent for assessment-bank)
        - childResourceIds (List[str], optional): Array of child resource IDs (only for assessment-bank type)
        - courseIdOnFail (str, optional): The courseId to enroll on failure (for placement tests)
        - grades (List[str], optional): The grades for the resource (for placement tests)
    """

    lessonType: str = Field(..., description="The type of lesson created")
    testType: str = Field(..., description="The type of test: 'qti' or 'assessment-bank'")
    lessonId: str = Field(
        ..., description="The sourcedId of the created internal test lesson (ComponentResource)"
    )
    courseComponentId: str = Field(
        ..., description="The sourcedId of the component (unit) containing the test"
    )
    resourceId: str = Field(
        ..., description="The sourcedId of the main resource (parent for assessment-bank)"
    )
    childResourceIds: Optional[List[str]] = Field(
        None, description="Array of child resource IDs (only for assessment-bank type)"
    )
    courseIdOnFail: Optional[str] = Field(
        None, description="The courseId to enroll on failure (for placement tests)"
    )
    grades: Optional[List[str]] = Field(
        None, description="The grades for the resource (for placement tests)"
    )

