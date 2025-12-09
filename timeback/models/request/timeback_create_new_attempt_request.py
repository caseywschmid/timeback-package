"""Request model for creating a new attempt.

POST /powerpath/createNewAttempt
"""

from pydantic import BaseModel, ConfigDict, Field


class TimebackCreateNewAttemptRequest(BaseModel):
    """Request model for creating a new attempt.
    
    Creates a new attempt for a student in a lesson if the current
    attempt is completed.
    
    For Assessment Bank lessons, this also updates the state for the
    student, associating the new attempt number with a different
    sub-resource using round-robin logic.
    
    Attributes:
        - student (str): The sourcedId of the student
        - lesson (str): The sourcedId of the lesson (ComponentResource)
    """

    model_config = ConfigDict(populate_by_name=True)

    student: str = Field(..., description="Student sourcedId")
    lesson: str = Field(..., description="Lesson (ComponentResource) sourcedId")

