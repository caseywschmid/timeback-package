"""Create Assessment Item endpoint for QTI API.

POST /assessment-items

Create a new QTI 3.0 assessment item, preferably from XML.
"""

from typing import Any, Dict

from timeback.http import HttpClient
from timeback.models.request import TimebackCreateAssessmentItemRequest
from timeback.models.response import TimebackCreateAssessmentItemResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def create_assessment_item(
    http: HttpClient,
    request: TimebackCreateAssessmentItemRequest
) -> TimebackCreateAssessmentItemResponse:
    """Create a new QTI assessment item.
    
    POST /assessment-items
    
    Creates a new assessment item on the service provider.
    The recommended approach is to send format='xml' with QTI XML content.
    The XML is validated against IMS QTI XSDs.
    
    Steps:
        1. Build request body from the request model
        2. Send POST request to /assessment-items
        3. Parse and validate response as TimebackCreateAssessmentItemResponse
    
    Args:
        http: Injected HTTP client for making requests to the QTI API
        request: The request model containing:
            - format: 'xml' (recommended) or 'json'
            - xml: QTI 3.0 XML string (when format='xml')
            - metadata: Optional custom metadata
    
    Returns:
        TimebackCreateAssessmentItemResponse containing the created item
    
    Raises:
        HTTPError: If the request fails
        ValidationError: If the response or XML cannot be parsed
    
    Example:
        >>> xml = '''<?xml version="1.0"?>
        ... <qti-assessment-item identifier="item-1" title="Test">
        ...   <!-- QTI content -->
        ... </qti-assessment-item>'''
        >>> request = TimebackCreateAssessmentItemRequest(
        ...     format="xml",
        ...     xml=xml,
        ...     metadata={"subject": "Math", "grade": "5"}
        ... )
        >>> item = create_assessment_item(http, request)
        >>> print(f"Created: {item.identifier}")
    """
    path = "/assessment-items"
    
    # Build request body
    body: Dict[str, Any] = request.model_dump(exclude_none=True)
    
    log.debug(f"Creating assessment item with format: {request.format}")
    
    data: Dict[str, Any] = http.post(path, json=body)
    log.debug(f"Created assessment item: {data.get('identifier', 'unknown')}")
    
    return TimebackCreateAssessmentItemResponse.model_validate(data)

