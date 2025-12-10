"""QTI API sort field enum for assessment tests.

Used by:
- timeback/models/request/timeback_search_assessment_tests_request.py
"""

from enum import Enum


class TimebackQTIAssessmentTestSortField(str, Enum):
    """Sort fields available for assessment test search endpoints.
    
    These fields are available for sorting assessment tests in search/list operations.
    """
    
    TITLE = "title"
    IDENTIFIER = "identifier"
    CREATED_AT = "createdAt"
    UPDATED_AT = "updatedAt"

