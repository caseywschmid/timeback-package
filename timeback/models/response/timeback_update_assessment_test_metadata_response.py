"""Response model for updating assessment test metadata only.

PUT /assessment-tests/{identifier}/metadata

Used by:
- timeback/services/qti/endpoints/update_assessment_test_metadata.py
"""

from timeback.models.timeback_qti_assessment_test import TimebackQTIAssessmentTest


class TimebackUpdateAssessmentTestMetadataResponse(TimebackQTIAssessmentTest):
    """Response model for updating assessment test metadata only.
    
    Inherits all fields from TimebackQTIAssessmentTest.
    Returns the assessment test with updated metadata.
    """
    pass

