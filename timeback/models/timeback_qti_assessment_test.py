"""QTI Assessment Test model.

Used by:
- timeback/models/response/timeback_search_assessment_tests_response.py
- timeback/models/response/timeback_get_assessment_test_response.py
- timeback/models/response/timeback_create_assessment_test_response.py
- timeback/models/response/timeback_update_assessment_test_response.py
"""

from typing import Any, Dict, List, Optional
from pydantic import BaseModel, ConfigDict, Field
from timeback.models.timeback_qti_test_part import TimebackQTITestPart
from timeback.models.timeback_qti_outcome_declaration import (
    TimebackQTIOutcomeDeclaration,
)


class TimebackQTIAssessmentTest(BaseModel):
    """QTI Assessment Test model.
    
    Assessment tests are the top-level containers that define complete testing
    experiences through their test parts and sections.
    
    Attributes:
        Required:
            - identifier (str): Unique identifier for the assessment test
            - title (str): Human-readable title
        
        Optional:
            - qti_version (str, optional): QTI version (default: "3.0")
            - tool_name (str, optional): Name of the tool that created the test
            - tool_version (str, optional): Version of the tool
            - qti_test_part (list, optional): List of test parts.
              See TimebackQTITestPart for structure.
            - qti_outcome_declaration (list, optional): Outcome variable declarations.
              See TimebackQTIOutcomeDeclaration for structure.
            - time_limit (float, optional): Time limit in seconds
            - max_attempts (int, optional): Maximum attempts allowed
            - tools_enabled (dict, optional): Configuration of enabled tools
            - metadata (dict, optional): Custom metadata
            - raw_xml (str, optional): Raw XML representation
            - content (dict, optional): Parsed XML content structure
            - created_at (str, optional): ISO 8601 creation timestamp
            - updated_at (str, optional): ISO 8601 last update timestamp
    """
    
    model_config = ConfigDict(populate_by_name=True)
    
    identifier: str
    title: str
    qti_version: Optional[str] = Field(None, alias="qtiVersion")
    tool_name: Optional[str] = Field(None, alias="toolName")
    tool_version: Optional[str] = Field(None, alias="toolVersion")
    qti_test_part: Optional[List[TimebackQTITestPart]] = Field(
        None, alias="qti-test-part"
    )
    qti_outcome_declaration: Optional[List[TimebackQTIOutcomeDeclaration]] = Field(
        None, alias="qti-outcome-declaration"
    )
    time_limit: Optional[float] = Field(None, alias="timeLimit")
    max_attempts: Optional[int] = Field(None, alias="maxAttempts")
    tools_enabled: Optional[Dict[str, bool]] = Field(None, alias="toolsEnabled")
    metadata: Optional[Dict[str, Any]] = None
    raw_xml: Optional[str] = Field(None, alias="rawXml")
    content: Optional[Dict[str, Any]] = None
    created_at: Optional[str] = Field(None, alias="createdAt")
    updated_at: Optional[str] = Field(None, alias="updatedAt")


