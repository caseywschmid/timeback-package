"""Request model for creating a test assignment.

POST /powerpath/test-assignments
"""

from typing import Optional
from pydantic import BaseModel, ConfigDict, Field
from timeback.enums import TimebackSubject, TimebackGrade


class TimebackCreateTestAssignmentRequest(BaseModel):
    """Request model for creating an individual test assignment.
    
    Creates a standalone test-out assignment for a student.
    
    Attributes:
        - student (str): The sourcedId of the student
        - subject (TimebackSubject): The subject (Math, Reading, etc.)
        - grade (TimebackGrade): The grade level (-1 through 13)
        - testName (str, optional): Display name for the test
    """

    model_config = ConfigDict(populate_by_name=True)

    student: str = Field(..., description="Student sourcedId")
    subject: TimebackSubject = Field(..., description="Test subject")
    grade: TimebackGrade = Field(..., description="Grade level")
    testName: Optional[str] = Field(None, description="Optional display name")

