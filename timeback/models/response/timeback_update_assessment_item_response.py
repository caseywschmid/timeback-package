"""Response model for updating a QTI assessment item.

PUT /assessment-items/{identifier}

Used by:
- timeback/services/qti/endpoints/update_assessment_item.py
"""

from timeback.models.timeback_qti_assessment_item import TimebackQTIAssessmentItem


class TimebackUpdateAssessmentItemResponse(TimebackQTIAssessmentItem):
    """Response model for updating a QTI assessment item.
    
    Inherits all fields from TimebackQTIAssessmentItem.
    Returns the updated assessment item with regenerated XML and validated content.
    """
    pass

