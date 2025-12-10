"""Update Assessment Item endpoint for QTI API.

PUT /assessment-items/{identifier}

Update an existing QTI assessment item's content and configuration.
"""

from typing import Any, Dict

from timeback.http import HttpClient
from timeback.models.request import TimebackUpdateAssessmentItemRequest
from timeback.models.response import TimebackUpdateAssessmentItemResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def update_assessment_item(
    http: HttpClient,
    identifier: str,
    request: TimebackUpdateAssessmentItemRequest
) -> TimebackUpdateAssessmentItemResponse:
    """Update a QTI assessment item.
    
    PUT /assessment-items/{identifier}
    
    Updates an existing assessment item including its question content,
    interactions, response processing, and scoring logic. This operation
    regenerates the QTI XML structure and validates all content.
    
    Steps:
        1. Build the path with the identifier
        2. Build request body from the request model
        3. Send PUT request to /assessment-items/{identifier}
        4. Parse and validate response as TimebackUpdateAssessmentItemResponse
    
    Args:
        http: Injected HTTP client for making requests to the QTI API
        identifier: The unique identifier of the assessment item to update
        request: The request model containing:
            - format: 'xml' (recommended) or 'json'
            - xml: Updated QTI 3.0 XML string (when format='xml')
            - metadata: Optional updated custom metadata
    
    Returns:
        TimebackUpdateAssessmentItemResponse containing the updated item
    
    Raises:
        HTTPError: If the request fails
        NotFoundError: If the assessment item doesn't exist
        ValidationError: If the response or XML cannot be parsed
    
    Example:
        >>> request = TimebackUpdateAssessmentItemRequest(
        ...     format="xml",
        ...     xml=updated_xml,
        ...     metadata={"difficulty": "hard"}
        ... )
        >>> item = update_assessment_item(http, "item-001", request)
        >>> print(f"Updated: {item.identifier}")
    """
    path = f"/assessment-items/{identifier}"
    
    # Build request body
    body: Dict[str, Any] = request.model_dump(exclude_none=True)
    
    log.debug(f"Updating assessment item: {identifier}")
    
    data: Dict[str, Any] = http.put(path, json=body)
    log.debug(f"Updated assessment item: {data.get('identifier', 'unknown')}")
    
    return TimebackUpdateAssessmentItemResponse.model_validate(data)

