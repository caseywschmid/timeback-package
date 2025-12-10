"""QTI submission mode enum.

Used by:
- timeback/models/request/timeback_search_assessment_tests_request.py
- timeback/models/timeback_qti_test_part.py
"""

from enum import Enum


class TimebackQTISubmissionMode(str, Enum):
    """Submission mode for QTI test parts.
    
    Determines how learner responses are submitted for response processing.
    
    Values:
        INDIVIDUAL: Responses can be submitted as each item is completed
        SIMULTANEOUS: Responses for all items are sent when the whole part is completed
    """
    
    INDIVIDUAL = "individual"
    SIMULTANEOUS = "simultaneous"

