"""Create External Test-Out endpoint for PowerPath.

POST /powerpath/createExternalTestOut

**DEPRECATED**: This endpoint is deprecated. Use POST /powerpath/lessonPlans/startTestOut instead.

Creates or updates a ComponentResource to act as a TestOut lesson in a course.
This allows integrating with external test-taking platforms (like Edulastic).

The endpoint creates or updates:
- A CourseComponent for the course to hold the TestOut lesson
- A Resource with lessonType = "test-out" and the external service details as metadata
- A ComponentResource acting as the TestOut lesson
"""

import warnings
from typing import Any, Dict

from timeback.http import HttpClient
from timeback.models.request import TimebackCreateExternalTestOutRequest
from timeback.models.response import TimebackCreateExternalTestResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def create_external_test_out(
    http: HttpClient,
    request: TimebackCreateExternalTestOutRequest,
) -> TimebackCreateExternalTestResponse:
    """Create an external test-out lesson for a course.

    POST /powerpath/createExternalTestOut

    **DEPRECATED**: This endpoint is deprecated. Use start_test_out() instead.
    Migration flow:
    1. Check availability: get_course_progress(courseId, studentId)
    2. Start test-out: start_test_out(courseId, studentId)
    3. Launch test: make_external_test_assignment(...)

    Args:
        http: Injected HTTP client for making requests
        request: Request containing course info, tool provider, grades, xp, and optional metadata

    Returns:
        TimebackCreateExternalTestResponse containing lessonId, courseComponentId, resourceId, etc.
    """
    warnings.warn(
        "create_external_test_out is deprecated. Use start_test_out() instead.",
        DeprecationWarning,
        stacklevel=2,
    )

    path = "/powerpath/createExternalTestOut"

    # Build request body, excluding None values
    body: Dict[str, Any] = request.model_dump(exclude_none=True)

    data: Dict[str, Any] = http.post(path, json=body)
    log.debug(f"Raw Data: {data}")
    return TimebackCreateExternalTestResponse.model_validate(data)

