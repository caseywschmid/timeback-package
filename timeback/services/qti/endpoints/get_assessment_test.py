"""Get Assessment Test endpoint for QTI API.

GET /assessment-tests/{identifier}

Retrieve a complete assessment test with its full structure.
"""

from typing import Any, Dict

from timeback.http import HttpClient
from timeback.models.response import TimebackGetAssessmentTestResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def get_assessment_test(
    http: HttpClient,
    identifier: str
) -> TimebackGetAssessmentTestResponse:
    """Get a specific QTI assessment test by identifier.
    
    GET /assessment-tests/{identifier}
    
    Retrieves a complete assessment test including all its test parts,
    sections, and assessment item references. This provides the full
    hierarchical structure needed to understand the test organization and flow.
    
    Steps:
        1. Build the path with the identifier
        2. Send GET request to /assessment-tests/{identifier}
        3. Parse and validate response as TimebackGetAssessmentTestResponse
    
    Args:
        http: Injected HTTP client for making requests to the QTI API
        identifier: The unique identifier of the assessment test to retrieve
    
    Returns:
        TimebackGetAssessmentTestResponse containing the full assessment test:
            - identifier: Unique identifier
            - title: Human-readable title
            - qti_test_part: List of test parts with sections
            - qti_outcome_declaration: Outcome variable declarations
            - time_limit: Time limit in seconds
            - max_attempts: Maximum attempts
            - metadata: Custom metadata
            - raw_xml: Complete QTI XML representation
    
    Raises:
        HTTPError: If the request fails
        NotFoundError: If the assessment test doesn't exist
        ValidationError: If the response cannot be parsed
    
    Example:
        >>> test = get_assessment_test(http, "test-001")
        >>> print(f"Title: {test.title}, Parts: {len(test.qti_test_part)}")
    """
    path = f"/assessment-tests/{identifier}"
    
    log.debug(f"Getting assessment test: {identifier}")
    
    data: Dict[str, Any] = http.get(path)
    log.debug(f"Retrieved assessment test: {data.get('identifier', 'unknown')}")
    
    return TimebackGetAssessmentTestResponse.model_validate(data)

