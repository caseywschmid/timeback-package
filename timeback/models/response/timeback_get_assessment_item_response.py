"""Response model for getting a single QTI assessment item.

GET /assessment-items/{identifier}

Used by:
- timeback/services/qti/endpoints/get_assessment_item.py
"""

from timeback.models.timeback_qti_assessment_item import TimebackQTIAssessmentItem


class TimebackGetAssessmentItemResponse(TimebackQTIAssessmentItem):
    """Response model for getting a single QTI assessment item.
    
    Inherits all fields from TimebackQTIAssessmentItem.
    This provides the complete assessment item including:
    - identifier, title, type
    - qtiVersion, timeDependent, adaptive
    - responseDeclarations, outcomeDeclarations
    - responseProcessing
    - feedbackBlock, rubrics, stimulus
    - metadata, rawXml, content
    """
    pass

