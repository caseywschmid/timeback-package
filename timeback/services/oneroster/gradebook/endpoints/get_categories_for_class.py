"""Get Categories for Class endpoint for OneRoster Gradebook.

GET /ims/oneroster/gradebook/v1p2/classes/{sourcedId}/categories

Builds the full path and query params, performs the HTTP GET via the injected
`HttpClient`, and parses the response into `TimebackGetAllCategoriesResponse`.
"""

from typing import Any, Dict

from timeback.http import HttpClient
from timeback.models.response import TimebackGetAllCategoriesResponse
from timeback.models.request import TimebackGetCategoriesForClassRequest
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def get_categories_for_class(
    http: HttpClient,
    request: TimebackGetCategoriesForClassRequest,
) -> TimebackGetAllCategoriesResponse:
    """Fetch a paginated list of categories for a specific class.

    GET /ims/oneroster/gradebook/v1p2/classes/{sourcedId}/categories

    Args:
        http: Injected HTTP client for making requests
        request: Request containing class_sourced_id and optional query parameters

    Returns:
        TimebackGetAllCategoriesResponse containing paginated list of categories
    """
    path = f"/ims/oneroster/gradebook/v1p2/classes/{request.class_sourced_id}/categories"

    query: Dict[str, Any] = {}
    if request.query_params:
        query = request.query_params.to_query_dict()

    data: Dict[str, Any] = http.get(path, params=query)
    log.debug(f"Raw Data: {data}")
    return TimebackGetAllCategoriesResponse.model_validate(data)

