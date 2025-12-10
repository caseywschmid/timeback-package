"""Request model for creating a QTI assessment test.

POST /assessment-tests

Used by:
- timeback/services/qti/endpoints/create_assessment_test.py
"""

from typing import Dict, Any, Optional, Literal
from pydantic import BaseModel, Field


class TimebackCreateAssessmentTestRequest(BaseModel):
    """Request model for creating a QTI assessment test.
    
    The recommended approach is to send format='xml' with the QTI XML string.
    JSON creation is also supported.
    
    Attributes:
        Required (when using XML format):
            - format (str): Content format, either 'xml' or 'json'. XML is recommended.
            - xml (str): QTI 3.0 XML content string (required when format='xml')
        
        Optional:
            - metadata (dict, optional): Custom metadata for the assessment test
    
    Example XML format:
        request = TimebackCreateAssessmentTestRequest(
            format="xml",
            xml='<?xml version="1.0"?><qti-assessment-test>...</qti-assessment-test>',
            metadata={"subject": "Math", "grade": "5"}
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
        description="Custom metadata for the assessment test"
    )

