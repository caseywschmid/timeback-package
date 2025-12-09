"""Request model for storing a lesson plan operation.

POST /powerpath/lessonPlans/{lessonPlanId}/operations
"""

from typing import Optional, Dict, Any
from pydantic import BaseModel, ConfigDict, Field


class TimebackStoreOperationRequest(BaseModel):
    """Request model for storing an operation on a lesson plan.
    
    Operations allow customization of the learning path. Available types:
    - set-skipped: Show/hide content for the student
    - move-item-before/after: Reorder content relative to other items
    - move-item-to-start/end: Move to beginning/end of parent
    - add-custom-resource: Add additional resources
    - change-item-parent: Move content to different sections
    
    Attributes:
        Required:
            - lesson_plan_id (str): The ID of the lesson plan (path parameter)
            - operation (dict): The operation to perform. Must include:
              - type (str): One of the operation types above
              - payload (dict): Operation-specific payload
        
        Optional:
            - reason (str, optional): Reason for the operation
    
    Example operation for set-skipped:
        {
            "type": "set-skipped",
            "payload": {
                "target": {"type": "component", "id": "comp-123"},
                "value": true
            }
        }
    """

    model_config = ConfigDict(populate_by_name=True)

    lesson_plan_id: str = Field(
        ..., alias="lessonPlanId", description="The ID of the lesson plan"
    )
    operation: Dict[str, Any] = Field(
        ..., description="The operation to perform (type + payload)"
    )
    reason: Optional[str] = Field(None, description="Reason for the operation")

