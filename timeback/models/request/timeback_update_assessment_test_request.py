"""Request model for updating a QTI assessment test.

PUT /assessment-tests/{identifier}

Used by:
- timeback/services/qti/endpoints/update_assessment_test.py
"""

from typing import Dict, Any, Optional, Literal
from pydantic import BaseModel, Field


class TimebackUpdateAssessmentTestRequest(BaseModel):
    """Request model for updating a QTI assessment test.
    
    The recommended approach is to send format='xml' with the QTI XML string.
    JSON updates are also supported.
    
    Attributes:
        Required (when using XML format):
            - format (str): Content format, either 'xml' or 'json'. XML is recommended.
            - xml (str): Updated QTI 3.0 XML content string (required when format='xml')
        
        Optional:
            - metadata (dict, optional): Updated custom metadata
    
    Example:
        request = TimebackUpdateAssessmentTestRequest(
            format="xml",
            xml='<?xml version="1.0"?><qti-assessment-test>...</qti-assessment-test>',
            metadata={"subject": "Math", "grade": "6"}
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
        description="Updated custom metadata for the assessment test"
    )

