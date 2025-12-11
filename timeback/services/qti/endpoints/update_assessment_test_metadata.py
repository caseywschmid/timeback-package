"""Update Assessment Test Metadata endpoint for QTI API.

PUT /assessment-tests/{identifier}/metadata

Update only the metadata fields of an assessment test.
"""

from typing import Any, Dict

from timeback.http import HttpClient
from timeback.models.request import TimebackUpdateAssessmentTestMetadataRequest
from timeback.models.response import TimebackUpdateAssessmentTestMetadataResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def update_assessment_test_metadata(
    http: HttpClient,
    identifier: str,
    request: TimebackUpdateAssessmentTestMetadataRequest
) -> TimebackUpdateAssessmentTestMetadataResponse:
    """Update only the metadata fields of an assessment test.
    
    PUT /assessment-tests/{identifier}/metadata
    
    This is a lightweight operation for administrative changes to metadata
    properties without affecting the test structure, test parts, sections,
    or assessment items.
    
    Steps:
        1. Build the path with the test identifier
        2. Build request body from the request model
        3. Send PUT request to /assessment-tests/{identifier}/metadata
        4. Parse and validate response as TimebackUpdateAssessmentTestMetadataResponse
    
    Args:
        http: Injected HTTP client for making requests to the QTI API
        identifier: The unique identifier of the assessment test to update
        request: The request model containing metadata to update
    
    Returns:
        TimebackUpdateAssessmentTestMetadataResponse containing the updated test
    
    Raises:
        HTTPError: If the request fails
        NotFoundError: If the assessment test doesn't exist
        ValidationError: If the response cannot be parsed
    
    Example:
        >>> request = TimebackUpdateAssessmentTestMetadataRequest(
        ...     metadata={"subject": "Math", "description": "Updated"}
        ... )
        >>> test = update_assessment_test_metadata(http, "test-001", request)
        >>> print(f"Updated: {test.identifier}")
    """
    path = f"/assessment-tests/{identifier}/metadata"
    
    # Build request body
    body: Dict[str, Any] = request.model_dump(exclude_none=True)
    
    log.debug(f"Updating metadata for test: {identifier}")
    
    data: Dict[str, Any] = http.put(path, json=body)
    log.debug(f"Updated metadata for test: {data.get('identifier', 'unknown')}")
    
    return TimebackUpdateAssessmentTestMetadataResponse.model_validate(data)

