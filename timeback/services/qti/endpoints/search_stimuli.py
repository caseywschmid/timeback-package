"""Search Stimuli endpoint for QTI API.

GET /stimuli

Search and filter stimuli with advanced filtering capabilities.
Supports text search across titles and identifiers, sorting, and pagination.
"""

from typing import Any, Dict, Optional

from timeback.http import HttpClient
from timeback.models.request import TimebackSearchStimuliRequest
from timeback.models.response import TimebackSearchStimuliResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def search_stimuli(
    http: HttpClient,
    request: Optional[TimebackSearchStimuliRequest] = None
) -> TimebackSearchStimuliResponse:
    """Search and filter QTI stimuli.
    
    GET /stimuli
    
    Retrieves a paginated list of stimuli with optional filtering.
    Supports fuzzy text search across title and identifier fields.
    
    Steps:
        1. Build query parameters from request (with defaults if not provided)
        2. Send GET request to /stimuli endpoint
        3. Parse and validate response as TimebackSearchStimuliResponse
    
    Args:
        http: Injected HTTP client for making requests to the QTI API
        request: Optional search parameters including query, pagination, and sorting.
                 If not provided, defaults to page=1, limit=10, order=desc.
    
    Returns:
        TimebackSearchStimuliResponse containing:
            - items: List of TimebackQTIStimulus objects
            - total: Total count of matching stimuli
            - page: Current page number
            - pages: Total number of pages
            - limit: Items per page
            - sort: Sort field used
            - order: Sort order used
    
    Raises:
        HTTPError: If the request fails
        ValidationError: If the response cannot be parsed
    """
    path = "/stimuli"
    
    # Use default request if none provided
    if request is None:
        request = TimebackSearchStimuliRequest()
    
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
    
    log.debug(f"Searching stimuli with params: {params}")
    
    data: Dict[str, Any] = http.get(path, params=params)
    log.debug(f"Received {len(data.get('items', []))} stimuli")
    
    return TimebackSearchStimuliResponse.model_validate(data)

