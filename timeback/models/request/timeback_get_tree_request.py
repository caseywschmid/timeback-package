"""Request model for getting a lesson plan tree.

GET /powerpath/lessonPlans/{courseId}/{userId}
"""

from pydantic import BaseModel, ConfigDict, Field


class TimebackGetTreeRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    """Request model for retrieving a lesson plan tree.
    
    Returns the complete lesson plan tree for a course and student,
    including all components, resources, and nested structure.
    
    Attributes:
        Required:
            - course_id (str): The sourcedId of the course
            - user_id (str): The sourcedId of the student
    """

    course_id: str = Field(..., alias="courseId", description="The sourcedId of the course")
    user_id: str = Field(..., alias="userId", description="The sourcedId of the student")

