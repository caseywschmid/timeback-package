"""Delete Test Part endpoint for QTI API.

DELETE /assessment-tests/{assessmentTestIdentifier}/test-parts/{identifier}

Delete an existing test part from an assessment test.
"""

from typing import Any, Dict, Optional

from timeback.http import HttpClient
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def delete_test_part(
    http: HttpClient,
    assessment_test_identifier: str,
    identifier: str
) -> None:
    """Delete an existing test part from an assessment test.
    
    DELETE /assessment-tests/{assessmentTestIdentifier}/test-parts/{identifier}
    
    Permanently deletes a test part and all its sections from the
    assessment test. The parent assessment test's XML is regenerated.
    This operation cannot be undone.
    
    Steps:
        1. Build the path with both identifiers
        2. Send DELETE request to the endpoint
    
    Args:
        http: Injected HTTP client for making requests to the QTI API
        assessment_test_identifier: Unique identifier of the parent assessment test
        identifier: Unique identifier of the test part to delete
    
    Returns:
        None
    
    Raises:
        HTTPError: If the request fails
        NotFoundError: If the test or test part doesn't exist
    
    Warning:
        This operation cannot be undone. All sections within the test part
        will also be deleted.
    
    Example:
        >>> delete_test_part(http, "test-001", "part-001")
        >>> print("Test part deleted")
    """
    path = f"/assessment-tests/{assessment_test_identifier}/test-parts/{identifier}"
    
    log.debug(f"Deleting test part {identifier} from test {assessment_test_identifier}")
    
    http.delete(path)
    log.debug(f"Deleted test part: {identifier}")

