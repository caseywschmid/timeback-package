"""Update Test Assignment endpoint for PowerPath.

PUT /powerpath/test-assignments/{id}

Updates a test assignment (currently only testName).
"""

from typing import Any, Dict

from timeback.http import HttpClient
from timeback.models.request import TimebackUpdateTestAssignmentRequest
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def update_test_assignment(
    http: HttpClient,
    assignment_id: str,
    request: TimebackUpdateTestAssignmentRequest,
) -> None:
    """Update a test assignment.

    PUT /powerpath/test-assignments/{id}

    Currently only supports updating the test name.
    Returns 204 No Content on success.

    Args:
        http: Injected HTTP client for making requests
        assignment_id: The test assignment sourcedId
        request: Request with testName

    Returns:
        None (204 response)
    """
    path = f"/powerpath/test-assignments/{assignment_id}"

    body = request.model_dump(exclude_none=True, by_alias=True)

    http.put(path, json=body)
    log.debug("Update successful (204)")

