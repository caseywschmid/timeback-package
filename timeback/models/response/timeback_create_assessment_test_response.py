"""Response model for creating a QTI assessment test.

POST /assessment-tests

Used by:
- timeback/services/qti/endpoints/create_assessment_test.py
"""

from timeback.models.timeback_qti_assessment_test import TimebackQTIAssessmentTest


class TimebackCreateAssessmentTestResponse(TimebackQTIAssessmentTest):
    """Response model for creating a QTI assessment test.
    
    Inherits all fields from TimebackQTIAssessmentTest.
    Returns the created assessment test with all generated fields populated.
    """
    pass

