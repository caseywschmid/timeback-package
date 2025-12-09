"""Request model for getting current level.

GET /powerpath/placement/getCurrentLevel
"""

from pydantic import BaseModel, Field

from timeback.enums import TimebackSubject


class TimebackGetCurrentLevelRequest(BaseModel):
    """Request model for getting the current level of a student in a placement process.
    
    Returns the current level of the student determined by the last completed 
    placement test's grade level, starting from the lowest grade level available 
    for the subject's placement tests.
    
    Attributes:
        Required:
            - student (str): The sourcedId of the student
            - subject (TimebackSubject): The subject name. See TimebackSubject enum for valid values.
    """

    student: str = Field(..., description="The sourcedId of the student")
    subject: TimebackSubject = Field(..., description="The subject name")

