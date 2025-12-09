"""Response model for getting lesson plan operations.

GET /powerpath/lessonPlans/{lessonPlanId}/operations
"""

from typing import List, Optional, Any, Dict
from pydantic import BaseModel, Field


class TimebackLessonPlanOperation(BaseModel):
    """A single operation in a lesson plan's operation log.
    
    Attributes:
        - id (str): Unique identifier for the operation
        - type (str): Operation type (set-skipped, move-item-before, etc.)
        - payload (dict, optional): Operation-specific payload data
        - reason (str, optional): Reason for the operation
        - createdAt (str): Timestamp when the operation was created
        - sequenceNumber (int): Order number of the operation
        - createdBy (str, optional): User who created the operation
    """

    id: str = Field(..., description="Unique identifier for the operation")
    type: str = Field(..., description="Operation type")
    payload: Optional[Dict[str, Any]] = Field(None, description="Operation-specific payload")
    reason: Optional[str] = Field(None, description="Reason for the operation")
    createdAt: str = Field(..., description="Timestamp when created")
    sequenceNumber: int = Field(..., description="Order number of the operation")
    createdBy: Optional[str] = Field(None, description="User who created the operation")


class TimebackGetOperationsResponse(BaseModel):
    """Response model for getting lesson plan operations.
    
    Attributes:
        - operations (List[TimebackLessonPlanOperation]): List of operations
          in chronological order. See TimebackLessonPlanOperation for structure.
    """

    operations: List[TimebackLessonPlanOperation] = Field(
        ..., description="List of operations"
    )

