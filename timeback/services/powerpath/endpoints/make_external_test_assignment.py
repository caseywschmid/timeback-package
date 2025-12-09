"""Make External Test Assignment endpoint for PowerPath.

POST /powerpath/makeExternalTestAssignment

Makes an external test assignment for a student.
Applies to 'test-out', 'placement', and 'unit-test' lessons.

The behavior varies by tool provider:
- For "edulastic": Authenticates student, assigns test, returns credentials and IDs
- For "mastery-track": Authenticates student, assigns test, waits for result write-back
"""

from typing import Any, Dict

from timeback.http import HttpClient
from timeback.models.request import TimebackMakeExternalTestAssignmentRequest
from timeback.models.response import TimebackMakeExternalTestAssignmentResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def make_external_test_assignment(
    http: HttpClient,
    request: TimebackMakeExternalTestAssignmentRequest,
) -> TimebackMakeExternalTestAssignmentResponse:
    """Make an external test assignment for a student.

    POST /powerpath/makeExternalTestAssignment

    Args:
        http: Injected HTTP client for making requests
        request: Request containing student, lesson, and optional test configuration

    Returns:
        TimebackMakeExternalTestAssignmentResponse with credentials, test URL, and IDs
    """
    path = "/powerpath/makeExternalTestAssignment"

    # Build request body, excluding None values
    body: Dict[str, Any] = request.model_dump(exclude_none=True)

    data: Dict[str, Any] = http.post(path, json=body)
    log.debug(f"Raw Data: {data}")
    return TimebackMakeExternalTestAssignmentResponse.model_validate(data)

