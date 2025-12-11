"""Get Section endpoint for QTI API.

GET /assessment-tests/{assessmentTestIdentifier}/test-parts/{testPartIdentifier}/sections/{identifier}

Retrieve a specific section by identifier.
"""

from typing import Any, Dict

from timeback.http import HttpClient
from timeback.models.response import TimebackGetSectionResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def get_section(
    http: HttpClient,
    assessment_test_identifier: str,
    test_part_identifier: str,
    identifier: str
) -> TimebackGetSectionResponse:
    """Retrieve a specific section by identifier.
    
    GET /assessment-tests/{assessmentTestIdentifier}/test-parts/{testPartIdentifier}/sections/{identifier}
    
    Retrieves a section including all its assessment item references,
    presentation settings, and configuration.
    
    Steps:
        1. Build the path with all identifiers
        2. Send GET request to the endpoint
        3. Parse and validate response as TimebackGetSectionResponse
    
    Args:
        http: Injected HTTP client for making requests to the QTI API
        assessment_test_identifier: Unique identifier of the parent assessment test
        test_part_identifier: Unique identifier of the parent test part
        identifier: Unique identifier of the section to retrieve
    
    Returns:
        TimebackGetSectionResponse containing the section with:
            - identifier: Section identifier
            - title: Human-readable title
            - visible: Whether section is visible to candidates
            - qti_assessment_item_ref: List of item references
    
    Raises:
        HTTPError: If the request fails
        NotFoundError: If the test, test part, or section doesn't exist
        ValidationError: If the response cannot be parsed
    
    Example:
        >>> section = get_section(http, "test-001", "part-001", "section-001")
        >>> print(f"Section: {section.title}")
        >>> for item in section.qti_assessment_item_ref:
        ...     print(f"  Item: {item.identifier}")
    """
    path = f"/assessment-tests/{assessment_test_identifier}/test-parts/{test_part_identifier}/sections/{identifier}"
    
    log.debug(f"Getting section {identifier} in test {assessment_test_identifier}, part {test_part_identifier}")
    
    data: Dict[str, Any] = http.get(path)
    log.debug(f"Retrieved section: {data.get('identifier', 'unknown')}")
    
    return TimebackGetSectionResponse.model_validate(data)

