"""Create Test Assignment endpoint for PowerPath.

POST /powerpath/test-assignments

Creates a standalone test-out assignment for a student.
"""

from typing import Any, Dict

from timeback.http import HttpClient
from timeback.models.request import TimebackCreateTestAssignmentRequest
from timeback.models.response import TimebackCreateTestAssignmentResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def create_test_assignment(
    http: HttpClient,
    request: TimebackCreateTestAssignmentRequest,
) -> TimebackCreateTestAssignmentResponse:
    """Create an individual test assignment.

    POST /powerpath/test-assignments

    Creates a standalone test-out assignment for a student,
    generating a Resource and an unlisted ComponentResource.

    Args:
        http: Injected HTTP client for making requests
        request: Request with student, subject, grade, and optional testName

    Returns:
        TimebackCreateTestAssignmentResponse with assignmentId, lessonId, resourceId
    """
    path = "/powerpath/test-assignments"

    body = request.model_dump(exclude_none=True, by_alias=True)

    data: Dict[str, Any] = http.post(path, json=body)
    log.debug(f"Raw Data: {data}")
    return TimebackCreateTestAssignmentResponse.model_validate(data)

