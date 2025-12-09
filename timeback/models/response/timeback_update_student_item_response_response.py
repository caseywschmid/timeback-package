"""Response model for updating student item response.

POST /powerpath/lessonPlans/updateStudentItemResponse
"""

from typing import Optional, Any, Dict
from pydantic import BaseModel, Field


class TimebackUpdateStudentItemResponseResponse(BaseModel):
    """Response model for updating student item response.
    
    POST /powerpath/lessonPlans/updateStudentItemResponse
    
    Returns the created/updated line item and result.
    
    Attributes:
        - componentResourceLineItem (dict, optional): The assessment line item
        - componentResourceResult (dict, optional): The assessment result
    """

    componentResourceLineItem: Optional[Dict[str, Any]] = Field(
        None, description="The assessment line item"
    )
    componentResourceResult: Optional[Dict[str, Any]] = Field(
        None, description="The assessment result"
    )

