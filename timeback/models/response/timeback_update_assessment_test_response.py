"""Response model for updating a QTI assessment test.

PUT /assessment-tests/{identifier}

Used by:
- timeback/services/qti/endpoints/update_assessment_test.py
"""

from timeback.models.timeback_qti_assessment_test import TimebackQTIAssessmentTest


class TimebackUpdateAssessmentTestResponse(TimebackQTIAssessmentTest):
    """Response model for updating a QTI assessment test.
    
    Inherits all fields from TimebackQTIAssessmentTest.
    Returns the updated assessment test with regenerated XML and validated content.
    """
    pass

