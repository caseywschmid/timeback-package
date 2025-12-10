"""QTI navigation mode enum.

Used by:
- timeback/models/request/timeback_search_assessment_tests_request.py
- timeback/models/timeback_qti_test_part.py
"""

from enum import Enum


class TimebackQTINavigationMode(str, Enum):
    """Navigation mode for QTI test parts.
    
    Controls how learners navigate through the test part.
    
    Values:
        LINEAR: Sequential navigation - items must be responded to in sequence
                without jumping around
        NONLINEAR: Free navigation - candidates can respond to items in any order
    """
    
    LINEAR = "linear"
    NONLINEAR = "nonlinear"

