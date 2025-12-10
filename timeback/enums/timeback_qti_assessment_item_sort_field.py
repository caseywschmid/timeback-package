"""QTI API sort field enum for assessment items.

Used by:
- timeback/models/request/timeback_search_assessment_items_request.py
"""

from enum import Enum


class TimebackQTIAssessmentItemSortField(str, Enum):
    """Sort fields available for assessment item search endpoints.
    
    These fields are available for sorting assessment items in search/list operations.
    """
    
    TITLE = "title"
    IDENTIFIER = "identifier"
    TYPE = "type"
    CREATED_AT = "createdAt"
    UPDATED_AT = "updatedAt"

