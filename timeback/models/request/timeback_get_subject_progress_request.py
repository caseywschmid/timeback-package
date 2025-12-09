"""Request model for getting subject progress.

GET /powerpath/placement/getSubjectProgress
"""

from pydantic import BaseModel, Field

from timeback.enums import TimebackSubject


class TimebackGetSubjectProgressRequest(BaseModel):
    """Request model for getting the progress a student has made in a subject.
    
    Returns the progress the student has made in each of the subject's courses,
    including completed lessons, XP earned, and test-out status.
    
    Attributes:
        Required:
            - student (str): The sourcedId of the student
            - subject (TimebackSubject): The subject name. See TimebackSubject enum for valid values.
    """

    student: str = Field(..., description="The sourcedId of the student")
    subject: TimebackSubject = Field(..., description="The subject name")

