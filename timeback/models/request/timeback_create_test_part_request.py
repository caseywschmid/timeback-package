"""Request model for creating a test part.

POST /assessment-tests/{assessmentTestIdentifier}/test-parts

Used by:
- timeback/services/qti/endpoints/create_test_part.py
"""

from typing import List
from pydantic import BaseModel, Field, ConfigDict
from timeback.enums import TimebackQTINavigationMode, TimebackQTISubmissionMode
from timeback.models.timeback_qti_section import TimebackQTISection


class TimebackCreateTestPartRequest(BaseModel):
    """Request model for creating a test part.
    
    Test parts organize sections and define navigation behaviors (linear/nonlinear)
    and submission modes. A test part must contain at least one assessment section.
    
    Attributes:
        Required:
            - identifier (str): Unique identifier for the test part
            - navigation_mode (TimebackQTINavigationMode): How learners navigate
            - submission_mode (TimebackQTISubmissionMode): How responses are submitted
            - qti_assessment_section (list): At least one section. See TimebackQTISection.
    
    Example:
        request = TimebackCreateTestPartRequest(
            identifier="part-001",
            navigation_mode=TimebackQTINavigationMode.LINEAR,
            submission_mode=TimebackQTISubmissionMode.INDIVIDUAL,
            qti_assessment_section=[
                TimebackQTISection(
                    identifier="section-001",
                    title="Section 1"
                )
            ]
        )
    """
    
    model_config = ConfigDict(populate_by_name=True)
    
    identifier: str = Field(..., description="Unique identifier for the test part")
    navigation_mode: TimebackQTINavigationMode = Field(
        ...,
        alias="navigationMode",
        description="Controls how learners navigate through the test part"
    )
    submission_mode: TimebackQTISubmissionMode = Field(
        ...,
        alias="submissionMode",
        description="Determines how learner responses are submitted"
    )
    qti_assessment_section: List[TimebackQTISection] = Field(
        ...,
        alias="qti-assessment-section",
        description="List of sections in this test part (at least one required)"
    )

