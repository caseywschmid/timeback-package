"""Sort order enum for API endpoints.

Used by:
- timeback/models/request/timeback_search_stimuli_request.py
- timeback/models/request/timeback_search_assessment_items_request.py
- timeback/models/request/timeback_search_assessment_tests_request.py
"""

from enum import Enum


class TimebackSortOrder(str, Enum):
    """Sort order for API search/list endpoints.
    
    Specifies whether results should be sorted in ascending
    or descending order.
    """
    
    ASC = "asc"
    DESC = "desc"

