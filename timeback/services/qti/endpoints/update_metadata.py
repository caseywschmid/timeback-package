"""Update Metadata endpoint for QTI API.

POST /assessment-items/metadata

Update metadata for assessment items (batch metadata update).
"""

from typing import Any, Dict

from timeback.http import HttpClient
from timeback.models.request import TimebackUpdateAssessmentItemMetadataRequest
from timeback.models.response import TimebackUpdateAssessmentItemMetadataResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def update_metadata(
    http: HttpClient,
    request: TimebackUpdateAssessmentItemMetadataRequest
) -> TimebackUpdateAssessmentItemMetadataResponse:
    """Update metadata for assessment items.
    
    POST /assessment-items/metadata
    
    This operation is used to update metadata for assessment items,
    such as resetting the human approved status. It accepts the same
    format as creating/updating assessment items.
    
    Steps:
        1. Build request body from the request model
        2. Send POST request to /assessment-items/metadata
        3. Parse and validate response as TimebackUpdateAssessmentItemMetadataResponse
    
    Args:
        http: Injected HTTP client for making requests to the QTI API
        request: The request model containing:
            - format: 'xml' (recommended) or 'json'
            - xml: QTI 3.0 XML string (when format='xml')
            - metadata: Optional metadata fields to update
    
    Returns:
        TimebackUpdateAssessmentItemMetadataResponse containing the updated item
    
    Raises:
        HTTPError: If the request fails
        ValidationError: If the response or XML cannot be parsed
    
    Example:
        >>> request = TimebackUpdateAssessmentItemMetadataRequest(
        ...     format="xml",
        ...     xml=xml_content,
        ...     metadata={"difficulty": "hard", "subject": "Math"}
        ... )
        >>> item = update_metadata(http, request)
        >>> print(f"Updated: {item.identifier}")
    """
    path = "/assessment-items/metadata"
    
    # Build request body
    body: Dict[str, Any] = request.model_dump(exclude_none=True)
    
    log.debug(f"Updating assessment item metadata with format: {request.format}")
    
    data: Dict[str, Any] = http.post(path, json=body)
    log.debug(f"Updated metadata for item: {data.get('identifier', 'unknown')}")
    
    return TimebackUpdateAssessmentItemMetadataResponse.model_validate(data)

