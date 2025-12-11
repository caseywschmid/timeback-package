"""Search Test Parts endpoint for QTI API.

GET /assessment-tests/{assessmentTestIdentifier}/test-parts

Search and filter test parts within an assessment test.
"""

from typing import Any, Dict, Optional

from timeback.http import HttpClient
from timeback.models.request import TimebackSearchTestPartsRequest
from timeback.models.response import TimebackSearchTestPartsResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def search_test_parts(
    http: HttpClient,
    assessment_test_identifier: str,
    request: Optional[TimebackSearchTestPartsRequest] = None
) -> TimebackSearchTestPartsResponse:
    """Search and filter test parts within an assessment test.
    
    GET /assessment-tests/{assessmentTestIdentifier}/test-parts
    
    Gets all test parts within an assessment test with support for
    filtering by navigation mode, submission mode, and text search.
    
    Steps:
        1. Build query parameters from request (with defaults if not provided)
        2. Send GET request to /assessment-tests/{id}/test-parts
        3. Parse and validate response as TimebackSearchTestPartsResponse
    
    Args:
        http: Injected HTTP client for making requests to the QTI API
        assessment_test_identifier: Unique identifier of the parent assessment test
        request: Optional search parameters including query, pagination, sorting,
                 and filters. If not provided, defaults to page=1, limit=10, order=desc.
    
    Returns:
        TimebackSearchTestPartsResponse containing:
            - items: List of TimebackQTITestPart objects
            - total: Total count of matching test parts
            - page: Current page number
            - pages: Total number of pages
            - limit: Items per page
            - sort: Sort field used
            - order: Sort order used
    
    Raises:
        HTTPError: If the request fails
        NotFoundError: If the assessment test doesn't exist
        ValidationError: If the response cannot be parsed
    
    Example:
        >>> request = TimebackSearchTestPartsRequest(
        ...     navigation_mode=TimebackQTINavigationMode.LINEAR
        ... )
        >>> response = search_test_parts(http, "test-001", request)
        >>> for part in response.items:
        ...     print(part.identifier, part.navigation_mode)
    """
    path = f"/assessment-tests/{assessment_test_identifier}/test-parts"
    
    # Use default request if none provided
    if request is None:
        request = TimebackSearchTestPartsRequest()
    
    # Build query parameters
    params: Dict[str, Any] = {
        "page": str(request.page),
        "limit": str(request.limit),
        "order": request.order.value,
    }
    
    # Add optional parameters if provided
    if request.query is not None:
        params["query"] = request.query
    
    if request.sort is not None:
        params["sort"] = request.sort
    
    if request.navigation_mode is not None:
        params["navigationMode"] = request.navigation_mode.value
    
    if request.submission_mode is not None:
        params["submissionMode"] = request.submission_mode.value
    
    if request.filter is not None:
        params["filter"] = request.filter
    
    log.debug(f"Searching test parts for test {assessment_test_identifier} with params: {params}")
    
    data: Dict[str, Any] = http.get(path, params=params)
    log.debug(f"Received {len(data.get('items', []))} test parts")
    
    return TimebackSearchTestPartsResponse.model_validate(data)

