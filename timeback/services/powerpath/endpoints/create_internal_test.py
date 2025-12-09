"""Create Internal Test endpoint for PowerPath.

POST /powerpath/createInternalTest

Creates or updates a ComponentResource to act as an internal test lesson in a course.
Supports two test types:
- QTI: Creates a single QTI resource
- Assessment Bank: Creates multiple QTI resources wrapped in an assessment bank

The endpoint creates or updates:
- A CourseComponent for the course to hold the test lesson
- One or more Resources with type = "qti" or type = "assessment-bank"
- A ComponentResource acting as the test lesson
"""

from typing import Any, Dict, Union

from timeback.http import HttpClient
from timeback.models.request import (
    TimebackCreateInternalQtiTestRequest,
    TimebackCreateInternalAssessmentBankTestRequest,
)
from timeback.models.response import TimebackCreateInternalTestResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def create_internal_test(
    http: HttpClient,
    request: Union[TimebackCreateInternalQtiTestRequest, TimebackCreateInternalAssessmentBankTestRequest],
) -> TimebackCreateInternalTestResponse:
    """Create an internal test lesson for a course.

    POST /powerpath/createInternalTest

    Supports two test types:
    - QTI (testType="qti"): Creates a single QTI resource
    - Assessment Bank (testType="assessment-bank"): Creates multiple QTI resources in a bank

    Args:
        http: Injected HTTP client for making requests
        request: Request containing course info, lesson type, test type, and QTI/assessment-bank config

    Returns:
        TimebackCreateInternalTestResponse containing lessonId, courseComponentId, resourceId, etc.
    """
    path = "/powerpath/createInternalTest"

    # Build request body, excluding None values
    body: Dict[str, Any] = request.model_dump(exclude_none=True)

    data: Dict[str, Any] = http.post(path, json=body)
    log.debug(f"Raw Data: {data}")
    return TimebackCreateInternalTestResponse.model_validate(data)

