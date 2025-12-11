"""Update Test Part endpoint for QTI API.

PUT /assessment-tests/{assessmentTestIdentifier}/test-parts/{identifier}

Update an existing test part within an assessment test.
"""

from typing import Any, Dict

from timeback.http import HttpClient
from timeback.models.request import TimebackUpdateTestPartRequest
from timeback.models.response import TimebackUpdateTestPartResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def update_test_part(
    http: HttpClient,
    assessment_test_identifier: str,
    identifier: str,
    request: TimebackUpdateTestPartRequest
) -> TimebackUpdateTestPartResponse:
    """Update an existing test part within an assessment test.
    
    PUT /assessment-tests/{assessmentTestIdentifier}/test-parts/{identifier}
    
    Updates a test part including its navigation mode, submission mode,
    and sections. This operation updates the entire test part structure
    and regenerates the parent assessment test's XML.
    
    Steps:
        1. Build the path with both identifiers
        2. Build request body from the request model
        3. Send PUT request to the endpoint
        4. Parse and validate response as TimebackUpdateTestPartResponse
    
    Args:
        http: Injected HTTP client for making requests to the QTI API
        assessment_test_identifier: Unique identifier of the parent assessment test
        identifier: Unique identifier of the test part to update
        request: Updated test part data including identifier, navigation mode,
                 submission mode, and sections.
    
    Returns:
        TimebackUpdateTestPartResponse containing the updated test part
    
    Raises:
        HTTPError: If the request fails
        NotFoundError: If the test or test part doesn't exist
        ValidationError: If the response cannot be parsed
    
    Example:
        >>> request = TimebackUpdateTestPartRequest(
        ...     identifier="part-001",
        ...     navigation_mode=TimebackQTINavigationMode.NONLINEAR,
        ...     submission_mode=TimebackQTISubmissionMode.SIMULTANEOUS,
        ...     qti_assessment_section=[
        ...         TimebackQTISection(identifier="section-001", title="Updated Section")
        ...     ]
        ... )
        >>> part = update_test_part(http, "test-001", "part-001", request)
        >>> print(f"Updated: {part.identifier}")
    """
    path = f"/assessment-tests/{assessment_test_identifier}/test-parts/{identifier}"
    
    # Build request body with aliases for proper serialization
    body: Dict[str, Any] = request.model_dump(exclude_none=True, by_alias=True)
    
    log.debug(f"Updating test part {identifier} in test {assessment_test_identifier}")
    
    data: Dict[str, Any] = http.put(path, json=body)
    log.debug(f"Updated test part: {data.get('identifier', 'unknown')}")
    
    return TimebackUpdateTestPartResponse.model_validate(data)

