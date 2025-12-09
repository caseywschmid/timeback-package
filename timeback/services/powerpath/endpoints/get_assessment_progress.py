"""Get Assessment Progress endpoint for PowerPath.

GET /powerpath/getAssessmentProgress

Returns the progress a student has made in a PowerPath lesson.
"""

from typing import Any, Dict, Optional

from timeback.http import HttpClient
from timeback.models.response import TimebackAssessmentProgressResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def get_assessment_progress(
    http: HttpClient,
    student: str,
    lesson: str,
    attempt: Optional[int] = None,
) -> TimebackAssessmentProgressResponse:
    """Get assessment progress for a student in a lesson.

    GET /powerpath/getAssessmentProgress

    Returns progress including:
    - Current score and XP
    - Questions answered with responses
    - Accuracy and completion metrics

    Args:
        http: Injected HTTP client for making requests
        student: The sourcedId of the student
        lesson: The sourcedId of the lesson (ComponentResource)
        attempt: Optional attempt number to query specific attempt

    Returns:
        TimebackAssessmentProgressResponse with progress data
    """
    path = "/powerpath/getAssessmentProgress"

    params: Dict[str, str] = {
        "student": student,
        "lesson": lesson,
    }
    if attempt is not None:
        params["attempt"] = str(attempt)

    data: Dict[str, Any] = http.get(path, params=params)
    log.debug(f"Raw Data: {data}")
    return TimebackAssessmentProgressResponse.model_validate(data)

