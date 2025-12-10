"""Search Assessment Tests endpoint for QTI API.

GET /assessment-tests

Search and filter assessment tests with advanced filtering capabilities.
"""

from typing import Any, Dict, Optional

from timeback.http import HttpClient
from timeback.models.request import TimebackSearchAssessmentTestsRequest
from timeback.models.response import TimebackSearchAssessmentTestsResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def search_assessment_tests(
    http: HttpClient,
    request: Optional[TimebackSearchAssessmentTestsRequest] = None
) -> TimebackSearchAssessmentTestsResponse:
    """Search and filter QTI assessment tests.
    
    GET /assessment-tests
    
    Retrieves a paginated list of assessment tests with optional filtering.
    Supports fuzzy text search across title and identifier fields,
    and filtering by navigation mode and submission mode.
    
    Steps:
        1. Build query parameters from request (with defaults if not provided)
        2. Send GET request to /assessment-tests endpoint
        3. Parse and validate response as TimebackSearchAssessmentTestsResponse
    
    Args:
        http: Injected HTTP client for making requests to the QTI API
        request: Optional search parameters including query, pagination, sorting,
                 navigation mode, submission mode, and filter.
                 If not provided, defaults to page=1, limit=10, order=desc.
    
    Returns:
        TimebackSearchAssessmentTestsResponse containing:
            - items: List of TimebackQTIAssessmentTest objects
            - total: Total count of matching tests
            - page: Current page number
            - pages: Total number of pages
            - limit: Items per page
            - sort: Sort field used
            - order: Sort order used
    
    Raises:
        HTTPError: If the request fails
        ValidationError: If the response cannot be parsed
    
    Example:
        >>> request = TimebackSearchAssessmentTestsRequest(
        ...     query="math",
        ...     navigation_mode=TimebackQTINavigationMode.LINEAR
        ... )
        >>> response = search_assessment_tests(http, request)
        >>> for test in response.items:
        ...     print(test.identifier, test.title)
    """
    path = "/assessment-tests"
    
    # Use default request if none provided
    if request is None:
        request = TimebackSearchAssessmentTestsRequest()
    
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
        params["sort"] = request.sort.value
    
    if request.navigation_mode is not None:
        params["navigationMode"] = request.navigation_mode.value
    
    if request.submission_mode is not None:
        params["submissionMode"] = request.submission_mode.value
    
    if request.filter is not None:
        params["filter"] = request.filter
    
    log.debug(f"Searching assessment tests with params: {params}")
    
    data: Dict[str, Any] = http.get(path, params=params)
    log.debug(f"Received {len(data.get('items', []))} assessment tests")
    
    return TimebackSearchAssessmentTestsResponse.model_validate(data)

