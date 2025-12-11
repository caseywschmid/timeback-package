"""Request model for updating a test part.

PUT /assessment-tests/{assessmentTestIdentifier}/test-parts/{identifier}

Used by:
- timeback/services/qti/endpoints/update_test_part.py
"""

from typing import List
from pydantic import BaseModel, Field, ConfigDict
from timeback.enums import TimebackQTINavigationMode, TimebackQTISubmissionMode
from timeback.models.timeback_qti_section import TimebackQTISection


class TimebackUpdateTestPartRequest(BaseModel):
    """Request model for updating a test part.
    
    Updates a test part including its navigation mode, submission mode,
    and sections. All required fields must be provided.
    
    Attributes:
        Required:
            - identifier (str): Unique identifier for the test part
            - navigation_mode (TimebackQTINavigationMode): How learners navigate
            - submission_mode (TimebackQTISubmissionMode): How responses are submitted
            - qti_assessment_section (list): At least one section. See TimebackQTISection.
    
    Example:
        request = TimebackUpdateTestPartRequest(
            identifier="part-001",
            navigation_mode=TimebackQTINavigationMode.NONLINEAR,
            submission_mode=TimebackQTISubmissionMode.SIMULTANEOUS,
            qti_assessment_section=[
                TimebackQTISection(
                    identifier="section-001",
                    title="Updated Section"
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

