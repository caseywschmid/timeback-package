"""Request model for creating bulk test assignments.

POST /powerpath/test-assignments/bulk
"""

from typing import List, Optional
from pydantic import BaseModel, ConfigDict, Field
from timeback.enums import TimebackSubject, TimebackGrade


class TimebackBulkTestAssignmentItem(BaseModel):
    """A single item in a bulk test assignment request.
    
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


class TimebackBulkTestAssignmentsRequest(BaseModel):
    """Request model for creating multiple test assignments.
    
    All-or-nothing operation: returns 200 if all succeed,
    400 if any validation errors are found.
    
    Attributes:
        - items (list): Array of test assignments to create (min 1)
    """

    model_config = ConfigDict(populate_by_name=True)

    items: List[TimebackBulkTestAssignmentItem] = Field(
        ..., min_length=1, description="Assignments to create"
    )

