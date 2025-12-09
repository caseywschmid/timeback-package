"""Response model for creating external tests (placement and test-out).

POST /powerpath/createExternalPlacementTest
POST /powerpath/createExternalTestOut
"""

from typing import Optional, List
from pydantic import BaseModel, Field


class TimebackCreateExternalTestResponse(BaseModel):
    """Response model for creating external tests.
    
    Shared response structure for both createExternalPlacementTest and createExternalTestOut.
    
    Attributes:
        - lessonType (str): The type of lesson created.
          Valid values: "powerpath-100", "quiz", "test-out", "placement", "unit-test", "alpha-read-article"
        - lessonId (str): The sourcedId of the created external test reference (ComponentResource)
        - courseComponentId (str): The sourcedId of the component (unit) containing the test
        - resourceId (str): The sourcedId of the resource representing the external test
        - toolProvider (str): The tool provider id
        - launchUrl (str, optional): The URL to the external test system
        - vendorId (str, optional): The ID of the test in the spreadsheet
        - courseIdOnFail (str, optional): The courseId to enroll the student in if they fail
        - grades (List[str], optional): The grades for the resource
    """

    lessonType: str = Field(..., description="The type of lesson created")
    lessonId: str = Field(
        ..., description="The sourcedId of the created external test reference (ComponentResource)"
    )
    courseComponentId: str = Field(
        ..., description="The sourcedId of the component (unit) containing the test"
    )
    resourceId: str = Field(
        ..., description="The sourcedId of the resource representing the external test"
    )
    toolProvider: str = Field(..., description="The tool provider id")
    launchUrl: Optional[str] = Field(None, description="The URL to the external test system")
    vendorId: Optional[str] = Field(None, description="The ID of the test in the spreadsheet")
    courseIdOnFail: Optional[str] = Field(
        None, description="The courseId to enroll the student in if they fail"
    )
    grades: Optional[List[str]] = Field(None, description="The grades for the resource")

