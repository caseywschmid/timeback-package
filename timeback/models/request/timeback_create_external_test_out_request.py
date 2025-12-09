"""Request model for creating an external test-out.

POST /powerpath/createExternalTestOut

**DEPRECATED**: This endpoint is deprecated. Use POST /powerpath/lessonPlans/startTestOut instead.
See documentation for the new migration flow.
"""

from typing import Optional, List, Literal, Any
from pydantic import BaseModel, Field
import warnings


class TimebackCreateExternalTestOutRequest(BaseModel):
    """Request model for creating an external test-out lesson.
    
    **DEPRECATED**: This endpoint is deprecated and will be removed in a future version.
    Migration: Test-outs are now created on-demand using POST /powerpath/lessonPlans/startTestOut.
    
    New Flow:
    1. Check test-out availability: GET /powerpath/lessonPlans/getCourseProgress/:courseId/student/:studentId
    2. Start test-out: POST /powerpath/lessonPlans/startTestOut with { courseId, studentId }
    3. Launch external test: POST /powerpath/makeExternalTestAssignment (unchanged)
    
    Creates or updates a ComponentResource to act as a TestOut lesson in a course.
    This allows integrating with external test-taking platforms (like Edulastic).
    
    Attributes:
        Required:
            - courseId (str): The sourcedId of the Course to create the external test for
            - toolProvider (str): The type of external service. Valid values: "edulastic", "mastery-track"
            - grades (List[str]): The grades for the resource. Valid values: "-1", "0", "1"..."13"
            - lessonType (Literal["test-out"]): Must be "test-out"
            - xp (int): The XP value for the resource (required for test-out)
            
        Optional:
            - lessonTitle (str): The title of the external test reference
            - launchUrl (str): The URL to the external test system
            - unitTitle (str): The title of the unit containing the external test
            - courseComponentSourcedId (str): The sourcedId of an existing CourseComponent (unit)
            - vendorId (str): The ID of the test in the spreadsheet
            - description (str): Description of the external test for the Resource metadata
            - resourceMetadata (Any): Additional metadata for the external test resource
    """

    # Required fields
    courseId: str = Field(..., description="The sourcedId of the Course to create the external test for")
    toolProvider: Literal["edulastic", "mastery-track"] = Field(
        ..., description="The type of external service"
    )
    grades: List[str] = Field(..., description="The grades for the resource")
    lessonType: Literal["test-out"] = Field(
        default="test-out", description="Must be 'test-out'"
    )
    xp: int = Field(..., description="The XP value for the resource (required for test-out)")

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

