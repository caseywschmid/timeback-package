"""Delete Assessment Test endpoint for QTI API.

DELETE /assessment-tests/{identifier}

Permanently delete a QTI assessment test.
"""

from typing import Any, Dict, Optional

from timeback.http import HttpClient
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def delete_assessment_test(
    http: HttpClient,
    identifier: str
) -> Optional[Dict[str, Any]]:
    """Delete a QTI assessment test.
    
    DELETE /assessment-tests/{identifier}
    
    Permanently deletes an assessment test and all its associated data
    including test parts, sections, and item references. This operation
    cannot be undone. The actual assessment items referenced by this test
    are NOT deleted.
    
    Steps:
        1. Build the path with the identifier
        2. Send DELETE request to /assessment-tests/{identifier}
        3. Return None on success (HTTP 204)
    
    Args:
        http: Injected HTTP client for making requests to the QTI API
        identifier: The unique identifier of the assessment test to delete
    
    Returns:
        None if successful (HTTP 204), or a dictionary with response data
    
    Raises:
        HTTPError: If the request fails
        NotFoundError: If the assessment test doesn't exist
    
    Example:
        >>> delete_assessment_test(http, "test-001")
        >>> # Assessment test "test-001" is now deleted
    
    Warning:
        - This operation cannot be undone
        - Test parts, sections, and item references are deleted
        - The actual assessment items are NOT deleted
    """
    path = f"/assessment-tests/{identifier}"
    
    log.debug(f"Deleting assessment test: {identifier}")
    
    result = http.delete(path)
    
    log.debug(f"Deleted assessment test: {identifier}")
    
    return result

