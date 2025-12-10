"""Search Assessment Items endpoint for QTI API.

GET /assessment-items

Search and filter assessment items with advanced filtering capabilities.
Supports text search, type filtering, sorting, and pagination.
"""

from typing import Any, Dict, Optional

from timeback.http import HttpClient
from timeback.models.request import TimebackSearchAssessmentItemsRequest
from timeback.models.response import TimebackSearchAssessmentItemsResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def search_assessment_items(
    http: HttpClient,
    request: Optional[TimebackSearchAssessmentItemsRequest] = None
) -> TimebackSearchAssessmentItemsResponse:
    """Search and filter QTI assessment items.
    
    GET /assessment-items
    
    Retrieves a paginated list of assessment items with optional filtering.
    Supports fuzzy text search across title and identifier fields,
    and advanced filtering by type.
    
    Steps:
        1. Build query parameters from request (with defaults if not provided)
        2. Send GET request to /assessment-items endpoint
        3. Parse and validate response as TimebackSearchAssessmentItemsResponse
    
    Args:
        http: Injected HTTP client for making requests to the QTI API
        request: Optional search parameters including query, pagination, sorting,
                 and filter. If not provided, defaults to page=1, limit=10, order=desc.
    
    Returns:
        TimebackSearchAssessmentItemsResponse containing:
            - items: List of TimebackQTIAssessmentItem objects
            - total: Total count of matching items
            - page: Current page number
            - pages: Total number of pages
            - limit: Items per page
            - sort: Sort field used
            - order: Sort order used
    
    Raises:
        HTTPError: If the request fails
        ValidationError: If the response cannot be parsed
    
    Example:
        >>> request = TimebackSearchAssessmentItemsRequest(
        ...     query="math",
        ...     filter="type='choice'"
        ... )
        >>> response = search_assessment_items(http, request)
        >>> for item in response.items:
        ...     print(item.identifier, item.type)
    """
    path = "/assessment-items"
    
    # Use default request if none provided
    if request is None:
        request = TimebackSearchAssessmentItemsRequest()
    
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
    
    if request.filter is not None:
        params["filter"] = request.filter
    
    log.debug(f"Searching assessment items with params: {params}")
    
    data: Dict[str, Any] = http.get(path, params=params)
    log.debug(f"Received {len(data.get('items', []))} assessment items")
    
    return TimebackSearchAssessmentItemsResponse.model_validate(data)

