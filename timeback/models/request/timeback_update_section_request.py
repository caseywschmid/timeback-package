"""Request model for updating a section.

PUT /assessment-tests/{assessmentTestIdentifier}/test-parts/{testPartIdentifier}/sections/{identifier}

Used by:
- timeback/services/qti/endpoints/update_section.py
"""

from typing import Optional, List
from pydantic import BaseModel, Field, ConfigDict
from timeback.models.timeback_qti_item_ref import TimebackQTIItemRef


class TimebackUpdateSectionRequest(BaseModel):
    """Request model for updating a section.
    
    Updates a section including its title, visibility, and item references.
    
    Attributes:
        Required:
            - identifier (str): Unique identifier for the section
            - title (str): Human-readable title
        
        Optional:
            - visible (bool, optional): Whether section is visible to candidates
            - required (bool, optional): Whether section is required
            - fixed (bool, optional): Whether section position is fixed
            - sequence (int, optional): Order within parent
            - qti_assessment_item_ref (list, optional): List of item references
    
    Example:
        request = TimebackUpdateSectionRequest(
            identifier="section-001",
            title="Updated Section Title",
            visible=True
        )
    """
    
    model_config = ConfigDict(populate_by_name=True)
    
    identifier: str = Field(..., description="Unique identifier for the section")
    title: str = Field(..., description="Human-readable title of the section")
    visible: bool = Field(True, description="Whether section is visible to candidates")
    required: Optional[bool] = Field(None, description="Whether section is required")
    fixed: Optional[bool] = Field(None, description="Whether section position is fixed")
    sequence: Optional[int] = Field(None, description="Order within parent")
    qti_assessment_item_ref: Optional[List[TimebackQTIItemRef]] = Field(
        None,
        alias="qti-assessment-item-ref",
        description="List of item references"
    )

