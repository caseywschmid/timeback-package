"""Start Test Out endpoint for PowerPath.

POST /powerpath/lessonPlans/startTestOut

Creates an on-demand test-out assignment for a student in a course.
This is the recommended replacement for create_external_test_out.
"""

from typing import Any, Dict

from timeback.http import HttpClient
from timeback.models.request import TimebackStartTestOutRequest
from timeback.models.response import TimebackStartTestOutResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def start_test_out(
    http: HttpClient,
    request: TimebackStartTestOutRequest,
) -> TimebackStartTestOutResponse:
    """Start a test-out assignment for a student.

    POST /powerpath/lessonPlans/startTestOut

    Creates an on-demand test-out assignment. After calling this endpoint,
    use make_external_test_assignment to start the test with the provider.

    Eligibility requirements:
    - Course must have a supported subject+grade combination
    - Student must be actively enrolled in a course with that subject+grade
    - Student must not have a completed or failed test-out for this subject+grade

    Args:
        http: Injected HTTP client for making requests
        request: Request containing courseId and studentId

    Returns:
        TimebackStartTestOutResponse with assignmentId, lessonId, resourceId, and status
    """
    path = "/powerpath/lessonPlans/startTestOut"

    # Build request body using aliases for camelCase
    body: Dict[str, Any] = request.model_dump(exclude_none=True, by_alias=True)

    data: Dict[str, Any] = http.post(path, json=body)
    log.debug(f"Raw Data: {data}")
    return TimebackStartTestOutResponse.model_validate(data)

