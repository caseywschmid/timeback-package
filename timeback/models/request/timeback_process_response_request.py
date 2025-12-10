"""Request model for processing a response to an assessment item.

POST /assessment-items/{identifier}/process-response

Used by:
- timeback/services/qti/endpoints/process_response.py
"""

from typing import Union, List
from pydantic import BaseModel, Field


class TimebackProcessResponseRequest(BaseModel):
    """Request model for processing a response to an assessment item.
    
    This endpoint validates a candidate's response and returns the score
    and feedback based on the item's response processing rules.
    
    Attributes:
        Required:
            - identifier (str): Unique identifier of the assessment item
            - response (str | list): The candidate's response. Can be:
              - A string for single-value responses (choice, text-entry)
              - A list of strings for multiple-value responses (multi-select)
    
    Example:
        # Single choice response
        request = TimebackProcessResponseRequest(
            identifier="item-001",
            response="B"
        )
        
        # Multiple choice response
        request = TimebackProcessResponseRequest(
            identifier="item-001",
            response=["A", "C"]
        )
    """
    
    identifier: str = Field(
        ...,
        description="Unique identifier of the assessment item"
    )
    response: Union[str, List[str]] = Field(
        ...,
        description="The candidate's response (string or list of strings)"
    )

