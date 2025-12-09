"""Get All Placement Tests endpoint for PowerPath.

GET /powerpath/placement/getAllPlacementTests

Returns all placement tests for a subject, including available results for each.
A 'Lesson' (placement test) in this context is a ComponentResource object which
has a Resource object with metadata.lessonType = "placement" associated with it.
"""

from typing import Any, Dict

from timeback.http import HttpClient
from timeback.models.request import TimebackGetAllPlacementTestsRequest
from timeback.models.response import TimebackGetAllPlacementTestsResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def get_all_placement_tests(
    http: HttpClient,
    request: TimebackGetAllPlacementTestsRequest,
) -> TimebackGetAllPlacementTestsResponse:
    """Fetch all placement tests for a student and subject.

    GET /powerpath/placement/getAllPlacementTests

    Args:
        http: Injected HTTP client for making requests
        request: Request containing student sourcedId and subject

    Returns:
        TimebackGetAllPlacementTestsResponse containing list of placement tests
    """
    path = "/powerpath/placement/getAllPlacementTests"

    # Build query parameters from request
    query: Dict[str, Any] = {
        "student": request.student,
        "subject": request.subject.value,  # Convert enum to string value
    }

    data: Dict[str, Any] = http.get(path, params=query)
    log.debug(f"Raw Data: {data}")
    return TimebackGetAllPlacementTestsResponse.model_validate(data)

