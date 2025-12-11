"""QTI Test Part model.

Used by:
- timeback/models/timeback_qti_assessment_test.py
- timeback/models/response/timeback_search_test_parts_response.py
"""

from typing import List, Optional
from pydantic import BaseModel, Field, ConfigDict
from timeback.models.timeback_qti_section import TimebackQTISection
from timeback.enums import TimebackQTINavigationMode, TimebackQTISubmissionMode


class TimebackQTITestPart(BaseModel):
    """QTI Test Part model.
    
    Test parts are organizational units within an assessment test that group
    sections and define testing behaviors like linear/nonlinear navigation.
    
    Attributes:
        Required:
            - identifier (str): Unique identifier for the test part
            - navigation_mode (TimebackQTINavigationMode): How learners navigate (linear/nonlinear)
            - submission_mode (TimebackQTISubmissionMode): How responses are submitted
        
        Optional:
            - qti_assessment_section (list): List of sections in this test part
    """
    
    model_config = ConfigDict(populate_by_name=True)
    
    identifier: str = Field(..., description="Unique identifier for the test part")
    navigation_mode: TimebackQTINavigationMode = Field(
        default=TimebackQTINavigationMode.LINEAR,
        alias="navigationMode",
        description="Controls how learners navigate through the test part"
    )
    submission_mode: TimebackQTISubmissionMode = Field(
        default=TimebackQTISubmissionMode.INDIVIDUAL,
        alias="submissionMode",
        description="Determines how learner responses are submitted"
    )
    qti_assessment_section: Optional[List[TimebackQTISection]] = Field(
        None,
        alias="qti-assessment-section",
        description="List of sections in this test part"
    )


