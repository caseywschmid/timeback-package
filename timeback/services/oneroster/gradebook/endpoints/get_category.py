"""Get Category endpoint for OneRoster Gradebook.

GET /ims/oneroster/gradebook/v1p2/categories/{sourcedId}

Fetches a single category by its sourcedId.
"""

from typing import Any, Dict

from timeback.http import HttpClient
from timeback.models.request import TimebackGetCategoryRequest
from timeback.models.response import TimebackGetCategoryResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="DEBUG")


def get_category(
    http: HttpClient, request: TimebackGetCategoryRequest
) -> TimebackGetCategoryResponse:
    """Fetch a single category by sourcedId.

    GET /ims/oneroster/gradebook/v1p2/categories/{sourcedId}

    Args:
        http: Injected HTTP client for making requests
        request: Request containing sourced_id and optional query parameters

    Returns:
        TimebackGetCategoryResponse containing the category data
    """
    # Extract query params if provided
    params: Dict[str, Any] = {}
    if request.query_params:
        params = request.query_params.to_query_dict()
    
    log.debug(f"Params: {params}")
    log.debug(f"Sourced ID: {request.sourced_id}")
    
    data = http.get(
        f"/ims/oneroster/gradebook/v1p2/categories/{request.sourced_id}", params=params
    )
    
    log.debug(f"Raw Data: {data}")
    return TimebackGetCategoryResponse.model_validate(data)

