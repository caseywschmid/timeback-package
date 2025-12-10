"""Response model for getting a single QTI assessment test.

GET /assessment-tests/{identifier}

Used by:
- timeback/services/qti/endpoints/get_assessment_test.py
"""

from timeback.models.timeback_qti_assessment_test import TimebackQTIAssessmentTest


class TimebackGetAssessmentTestResponse(TimebackQTIAssessmentTest):
    """Response model for getting a single QTI assessment test.
    
    Inherits all fields from TimebackQTIAssessmentTest.
    This provides the complete assessment test including all test parts,
    sections, and assessment item references.
    """
    pass

