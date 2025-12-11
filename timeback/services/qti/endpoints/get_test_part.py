"""Get Test Part endpoint for QTI API.

GET /assessment-tests/{assessmentTestIdentifier}/test-parts/{identifier}

Retrieve a specific test part by identifier.
"""

from typing import Any, Dict

from timeback.http import HttpClient
from timeback.models.response import TimebackGetTestPartResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def get_test_part(
    http: HttpClient,
    assessment_test_identifier: str,
    identifier: str
) -> TimebackGetTestPartResponse:
    """Retrieve a specific test part by identifier.
    
    GET /assessment-tests/{assessmentTestIdentifier}/test-parts/{identifier}
    
    Retrieves a test part including all its sections and their assessment
    item references. Test parts define navigation and submission behaviors
    for groups of sections.
    
    Steps:
        1. Build the path with both identifiers
        2. Send GET request to the endpoint
        3. Parse and validate response as TimebackGetTestPartResponse
    
    Args:
        http: Injected HTTP client for making requests to the QTI API
        assessment_test_identifier: Unique identifier of the parent assessment test
        identifier: Unique identifier of the test part to retrieve
    
    Returns:
        TimebackGetTestPartResponse containing the test part with:
            - identifier: Test part identifier
            - navigation_mode: Linear or nonlinear navigation
            - submission_mode: Individual or simultaneous submission
            - qti_assessment_section: List of sections in this part
    
    Raises:
        HTTPError: If the request fails
        NotFoundError: If the test or test part doesn't exist
        ValidationError: If the response cannot be parsed
    
    Example:
        >>> part = get_test_part(http, "test-001", "part-001")
        >>> print(f"Part: {part.identifier}")
        >>> print(f"Sections: {len(part.qti_assessment_section)}")
    """
    path = f"/assessment-tests/{assessment_test_identifier}/test-parts/{identifier}"
    
    log.debug(f"Getting test part {identifier} from test {assessment_test_identifier}")
    
    data: Dict[str, Any] = http.get(path)
    log.debug(f"Retrieved test part: {data.get('identifier', 'unknown')}")
    
    return TimebackGetTestPartResponse.model_validate(data)

