"""Response model for syncing all lesson plans for a course.

POST /powerpath/lessonPlans/course/{courseId}/sync
"""

from typing import List
from pydantic import BaseModel, Field


class TimebackSyncCourseLessonPlansResponse(BaseModel):
    """Response model for bulk syncing all lesson plans for a course.
    
    Attributes:
        - lessonPlansAffected (List[str]): IDs of lesson plans that were synced
    """

    lessonPlansAffected: List[str] = Field(
        ..., description="IDs of lesson plans that were synced"
    )

