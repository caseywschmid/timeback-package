"""Get All Classes endpoint for OneRoster Rostering.

GET /ims/oneroster/rostering/v1p2/classes

Builds the full path and query params, performs the HTTP GET via the injected
`HttpClient`, and parses the response into `TimebackGetAllClassesResponse`.
"""

from typing import Any, Dict

from timeback.http import HttpClient
from timeback.models.response import TimebackGetAllClassesResponse
from timeback.models.request import TimebackGetAllClassesRequest
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def get_all_classes(
    http: HttpClient,
    request: TimebackGetAllClassesRequest,
) -> TimebackGetAllClassesResponse:
    """Fetch a paginated list of classes.

    GET /ims/oneroster/rostering/v1p2/classes

    Args:
        http: Injected HTTP client for making requests
        request: Request containing optional query parameters

    Returns:
        TimebackGetAllClassesResponse containing paginated list of classes
    """
    path = "/ims/oneroster/rostering/v1p2/classes"

    query: Dict[str, Any] = {}
    if request.query_params:
        query = request.query_params.to_query_dict()

    data: Dict[str, Any] = http.get(path, params=query)
    log.debug(f"Raw Data: {data}")
    return TimebackGetAllClassesResponse.model_validate(data)

