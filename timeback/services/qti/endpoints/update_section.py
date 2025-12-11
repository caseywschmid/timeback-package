"""Update Section endpoint for QTI API.

PUT /assessment-tests/{assessmentTestIdentifier}/test-parts/{testPartIdentifier}/sections/{identifier}

Update an existing section within a test part.
"""

from typing import Any, Dict

from timeback.http import HttpClient
from timeback.models.request import TimebackUpdateSectionRequest
from timeback.models.response import TimebackUpdateSectionResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def update_section(
    http: HttpClient,
    assessment_test_identifier: str,
    test_part_identifier: str,
    identifier: str,
    request: TimebackUpdateSectionRequest
) -> TimebackUpdateSectionResponse:
    """Update an existing section within a test part.
    
    PUT /assessment-tests/{assessmentTestIdentifier}/test-parts/{testPartIdentifier}/sections/{identifier}
    
    Updates a section including its title, visibility, and item references.
    The parent assessment test's XML is automatically regenerated.
    
    Steps:
        1. Build the path with all identifiers
        2. Build request body from the request model
        3. Send PUT request to the endpoint
        4. Parse and validate response as TimebackUpdateSectionResponse
    
    Args:
        http: Injected HTTP client for making requests to the QTI API
        assessment_test_identifier: Unique identifier of the parent assessment test
        test_part_identifier: Unique identifier of the parent test part
        identifier: Unique identifier of the section to update
        request: Updated section data.
    
    Returns:
        TimebackUpdateSectionResponse containing the updated section
    
    Raises:
        HTTPError: If the request fails
        NotFoundError: If the test, test part, or section doesn't exist
        ValidationError: If the response cannot be parsed
    
    Example:
        >>> request = TimebackUpdateSectionRequest(
        ...     identifier="section-001",
        ...     title="Updated Section Title"
        ... )
        >>> section = update_section(http, "test-001", "part-001", "section-001", request)
        >>> print(f"Updated: {section.title}")
    """
    path = f"/assessment-tests/{assessment_test_identifier}/test-parts/{test_part_identifier}/sections/{identifier}"
    
    # Build request body with aliases for proper serialization
    body: Dict[str, Any] = request.model_dump(exclude_none=True, by_alias=True)
    
    log.debug(f"Updating section {identifier} in test {assessment_test_identifier}, part {test_part_identifier}")
    
    data: Dict[str, Any] = http.put(path, json=body)
    log.debug(f"Updated section: {data.get('identifier', 'unknown')}")
    
    return TimebackUpdateSectionResponse.model_validate(data)

