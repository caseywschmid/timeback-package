"""Request model for getting all placement tests.

GET /powerpath/placement/getAllPlacementTests
"""

from pydantic import BaseModel, Field

from timeback.enums import TimebackSubject


class TimebackGetAllPlacementTestsRequest(BaseModel):
    """Request model for getting all placement tests for a student and subject.
    
    This endpoint returns all placement tests for a subject, including available
    results for each. A 'Lesson' (placement test) in this context is a 
    ComponentResource object which has a Resource object with 
    metadata.lessonType = "placement" associated with it.
    
    Attributes:
        Required:
            - student (str): The sourcedId of the student
            - subject (TimebackSubject): The subject name. See TimebackSubject enum for valid values.
    """

    student: str = Field(..., description="The sourcedId of the student")
    subject: TimebackSubject = Field(..., description="The subject name")

