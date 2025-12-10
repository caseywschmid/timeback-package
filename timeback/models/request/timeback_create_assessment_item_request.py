"""Request model for creating a QTI assessment item.

POST /assessment-items

Used by:
- timeback/services/qti/endpoints/create_assessment_item.py
"""

from typing import Dict, Any, Optional, Literal
from pydantic import BaseModel, Field


class TimebackCreateAssessmentItemRequest(BaseModel):
    """Request model for creating a QTI assessment item.
    
    The recommended approach is to send format='xml' with the QTI XML string.
    JSON creation is experimental and may change.
    
    Attributes:
        Required (when using XML format):
            - format (str): Content format, either 'xml' or 'json'. XML is recommended.
            - xml (str): QTI 3.0 XML content string (required when format='xml')
        
        Optional:
            - metadata (dict, optional): Custom metadata for the assessment item
              including subject, grade, difficulty, learningObjectiveSet, etc.
    
    Example XML format:
        request = TimebackCreateAssessmentItemRequest(
            format="xml",
            xml='<?xml version="1.0"?><qti-assessment-item>...</qti-assessment-item>',
            metadata={"subject": "Math", "grade": "5", "difficulty": "medium"}
        )
    """
    
    format: Literal["xml", "json"] = Field(
        default="xml",
        description="Content format. 'xml' is recommended for production use."
    )
    xml: Optional[str] = Field(
        None,
        description="QTI 3.0 XML content string. Required when format='xml'."
    )
    metadata: Optional[Dict[str, Any]] = Field(
        None,
        description="Custom metadata for the assessment item"
    )

