"""Get Test Assignment endpoint for PowerPath.

GET /powerpath/test-assignments/{id}

Returns a single test assignment by ID.
"""

from typing import Any, Dict

from timeback.http import HttpClient
from timeback.models.timeback_test_assignment import TimebackTestAssignment
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def get_test_assignment(
    http: HttpClient,
    assignment_id: str,
) -> TimebackTestAssignment:
    """Get a test assignment by ID.

    GET /powerpath/test-assignments/{id}

    Args:
        http: Injected HTTP client for making requests
        assignment_id: The test assignment sourcedId

    Returns:
        TimebackTestAssignment with assignment details
    """
    path = f"/powerpath/test-assignments/{assignment_id}"

    data: Dict[str, Any] = http.get(path)
    log.debug(f"Raw Data: {data}")
    return TimebackTestAssignment.model_validate(data)

