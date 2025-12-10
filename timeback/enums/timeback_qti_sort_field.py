"""QTI API sort field enum for stimuli, assessment items, and tests.

Used by:
- timeback/models/request/timeback_search_stimuli_request.py
- timeback/models/request/timeback_search_assessment_items_request.py
- timeback/models/request/timeback_search_assessment_tests_request.py
"""

from enum import Enum


class TimebackQTISortField(str, Enum):
    """Sort fields available for QTI entity search endpoints.
    
    These fields are available for sorting stimuli, assessment items,
    and assessment tests in search/list operations.
    """
    
    TITLE = "title"
    IDENTIFIER = "identifier"
    CREATED_AT = "createdAt"
    UPDATED_AT = "updatedAt"

