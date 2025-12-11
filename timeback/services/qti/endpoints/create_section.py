"""Create Section endpoint for QTI API.

POST /assessment-tests/{assessmentTestIdentifier}/test-parts/{testPartIdentifier}/sections

Create a new section within a test part.
"""

from typing import Any, Dict

from timeback.http import HttpClient
from timeback.models.request import TimebackCreateSectionRequest
from timeback.models.response import TimebackCreateSectionResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def create_section(
    http: HttpClient,
    assessment_test_identifier: str,
    test_part_identifier: str,
    request: TimebackCreateSectionRequest
) -> TimebackCreateSectionResponse:
    """Create a new section within a test part.
    
    POST /assessment-tests/{assessmentTestIdentifier}/test-parts/{testPartIdentifier}/sections
    
    Sections organize assessment items and define their presentation behavior.
    The parent assessment test's XML is automatically updated.
    
    Steps:
        1. Build the path with all identifiers
        2. Build request body from the request model
        3. Send POST request to the endpoint
        4. Parse and validate response as TimebackCreateSectionResponse
    
    Args:
        http: Injected HTTP client for making requests to the QTI API
        assessment_test_identifier: Unique identifier of the parent assessment test
        test_part_identifier: Unique identifier of the parent test part
        request: The section data including identifier, title, and visibility.
    
    Returns:
        TimebackCreateSectionResponse containing the created section
    
    Raises:
        HTTPError: If the request fails
        NotFoundError: If the test or test part doesn't exist
        ValidationError: If the response cannot be parsed
    
    Example:
        >>> request = TimebackCreateSectionRequest(
        ...     identifier="section-001",
        ...     title="Introduction Section"
        ... )
        >>> section = create_section(http, "test-001", "part-001", request)
        >>> print(f"Created: {section.identifier}")
    """
    path = f"/assessment-tests/{assessment_test_identifier}/test-parts/{test_part_identifier}/sections"
    
    # Build request body with aliases for proper serialization
    body: Dict[str, Any] = request.model_dump(exclude_none=True, by_alias=True)
    
    log.debug(f"Creating section {request.identifier} in test {assessment_test_identifier}, part {test_part_identifier}")
    
    data: Dict[str, Any] = http.post(path, json=body)
    log.debug(f"Created section: {data.get('identifier', 'unknown')}")
    
    return TimebackCreateSectionResponse.model_validate(data)

