"""Request model for resetting user placement.

POST /powerpath/placement/resetUserPlacement
"""

from pydantic import BaseModel, Field

from timeback.enums import TimebackSubject


class TimebackResetUserPlacementRequest(BaseModel):
    """Request model for resetting user placement for a subject.
    
    Resets a user's placement progress for a specific subject by:
    - Soft deleting all placement assessment results for that subject
    - Resetting user onboarding state to "in_progress"
    
    This operation is restricted to administrators only and cannot be undone.
    
    Attributes:
        Required:
            - student (str): The sourcedId of the student
            - subject (TimebackSubject): The subject to reset. See TimebackSubject enum.
    """

    student: str = Field(..., description="The sourcedId of the student")
    subject: TimebackSubject = Field(..., description="The subject to reset")

