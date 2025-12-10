"""Request model for updating a QTI assessment item.

PUT /assessment-items/{identifier}

Used by:
- timeback/services/qti/endpoints/update_assessment_item.py
"""

from typing import Dict, Any, Optional, Literal
from pydantic import BaseModel, Field


class TimebackUpdateAssessmentItemRequest(BaseModel):
    """Request model for updating a QTI assessment item.
    
    The recommended approach is to send format='xml' with the QTI XML string.
    JSON updates are experimental and may change.
    
    Attributes:
        Required (when using XML format):
            - format (str): Content format, either 'xml' or 'json'. XML is recommended.
            - xml (str): Updated QTI 3.0 XML content string (required when format='xml')
        
        Optional:
            - metadata (dict, optional): Updated custom metadata for the assessment item
    
    Example:
        request = TimebackUpdateAssessmentItemRequest(
            format="xml",
            xml='<?xml version="1.0"?><qti-assessment-item>...</qti-assessment-item>',
            metadata={"subject": "Math", "grade": "6", "difficulty": "hard"}
        )
    """
    
    format: Literal["xml", "json"] = Field(
        default="xml",
        description="Content format. 'xml' is recommended for production use."
    )
    xml: Optional[str] = Field(
        None,
        description="Updated QTI 3.0 XML content string. Required when format='xml'."
    )
    metadata: Optional[Dict[str, Any]] = Field(
        None,
        description="Updated custom metadata for the assessment item"
    )

