"""Get Test-Out endpoint for PowerPath.

GET /powerpath/testOut

**DEPRECATED**: This endpoint is deprecated. Use GET /powerpath/lessonPlans/getCourseProgress instead.

Returns the testOut lesson reference for a student and course.
"""

import warnings
from typing import Any, Dict

from timeback.http import HttpClient
from timeback.models.request import TimebackGetTestOutRequest
from timeback.models.response import TimebackGetTestOutResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def get_test_out(
    http: HttpClient,
    request: TimebackGetTestOutRequest,
) -> TimebackGetTestOutResponse:
    """Get test-out information for a student and course.

    GET /powerpath/testOut

    **DEPRECATED**: This endpoint is deprecated. Use get_course_progress() instead.
    The response includes a `testOut` field with comprehensive status information.

    Args:
        http: Injected HTTP client for making requests
        request: Request containing student and course sourcedIds

    Returns:
        TimebackGetTestOutResponse with lesson info, finalized status, and credentials
    """
    warnings.warn(
        "get_test_out is deprecated. Use get_course_progress() instead.",
        DeprecationWarning,
        stacklevel=2,
    )

    path = "/powerpath/testOut"

    # Build query parameters from request
    query: Dict[str, Any] = {
        "student": request.student,
        "course": request.course,
    }

    data: Dict[str, Any] = http.get(path, params=query)
    log.debug(f"Raw Data: {data}")
    return TimebackGetTestOutResponse.model_validate(data)

