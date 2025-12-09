"""Create New Attempt endpoint for PowerPath.

POST /powerpath/createNewAttempt

Creates a new attempt for a student in a lesson.
"""

from typing import Any, Dict

from timeback.http import HttpClient
from timeback.models.request import TimebackCreateNewAttemptRequest
from timeback.models.response import TimebackCreateNewAttemptResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def create_new_attempt(
    http: HttpClient,
    request: TimebackCreateNewAttemptRequest,
) -> TimebackCreateNewAttemptResponse:
    """Create a new attempt for a student in a lesson.

    POST /powerpath/createNewAttempt

    Creates a new attempt if the current attempt is completed.
    For Assessment Bank lessons, this updates the state to serve
    a different sub-test using round-robin logic.

    Args:
        http: Injected HTTP client for making requests
        request: Request with student and lesson IDs

    Returns:
        TimebackCreateNewAttemptResponse with attempt data
    """
    path = "/powerpath/createNewAttempt"

    body = request.model_dump(exclude_none=True, by_alias=True)

    data: Dict[str, Any] = http.post(path, json=body)
    log.debug(f"Raw Data: {data}")
    return TimebackCreateNewAttemptResponse.model_validate(data)

