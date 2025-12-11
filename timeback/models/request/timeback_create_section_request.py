"""Request model for creating a section within a test part.

POST /assessment-tests/{assessmentTestIdentifier}/test-parts/{testPartIdentifier}/sections

Used by:
- timeback/services/qti/endpoints/create_section.py
"""

from typing import Optional, List
from pydantic import BaseModel, Field, ConfigDict
from timeback.models.timeback_qti_item_ref import TimebackQTIItemRef


class TimebackCreateSectionRequest(BaseModel):
    """Request model for creating a section within a test part.
    
    Sections organize assessment items and define their presentation behavior.
    
    Attributes:
        Required:
            - identifier (str): Unique identifier for the section
            - title (str): Human-readable title
        
        Optional:
            - visible (bool, optional): Whether section is visible to candidates (default: True)
            - required (bool, optional): Whether section is required (default: True)
            - fixed (bool, optional): Whether section position is fixed (default: False)
            - sequence (int, optional): Order within parent
            - qti_assessment_item_ref (list, optional): List of item references
    
    Example:
        request = TimebackCreateSectionRequest(
            identifier="section-001",
            title="Introduction",
            visible=True,
            qti_assessment_item_ref=[
                TimebackQTIItemRef(identifier="item-001", href="/assessment-items/item-001")
            ]
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

