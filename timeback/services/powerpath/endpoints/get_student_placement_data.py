"""Get Student Placement Data endpoint for PowerPath.

GET /powerpath/placement/{studentId}

Returns comprehensive placement data for a student across all subjects,
including grades, RIT scores, test results, and placement status.
"""

from typing import Any, Dict

from timeback.http import HttpClient
from timeback.models import TimebackSubjectPlacementData
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")

# Type alias for the response - a dictionary with subject names as keys
StudentPlacementDataResponse = Dict[str, TimebackSubjectPlacementData]


def get_student_placement_data(
    http: HttpClient,
    student_id: str,
) -> StudentPlacementDataResponse:
    """Get comprehensive placement data for a student.

    GET /powerpath/placement/{studentId}

    Returns placement data for all subjects including:
    - Starting and current grade levels
    - RIT scores (GROWTH and SCREENING)
    - Test results with status and scores
    - Next test ID for each subject

    Args:
        http: Injected HTTP client for making requests
        student_id: The sourcedId of the student

    Returns:
        Dictionary with subject names as keys and TimebackSubjectPlacementData as values.
        Subjects include: Reading, Language, Vocabulary, Social Studies, Writing, 
        Science, FastMath, Math
    """
    path = f"/powerpath/placement/{student_id}"

    data: Dict[str, Any] = http.get(path)
    log.debug(f"Raw Data: {data}")

    # Parse each subject's placement data
    result: StudentPlacementDataResponse = {}
    for subject, subject_data in data.items():
        result[subject] = TimebackSubjectPlacementData.model_validate(subject_data)

    return result

