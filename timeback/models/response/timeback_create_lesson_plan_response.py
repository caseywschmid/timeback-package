"""Response model for creating a lesson plan.

POST /powerpath/lessonPlans/
"""

from pydantic import BaseModel, Field


class TimebackCreateLessonPlanResponse(BaseModel):
    """Response model for creating a lesson plan.
    
    Returns 200 if the lesson plan already exists, 201 if newly created.
    Both cases return the same response structure.
    
    Attributes:
        - lessonPlanId (str): The ID of the created or existing lesson plan
    """

    lessonPlanId: str = Field(..., description="The ID of the lesson plan")

