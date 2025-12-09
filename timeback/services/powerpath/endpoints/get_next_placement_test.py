"""Get Next Placement Test endpoint for PowerPath.

GET /powerpath/placement/getNextPlacementTest

Returns the next placement test for the student in a subject:
- If the student has completed all placement tests, lesson will be null and exhaustedTests = true.
- If the student hasn't started, returns the first placement test.
- If the student scored < 90 on last test, returns null (onboarded = true).
- If the student scored >= 90, returns the next test.

A 'Lesson' in this context is a ComponentResource object which has a Resource 
object with metadata.lessonType = "placement" associated with it.
"""

from typing import Any, Dict

from timeback.http import HttpClient
from timeback.models.request import TimebackGetNextPlacementTestRequest
from timeback.models.response import TimebackGetNextPlacementTestResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def get_next_placement_test(
    http: HttpClient,
    request: TimebackGetNextPlacementTestRequest,
) -> TimebackGetNextPlacementTestResponse:
    """Fetch the next placement test for a student in a subject.

    GET /powerpath/placement/getNextPlacementTest

    Args:
        http: Injected HTTP client for making requests
        request: Request containing student sourcedId and subject

    Returns:
        TimebackGetNextPlacementTestResponse containing next test info, onboarded status, etc.
    """
    path = "/powerpath/placement/getNextPlacementTest"

    # Build query parameters from request
    query: Dict[str, Any] = {
        "student": request.student,
        "subject": request.subject.value,  # Convert enum to string value
    }

    data: Dict[str, Any] = http.get(path, params=query)
    log.debug(f"Raw Data: {data}")
    return TimebackGetNextPlacementTestResponse.model_validate(data)

