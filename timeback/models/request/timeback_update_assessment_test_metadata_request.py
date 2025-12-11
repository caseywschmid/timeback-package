"""Request model for updating assessment test metadata only.

PUT /assessment-tests/{identifier}/metadata

Used by:
- timeback/services/qti/endpoints/update_assessment_test_metadata.py
"""

from typing import Dict, Any
from pydantic import BaseModel, Field


class TimebackUpdateAssessmentTestMetadataRequest(BaseModel):
    """Request model for updating assessment test metadata only.
    
    This is a lightweight operation for administrative changes to
    title, description, and other metadata properties without affecting
    the test structure, test parts, sections, or assessment items.
    
    Attributes:
        Required:
            - metadata (dict): Custom metadata to update for the assessment test
    
    Example:
        request = TimebackUpdateAssessmentTestMetadataRequest(
            metadata={
                "subject": "Math",
                "grade": "5",
                "description": "Updated description"
            }
        )
    """
    
    metadata: Dict[str, Any] = Field(
        ...,
        description="Custom metadata to update for the assessment test"
    )

