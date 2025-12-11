"""Delete Section endpoint for QTI API.

DELETE /assessment-tests/{assessmentTestIdentifier}/test-parts/{testPartIdentifier}/sections/{identifier}

Delete an existing section from a test part.
"""

from timeback.http import HttpClient
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def delete_section(
    http: HttpClient,
    assessment_test_identifier: str,
    test_part_identifier: str,
    identifier: str
) -> None:
    """Delete an existing section from a test part.
    
    DELETE /assessment-tests/{assessmentTestIdentifier}/test-parts/{testPartIdentifier}/sections/{identifier}
    
    Permanently deletes a section and all its item references from the
    test part. The parent assessment test's XML is regenerated.
    This operation cannot be undone.
    
    Steps:
        1. Build the path with all identifiers
        2. Send DELETE request to the endpoint
    
    Args:
        http: Injected HTTP client for making requests to the QTI API
        assessment_test_identifier: Unique identifier of the parent assessment test
        test_part_identifier: Unique identifier of the parent test part
        identifier: Unique identifier of the section to delete
    
    Returns:
        None
    
    Raises:
        HTTPError: If the request fails
        NotFoundError: If the test, test part, or section doesn't exist
    
    Warning:
        This operation cannot be undone. Item references within the section
        will be removed, but the actual assessment items are NOT deleted.
    
    Example:
        >>> delete_section(http, "test-001", "part-001", "section-001")
        >>> print("Section deleted")
    """
    path = f"/assessment-tests/{assessment_test_identifier}/test-parts/{test_part_identifier}/sections/{identifier}"
    
    log.debug(f"Deleting section {identifier} from test {assessment_test_identifier}, part {test_part_identifier}")
    
    http.delete(path)
    log.debug(f"Deleted section: {identifier}")

