"""Response model for batch updating assessment item metadata.

POST /assessment-items/metadata

Used by:
- timeback/services/qti/endpoints/update_metadata.py
"""

from timeback.models.timeback_qti_assessment_item import TimebackQTIAssessmentItem


class TimebackUpdateAssessmentItemMetadataResponse(TimebackQTIAssessmentItem):
    """Response model for batch updating assessment item metadata.
    
    Inherits all fields from TimebackQTIAssessmentItem.
    Returns the updated assessment item with the new metadata applied.
    """
    pass

