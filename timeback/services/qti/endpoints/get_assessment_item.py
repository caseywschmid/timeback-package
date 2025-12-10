"""Get Assessment Item endpoint for QTI API.

GET /assessment-items/{identifier}

Retrieve a specific assessment item with its complete content.
"""

from typing import Any, Dict

from timeback.http import HttpClient
from timeback.models.response import TimebackGetAssessmentItemResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def get_assessment_item(
    http: HttpClient,
    identifier: str
) -> TimebackGetAssessmentItemResponse:
    """Get a specific QTI assessment item by identifier.
    
    GET /assessment-items/{identifier}
    
    Retrieves a complete assessment item including its question content,
    answer choices, interaction types, response processing rules, and
    scoring logic.
    
    Steps:
        1. Build the path with the identifier
        2. Send GET request to /assessment-items/{identifier}
        3. Parse and validate response as TimebackGetAssessmentItemResponse
    
    Args:
        http: Injected HTTP client for making requests to the QTI API
        identifier: The unique identifier of the assessment item to retrieve
    
    Returns:
        TimebackGetAssessmentItemResponse containing the full assessment item:
            - identifier: Unique identifier
            - title: Human-readable title
            - type: Interaction type (choice, text-entry, etc.)
            - qtiVersion: QTI version
            - responseDeclarations: Response variable definitions
            - outcomeDeclarations: Outcome variable definitions
            - responseProcessing: Scoring/feedback logic
            - metadata: Custom metadata
            - rawXml: Complete QTI XML representation
    
    Raises:
        HTTPError: If the request fails
        NotFoundError: If the assessment item doesn't exist
        ValidationError: If the response cannot be parsed
    
    Example:
        >>> item = get_assessment_item(http, "item-001")
        >>> print(f"Title: {item.title}, Type: {item.type}")
    """
    path = f"/assessment-items/{identifier}"
    
    log.debug(f"Getting assessment item: {identifier}")
    
    data: Dict[str, Any] = http.get(path)
    log.debug(f"Retrieved assessment item: {data.get('identifier', 'unknown')}")
    
    return TimebackGetAssessmentItemResponse.model_validate(data)

