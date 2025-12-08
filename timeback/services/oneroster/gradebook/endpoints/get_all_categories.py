"""Get All Categories endpoint for OneRoster Gradebook.

GET /ims/oneroster/gradebook/v1p2/categories

Fetches all categories with pagination support.
"""

from typing import Any, Dict

from timeback.http import HttpClient
from timeback.models.response import TimebackGetAllCategoriesResponse
from timeback.models.request import TimebackGetAllCategoriesRequest
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def get_all_categories(
    http: HttpClient,
    request: TimebackGetAllCategoriesRequest,
) -> TimebackGetAllCategoriesResponse:
    """Fetch a paginated list of categories.

    GET /ims/oneroster/gradebook/v1p2/categories

    Args:
        http: Injected HTTP client for making requests
        request: Request containing optional query parameters

    Returns:
        TimebackGetAllCategoriesResponse containing paginated list of categories
    """
    path = "/ims/oneroster/gradebook/v1p2/categories"

    query: Dict[str, Any] = {}
    if request.query_params:
        query = request.query_params.to_query_dict()

    log.debug(f"Path: {path}")
    log.debug(f"Query params: {query}")
    data: Dict[str, Any] = http.get(path, params=query)
    log.debug(f"Raw Data: {data}")
    return TimebackGetAllCategoriesResponse.model_validate(data)

