"""Response model for getting a test part.

GET /assessment-tests/{assessmentTestIdentifier}/test-parts/{identifier}

Used by:
- timeback/services/qti/endpoints/get_test_part.py
"""

from typing import Optional, Dict, Any
from pydantic import Field, ConfigDict
from timeback.models.timeback_qti_test_part import TimebackQTITestPart


class TimebackGetTestPartResponse(TimebackQTITestPart):
    """Response model for getting a test part.
    
    Inherits all fields from TimebackQTITestPart and adds:
        - raw_xml (str, optional): Raw XML representation
        - content (dict, optional): Parsed content structure
    """
    
    model_config = ConfigDict(populate_by_name=True)
    
    raw_xml: Optional[str] = Field(
        None,
        alias="rawXml",
        description="Raw XML representation of the test part"
    )
    content: Optional[Dict[str, Any]] = Field(
        None,
        description="Parsed content structure"
    )

