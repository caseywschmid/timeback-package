"""Request model for getting test-out information.

GET /powerpath/testOut

**DEPRECATED**: This endpoint is deprecated. Use GET /powerpath/lessonPlans/getCourseProgress instead.
"""

from pydantic import BaseModel, Field


class TimebackGetTestOutRequest(BaseModel):
    """Request model for getting test-out information.
    
    **DEPRECATED**: This endpoint is deprecated and will be removed.
    Migration: Use GET /powerpath/lessonPlans/getCourseProgress/:courseId/student/:studentId instead.
    The response includes a `testOut` field with comprehensive status information.
    
    Attributes:
        Required:
            - student (str): The sourcedId of the student
            - course (str): The sourcedId of the Course to retrieve the testOut from
    """

    student: str = Field(..., description="The sourcedId of the student")
    course: str = Field(..., description="The sourcedId of the Course")

