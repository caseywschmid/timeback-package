"""Response model for storing a lesson plan operation.

POST /powerpath/lessonPlans/{lessonPlanId}/operations
"""

from typing import Optional
from pydantic import BaseModel, Field


class TimebackStoreOperationResponse(BaseModel):
    """Response model for storing a lesson plan operation.
    
    Attributes:
        - success (bool): Whether the operation was stored successfully
        - message (str, optional): Additional message about the operation
        - operationId (str, optional): The ID of the created operation
    """

    success: bool = Field(..., description="Whether the operation was successful")
    message: Optional[str] = Field(None, description="Additional message")
    operationId: Optional[str] = Field(None, description="ID of the created operation")

