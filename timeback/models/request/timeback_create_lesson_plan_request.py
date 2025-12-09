"""Request model for creating a lesson plan.

POST /powerpath/lessonPlans/
"""

from typing import Optional
from pydantic import BaseModel, ConfigDict, Field


class TimebackCreateLessonPlanRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    """Request model for creating a new lesson plan.
    
    Creates a new lesson plan for a course and student. Used for:
    - Initial setup when a new student is enrolled in a course
    - Creating a student's learning path from scratch
    
    If the lesson plan already exists, returns the existing lesson plan ID.
    
    Attributes:
        Required:
            - course_id (str): The sourcedId of the course
            - user_id (str): The sourcedId of the student
        
        Optional:
            - class_id (str, optional): The sourcedId of the class.
              Defaults to current year's class for the student.
    """

    course_id: str = Field(..., alias="courseId", description="The sourcedId of the course")
    user_id: str = Field(..., alias="userId", description="The sourcedId of the student")
    class_id: Optional[str] = Field(
        None, alias="classId", description="The sourcedId of the class (optional)"
    )

