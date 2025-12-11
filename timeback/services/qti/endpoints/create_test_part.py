"""Create Test Part endpoint for QTI API.

POST /assessment-tests/{assessmentTestIdentifier}/test-parts

Create a new test part within an assessment test.
"""

from typing import Any, Dict

from timeback.http import HttpClient
from timeback.models.request import TimebackCreateTestPartRequest
from timeback.models.response import TimebackCreateTestPartResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def create_test_part(
    http: HttpClient,
    assessment_test_identifier: str,
    request: TimebackCreateTestPartRequest
) -> TimebackCreateTestPartResponse:
    """Create a new test part within an assessment test.
    
    POST /assessment-tests/{assessmentTestIdentifier}/test-parts
    
    Test parts organize sections and define navigation behaviors
    (linear/nonlinear) and submission modes. The assessment test's XML
    structure is automatically updated to include the new test part.
    
    Steps:
        1. Build the path with the assessment test identifier
        2. Build request body from the request model
        3. Send POST request to /assessment-tests/{id}/test-parts
        4. Parse and validate response as TimebackCreateTestPartResponse
    
    Args:
        http: Injected HTTP client for making requests to the QTI API
        assessment_test_identifier: Unique identifier of the parent assessment test
        request: The test part data including identifier, navigation mode,
                 submission mode, and at least one section.
    
    Returns:
        TimebackCreateTestPartResponse containing the created test part
    
    Raises:
        HTTPError: If the request fails
        NotFoundError: If the assessment test doesn't exist
        ValidationError: If the response cannot be parsed
    
    Example:
        >>> request = TimebackCreateTestPartRequest(
        ...     identifier="part-001",
        ...     navigation_mode=TimebackQTINavigationMode.LINEAR,
        ...     submission_mode=TimebackQTISubmissionMode.INDIVIDUAL,
        ...     qti_assessment_section=[
        ...         TimebackQTISection(identifier="section-001", title="Section 1")
        ...     ]
        ... )
        >>> part = create_test_part(http, "test-001", request)
        >>> print(f"Created: {part.identifier}")
    """
    path = f"/assessment-tests/{assessment_test_identifier}/test-parts"
    
    # Build request body with aliases for proper serialization
    body: Dict[str, Any] = request.model_dump(exclude_none=True, by_alias=True)
    
    log.debug(f"Creating test part {request.identifier} in test {assessment_test_identifier}")
    
    data: Dict[str, Any] = http.post(path, json=body)
    log.debug(f"Created test part: {data.get('identifier', 'unknown')}")
    
    return TimebackCreateTestPartResponse.model_validate(data)

