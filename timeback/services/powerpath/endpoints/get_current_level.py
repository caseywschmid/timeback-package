"""Get Current Level endpoint for PowerPath.

GET /powerpath/placement/getCurrentLevel

Returns the current level of the student in a placement process:
- The level is determined by the last completed placement test's grade level,
  starting from the lowest grade level available for the subject's placement tests.
- As the student completes placement tests and attains scores of 90 or greater,
  their level updates to the next level available for the subject.

Also returns the 'onboarded' boolean that indicates if the student completed
the onboarding process for the subject.
"""

from typing import Any, Dict

from timeback.http import HttpClient
from timeback.models.request import TimebackGetCurrentLevelRequest
from timeback.models.response import TimebackGetCurrentLevelResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def get_current_level(
    http: HttpClient,
    request: TimebackGetCurrentLevelRequest,
) -> TimebackGetCurrentLevelResponse:
    """Fetch the current level of a student in a placement process.

    GET /powerpath/placement/getCurrentLevel

    Args:
        http: Injected HTTP client for making requests
        request: Request containing student sourcedId and subject

    Returns:
        TimebackGetCurrentLevelResponse containing gradeLevel, onboarded status, and availableTests
    """
    path = "/powerpath/placement/getCurrentLevel"

    # Build query parameters from request
    query: Dict[str, Any] = {
        "student": request.student,
        "subject": request.subject.value,  # Convert enum to string value
    }

    data: Dict[str, Any] = http.get(path, params=query)
    log.debug(f"Raw Data: {data}")
    return TimebackGetCurrentLevelResponse.model_validate(data)

