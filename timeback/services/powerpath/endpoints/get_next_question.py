"""Get Next Question endpoint for PowerPath.

GET /powerpath/getNextQuestion

Returns the next question in a PowerPath-100 lesson.
"""

from typing import Any, Dict

from timeback.http import HttpClient
from timeback.models.response import TimebackNextQuestionResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def get_next_question(
    http: HttpClient,
    student: str,
    lesson: str,
) -> TimebackNextQuestionResponse:
    """Get the next question for a student in a PowerPath-100 lesson.

    GET /powerpath/getNextQuestion

    Note: This endpoint only works with lessons of type 'powerpath-100'.

    Args:
        http: Injected HTTP client for making requests
        student: The sourcedId of the student
        lesson: The sourcedId of the lesson (ComponentResource)

    Returns:
        TimebackNextQuestionResponse with score and next question
    """
    path = "/powerpath/getNextQuestion"

    params: Dict[str, str] = {
        "student": student,
        "lesson": lesson,
    }

    data: Dict[str, Any] = http.get(path, params=params)
    log.debug(f"Raw Data: {data}")
    return TimebackNextQuestionResponse.model_validate(data)

