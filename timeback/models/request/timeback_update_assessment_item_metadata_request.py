"""Request model for batch updating assessment item metadata.

POST /assessment-items/metadata

Used by:
- timeback/services/qti/endpoints/update_metadata.py
"""

from typing import Dict, Any, Optional, Literal
from pydantic import BaseModel, Field


class TimebackUpdateAssessmentItemMetadataRequest(BaseModel):
    """Request model for batch updating assessment item metadata.
    
    This operation is used to update metadata for assessment items,
    such as resetting the human approved status.
    
    Attributes:
        Required (when using XML format):
            - format (str): Content format, either 'xml' or 'json'. XML is recommended.
            - xml (str): QTI 3.0 XML content string (required when format='xml')
        
        Optional:
            - metadata (dict, optional): Metadata to update for the assessment item
              Common fields: subject, grade, difficulty, learningObjectiveSet
    
    Example:
        request = TimebackUpdateAssessmentItemMetadataRequest(
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
        description="Metadata to update for the assessment item"
    )

