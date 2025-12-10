"""Response model for creating a QTI assessment item.

POST /assessment-items

Used by:
- timeback/services/qti/endpoints/create_assessment_item.py
"""

from timeback.models.timeback_qti_assessment_item import TimebackQTIAssessmentItem


class TimebackCreateAssessmentItemResponse(TimebackQTIAssessmentItem):
    """Response model for creating a QTI assessment item.
    
    Inherits all fields from TimebackQTIAssessmentItem.
    Returns the created assessment item with all generated fields populated.
    """
    pass

