"""Create Assessment Test endpoint for QTI API.

POST /assessment-tests

Create a new QTI assessment test.
"""

from typing import Any, Dict

from timeback.http import HttpClient
from timeback.models.request import TimebackCreateAssessmentTestRequest
from timeback.models.response import TimebackCreateAssessmentTestResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def create_assessment_test(
    http: HttpClient,
    request: TimebackCreateAssessmentTestRequest
) -> TimebackCreateAssessmentTestResponse:
    """Create a new QTI assessment test.
    
    POST /assessment-tests
    
    Creates a new assessment test on the service provider.
    Supports both JSON and XML formats. The recommended approach is
    to send format='xml' with QTI XML content.
    
    Steps:
        1. Build request body from the request model
        2. Send POST request to /assessment-tests
        3. Parse and validate response as TimebackCreateAssessmentTestResponse
    
    Args:
        http: Injected HTTP client for making requests to the QTI API
        request: The request model containing:
            - format: 'xml' (recommended) or 'json'
            - xml: QTI 3.0 XML string (when format='xml')
            - metadata: Optional custom metadata
    
    Returns:
        TimebackCreateAssessmentTestResponse containing the created test
    
    Raises:
        HTTPError: If the request fails
        ValidationError: If the response or XML cannot be parsed
    
    Example:
        >>> xml = '''<?xml version="1.0"?>
        ... <qti-assessment-test identifier="test-1" title="Math Test">
        ...   <!-- QTI content -->
        ... </qti-assessment-test>'''
        >>> request = TimebackCreateAssessmentTestRequest(
        ...     format="xml",
        ...     xml=xml,
        ...     metadata={"subject": "Math"}
        ... )
        >>> test = create_assessment_test(http, request)
        >>> print(f"Created: {test.identifier}")
    """
    path = "/assessment-tests"
    
    # Build request body
    body: Dict[str, Any] = request.model_dump(exclude_none=True)
    
    log.debug(f"Creating assessment test with format: {request.format}")
    
    data: Dict[str, Any] = http.post(path, json=body)
    log.debug(f"Created assessment test: {data.get('identifier', 'unknown')}")
    
    return TimebackCreateAssessmentTestResponse.model_validate(data)

