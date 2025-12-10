"""Update Assessment Test endpoint for QTI API.

PUT /assessment-tests/{identifier}

Update an existing QTI assessment test.
"""

from typing import Any, Dict

from timeback.http import HttpClient
from timeback.models.request import TimebackUpdateAssessmentTestRequest
from timeback.models.response import TimebackUpdateAssessmentTestResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def update_assessment_test(
    http: HttpClient,
    identifier: str,
    request: TimebackUpdateAssessmentTestRequest
) -> TimebackUpdateAssessmentTestResponse:
    """Update a QTI assessment test.
    
    PUT /assessment-tests/{identifier}
    
    Updates an entire assessment test by replacing its complete structure.
    This operation updates the test including its test parts, sections, and
    item references. The updated XML structure is automatically regenerated.
    
    Steps:
        1. Build the path with the identifier
        2. Build request body from the request model
        3. Send PUT request to /assessment-tests/{identifier}
        4. Parse and validate response as TimebackUpdateAssessmentTestResponse
    
    Args:
        http: Injected HTTP client for making requests to the QTI API
        identifier: The unique identifier of the assessment test to update
        request: The request model containing:
            - format: 'xml' (recommended) or 'json'
            - xml: Updated QTI 3.0 XML string (when format='xml')
            - metadata: Optional updated custom metadata
    
    Returns:
        TimebackUpdateAssessmentTestResponse containing the updated test
    
    Raises:
        HTTPError: If the request fails
        NotFoundError: If the assessment test doesn't exist
        ValidationError: If the response or XML cannot be parsed
    
    Example:
        >>> request = TimebackUpdateAssessmentTestRequest(
        ...     format="xml",
        ...     xml=updated_xml,
        ...     metadata={"subject": "Math", "version": "2.0"}
        ... )
        >>> test = update_assessment_test(http, "test-001", request)
        >>> print(f"Updated: {test.identifier}")
    """
    path = f"/assessment-tests/{identifier}"
    
    # Build request body
    body: Dict[str, Any] = request.model_dump(exclude_none=True)
    
    log.debug(f"Updating assessment test: {identifier}")
    
    data: Dict[str, Any] = http.put(path, json=body)
    log.debug(f"Updated assessment test: {data.get('identifier', 'unknown')}")
    
    return TimebackUpdateAssessmentTestResponse.model_validate(data)

