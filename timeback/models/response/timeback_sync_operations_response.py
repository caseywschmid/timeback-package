"""Response model for sync operations and recreate lesson plan endpoints.

POST /powerpath/lessonPlans/{lessonPlanId}/operations/sync
POST /powerpath/lessonPlans/{lessonPlanId}/recreate

These endpoints share the same response structure.
"""

from typing import List, Optional
from pydantic import BaseModel, Field


class TimebackOperationError(BaseModel):
    """An error that occurred during an operation.
    
    Attributes:
        - message (str): Description of the error
    """

    message: str = Field(..., description="Error message")


class TimebackOperationResult(BaseModel):
    """Result of a single operation during sync/recreate.
    
    Attributes:
        - success (bool): Whether the operation succeeded
        - errors (List[TimebackOperationError], optional): Errors if operation failed
    """

    success: bool = Field(..., description="Whether the operation succeeded")
    errors: Optional[List[TimebackOperationError]] = Field(
        None, description="Errors if operation failed"
    )


class TimebackSyncOperationsResponse(BaseModel):
    """Response model for sync operations and recreate lesson plan.
    
    Attributes:
        - success (bool): Whether the overall sync/recreate succeeded
        - message (str, optional): Additional information message
        - operationCount (int): Number of operations processed
        - operationResults (List[TimebackOperationResult]): Result of each operation
    """

    success: bool = Field(..., description="Whether the sync succeeded")
    message: Optional[str] = Field(None, description="Additional message")
    operationCount: int = Field(..., description="Number of operations processed")
    operationResults: List[TimebackOperationResult] = Field(
        ..., description="Results of each operation"
    )

