"""Process Response endpoint for QTI API.

POST /assessment-items/{identifier}/process-response

Process a candidate's response to an assessment item and get score + feedback.
"""

from typing import Any, Dict

from timeback.http import HttpClient
from timeback.models.request import TimebackProcessResponseRequest
from timeback.models.response import TimebackProcessResponseResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def process_response(
    http: HttpClient,
    identifier: str,
    request: TimebackProcessResponseRequest
) -> TimebackProcessResponseResponse:
    """Process a response for an assessment item.
    
    POST /assessment-items/{identifier}/process-response
    
    Validates the candidate's response against the assessment item's
    response processing rules and returns the score and feedback.
    
    Steps:
        1. Build the path with the item identifier
        2. Build the request body with response data
        3. Send POST request to process-response endpoint
        4. Parse and validate response as TimebackProcessResponseResponse
    
    Args:
        http: Injected HTTP client for making requests to the QTI API
        identifier: The unique identifier of the assessment item
        request: The request model containing:
            - identifier: Item identifier (should match path param)
            - response: Candidate's response (string or list of strings)
    
    Returns:
        TimebackProcessResponseResponse containing:
            - score: Numerical score (0.0-1.0)
            - feedback: Structured feedback with identifier and message
    
    Raises:
        HTTPError: If the request fails
        NotFoundError: If the assessment item doesn't exist
        ValidationError: If the response cannot be parsed
    
    Example:
        >>> request = TimebackProcessResponseRequest(
        ...     identifier="item-001",
        ...     response="B"
        ... )
        >>> result = process_response(http, "item-001", request)
        >>> print(f"Score: {result.score}, Feedback: {result.feedback.value}")
    """
    path = f"/assessment-items/{identifier}/process-response"
    
    # Build request body
    body: Dict[str, Any] = request.model_dump()
    
    log.debug(f"Processing response for item: {identifier}")
    
    data: Dict[str, Any] = http.post(path, json=body)
    log.debug(f"Response processed - Score: {data.get('score')}")
    
    return TimebackProcessResponseResponse.model_validate(data)

