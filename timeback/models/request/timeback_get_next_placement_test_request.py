"""Request model for getting the next placement test.

GET /powerpath/placement/getNextPlacementTest
"""

from pydantic import BaseModel, Field

from timeback.enums import TimebackSubject


class TimebackGetNextPlacementTestRequest(BaseModel):
    """Request model for getting the next placement test for a student.
    
    Returns the next placement test the student should take based on their
    progress in the placement process for a given subject.
    
    Attributes:
        Required:
            - student (str): The sourcedId of the student
            - subject (TimebackSubject): The subject name. See TimebackSubject enum for valid values.
    """

    student: str = Field(..., description="The sourcedId of the student")
    subject: TimebackSubject = Field(..., description="The subject name")

