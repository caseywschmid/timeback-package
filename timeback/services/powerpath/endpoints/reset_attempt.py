"""Reset Attempt endpoint for PowerPath.

POST /powerpath/resetAttempt

Resets a student's attempt for a lesson.
"""

from typing import Any, Dict

from timeback.http import HttpClient
from timeback.models.request import TimebackResetAttemptRequest
from timeback.models.response import TimebackResetAttemptResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def reset_attempt(
    http: HttpClient,
    request: TimebackResetAttemptRequest,
) -> TimebackResetAttemptResponse:
    """Reset a student's attempt for a lesson.

    POST /powerpath/resetAttempt

    Resets the attempt by:
    - Soft-deleting previous question responses
    - Resetting test score to 0
    - Updating scoreStatus to "not submitted"

    For external tests, only resets the score to 0.
    For Assessment Bank lessons, keeps user in same bank test.

    Args:
        http: Injected HTTP client for making requests
        request: Request with student and lesson IDs

    Returns:
        TimebackResetAttemptResponse with success status and score
    """
    path = "/powerpath/resetAttempt"

    body = request.model_dump(exclude_none=True, by_alias=True)

    data: Dict[str, Any] = http.post(path, json=body)
    log.debug(f"Raw Data: {data}")
    return TimebackResetAttemptResponse.model_validate(data)

