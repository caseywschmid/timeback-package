"""Search Sections endpoint for QTI API.

GET /assessment-tests/{assessmentTestIdentifier}/test-parts/{testPartIdentifier}/sections

Search and filter sections within a test part.
"""

from typing import Any, Dict, Optional

from timeback.http import HttpClient
from timeback.models.request import TimebackSearchSectionsRequest
from timeback.models.response import TimebackSearchSectionsResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def search_sections(
    http: HttpClient,
    assessment_test_identifier: str,
    test_part_identifier: str,
    request: Optional[TimebackSearchSectionsRequest] = None
) -> TimebackSearchSectionsResponse:
    """Search and filter sections within a test part.
    
    GET /assessment-tests/{assessmentTestIdentifier}/test-parts/{testPartIdentifier}/sections
    
    Gets all sections within a specific test part with support for
    text search, sorting, and pagination.
    
    Steps:
        1. Build query parameters from request (with defaults if not provided)
        2. Send GET request to the endpoint
        3. Parse and validate response as TimebackSearchSectionsResponse
    
    Args:
        http: Injected HTTP client for making requests to the QTI API
        assessment_test_identifier: Unique identifier of the parent assessment test
        test_part_identifier: Unique identifier of the parent test part
        request: Optional search parameters including query, pagination, and sorting.
                 If not provided, defaults to page=1, limit=10, order=desc.
    
    Returns:
        TimebackSearchSectionsResponse containing:
            - items: List of TimebackQTISection objects
            - total: Total count of matching sections
            - page: Current page number
            - pages: Total number of pages
            - limit: Items per page
            - sort: Sort field used
            - order: Sort order used
    
    Raises:
        HTTPError: If the request fails
        NotFoundError: If the test or test part doesn't exist
        ValidationError: If the response cannot be parsed
    
    Example:
        >>> request = TimebackSearchSectionsRequest(query="intro")
        >>> response = search_sections(http, "test-001", "part-001", request)
        >>> for section in response.items:
        ...     print(section.identifier, section.title)
    """
    path = f"/assessment-tests/{assessment_test_identifier}/test-parts/{test_part_identifier}/sections"
    
    # Use default request if none provided
    if request is None:
        request = TimebackSearchSectionsRequest()
    
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
    
    log.debug(f"Searching sections in test {assessment_test_identifier}, part {test_part_identifier}")
    
    data: Dict[str, Any] = http.get(path, params=params)
    log.debug(f"Received {len(data.get('items', []))} sections")
    
    return TimebackSearchSectionsResponse.model_validate(data)

