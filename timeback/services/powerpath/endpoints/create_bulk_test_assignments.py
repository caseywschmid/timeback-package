"""Create Bulk Test Assignments endpoint for PowerPath.

POST /powerpath/test-assignments/bulk

Creates multiple test assignments in one request.
"""

from typing import Any, Dict

from timeback.http import HttpClient
from timeback.models.request import TimebackBulkTestAssignmentsRequest
from timeback.models.response import TimebackBulkTestAssignmentsResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def create_bulk_test_assignments(
    http: HttpClient,
    request: TimebackBulkTestAssignmentsRequest,
) -> TimebackBulkTestAssignmentsResponse:
    """Create multiple test assignments.

    POST /powerpath/test-assignments/bulk

    All-or-nothing operation: validates all items and reports
    all errors before processing. Returns 200 if all succeed,
    400 if any validation errors are found.

    Args:
        http: Injected HTTP client for making requests
        request: Request with items array

    Returns:
        TimebackBulkTestAssignmentsResponse with success, results, errors
    """
    path = "/powerpath/test-assignments/bulk"

    body = request.model_dump(exclude_none=True, by_alias=True)

    data: Dict[str, Any] = http.post(path, json=body)
    log.debug(f"Raw Data: {data}")
    return TimebackBulkTestAssignmentsResponse.model_validate(data)

