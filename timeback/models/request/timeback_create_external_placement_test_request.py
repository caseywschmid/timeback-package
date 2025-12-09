"""Request model for creating an external placement test.

POST /powerpath/createExternalPlacementTest
"""

from typing import Optional, List, Literal, Any
from pydantic import BaseModel, Field


class TimebackCreateExternalPlacementTestRequest(BaseModel):
    """Request model for creating an external placement test.
    
    Creates or updates a ComponentResource to act as a Placement Test lesson in a course.
    This allows integrating with external test-taking platforms (like Edulastic) for content delivery.
    
    The endpoint creates or updates:
    - A CourseComponent for the course to hold the Placement Test lesson
    - A Resource with lessonType = "placement" and the external service details as metadata
    - A ComponentResource acting as the Placement Test lesson
    
    Attributes:
        Required:
            - courseId (str): The sourcedId of the Course to create the external test for
            - toolProvider (str): The type of external service. Valid values: "edulastic", "mastery-track"
            - grades (List[str]): The grades for the resource. Valid values: "-1", "0", "1"..."13"
            - lessonType (Literal["placement"]): Must be "placement"
            
        Optional:
            - lessonTitle (str): The title of the external test reference
            - launchUrl (str): The URL to the external test system (e.g., Edulastic, QTI, etc.)
            - unitTitle (str): The title of the unit containing the external test
            - courseComponentSourcedId (str): The sourcedId of an existing CourseComponent (unit).
              If not provided, a new unit will be created.
            - vendorId (str): The ID of the test in the spreadsheet
            - description (str): Description of the external test for the Resource entity's metadata
            - resourceMetadata (Any): Additional metadata for the external test resource
            - courseIdOnFail (str): The courseId to enroll the student in if they fail 
              the placement test (score < 90%)
            - xp (int): The XP value for the resource
    """

    # Required fields
    courseId: str = Field(..., description="The sourcedId of the Course to create the external test for")
    toolProvider: Literal["edulastic", "mastery-track"] = Field(
        ..., description="The type of external service"
    )
    grades: List[str] = Field(..., description="The grades for the resource")
    lessonType: Literal["placement"] = Field(
        default="placement", description="Must be 'placement'"
    )

    # Optional fields
    lessonTitle: Optional[str] = Field(None, description="The title of the external test reference")
    launchUrl: Optional[str] = Field(None, description="The URL to the external test system")
    unitTitle: Optional[str] = Field(None, description="The title of the unit containing the external test")
    courseComponentSourcedId: Optional[str] = Field(
        None, description="The sourcedId of an existing CourseComponent (unit) for the test"
    )
    vendorId: Optional[str] = Field(None, description="The ID of the test in the spreadsheet")
    description: Optional[str] = Field(
        None, description="Description of the external test for the Resource metadata"
    )
    resourceMetadata: Optional[Any] = Field(
        None, description="Additional metadata for the external test resource"
    )
    courseIdOnFail: Optional[str] = Field(
        None, description="The courseId to enroll the student in if they fail (score < 90%)"
    )
    xp: Optional[int] = Field(None, description="The XP value for the resource")

