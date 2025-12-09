"""Get Attempts endpoint for PowerPath.

GET /powerpath/getAttempts

Returns all attempts for a student in a lesson.
"""

from typing import Any, Dict

from timeback.http import HttpClient
from timeback.models.response import TimebackGetAttemptsResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def get_attempts(
    http: HttpClient,
    student: str,
    lesson: str,
) -> TimebackGetAttemptsResponse:
    """Get all attempts for a student in a lesson.

    GET /powerpath/getAttempts

    For Assessment Bank lessons, each attempt may represent a different
    sub-test of the bank.

    Args:
        http: Injected HTTP client for making requests
        student: The sourcedId of the student
        lesson: The sourcedId of the lesson (ComponentResource)

    Returns:
        TimebackGetAttemptsResponse with list of all attempts
    """
    path = "/powerpath/getAttempts"

    params: Dict[str, str] = {
        "student": student,
        "lesson": lesson,
    }

    data: Dict[str, Any] = http.get(path, params=params)
    log.debug(f"Raw Data: {data}")
    return TimebackGetAttemptsResponse.model_validate(data)

