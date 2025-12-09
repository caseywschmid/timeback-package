"""Response model for getting subject progress.

GET /powerpath/placement/getSubjectProgress
"""

from typing import List
from pydantic import BaseModel, Field

from timeback.models.timeback_subject_progress import TimebackSubjectProgressItem


class TimebackGetSubjectProgressResponse(BaseModel):
    """Response model for getting subject progress.
    
    Returns the progress the student has made in each of the subject's courses.
    
    Attributes:
        - progress (List[TimebackSubjectProgressItem]): List of progress items,
          one for each course in the subject. See TimebackSubjectProgressItem for structure.
    """

    progress: List[TimebackSubjectProgressItem] = Field(
        ..., description="The progress of the student in each of the subject's courses"
    )

