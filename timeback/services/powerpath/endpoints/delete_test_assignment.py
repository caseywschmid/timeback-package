"""Delete Test Assignment endpoint for PowerPath.

DELETE /powerpath/test-assignments/{id}

Soft deletes a test assignment.
"""

from timeback.http import HttpClient
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def delete_test_assignment(
    http: HttpClient,
    assignment_id: str,
) -> None:
    """Delete a test assignment.

    DELETE /powerpath/test-assignments/{id}

    Soft deletes a test assignment by ID.
    Returns 204 No Content on success.

    Args:
        http: Injected HTTP client for making requests
        assignment_id: The test assignment sourcedId

    Returns:
        None (204 response)
    """
    path = f"/powerpath/test-assignments/{assignment_id}"

    http.delete(path)
    log.debug("Delete successful (204)")

