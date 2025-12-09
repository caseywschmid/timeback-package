"""Request model for updating a test assignment.

PUT /powerpath/test-assignments/{id}
"""

from pydantic import BaseModel, ConfigDict, Field


class TimebackUpdateTestAssignmentRequest(BaseModel):
    """Request model for updating a test assignment.
    
    Currently only supports updating the test name.
    
    Attributes:
        - testName (str): New display name for the test
    """

    model_config = ConfigDict(populate_by_name=True)

    testName: str = Field(..., min_length=1, description="Test display name")

