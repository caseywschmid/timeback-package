"""Response model for resetting user placement.

POST /powerpath/placement/resetUserPlacement
"""

from pydantic import BaseModel, Field


class TimebackResetUserPlacementResponse(BaseModel):
    """Response model for resetting user placement.
    
    Attributes:
        - success (bool): Whether the reset operation was successful
        - placementResultsDeleted (int): Number of placement results soft-deleted
        - onboardingReset (bool): Whether onboarding state was reset
    """

    success: bool = Field(..., description="Whether the reset operation was successful")
    placementResultsDeleted: int = Field(
        ..., description="Number of placement results soft-deleted"
    )
    onboardingReset: bool = Field(..., description="Whether onboarding state was reset")

