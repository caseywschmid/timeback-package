"""Get Class endpoint for OneRoster Rostering.

GET /ims/oneroster/rostering/v1p2/classes/{sourcedId}

Fetches a specific class by sourcedId.
"""

from typing import Any, Dict

from timeback.http import HttpClient
from timeback.models.response import TimebackGetClassResponse
from timeback.models.request import TimebackGetClassRequest
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def get_class(http: HttpClient, request: TimebackGetClassRequest) -> TimebackGetClassResponse:
    """Fetch a single class by sourcedId.

    GET /ims/oneroster/rostering/v1p2/classes/{sourcedId}

    Args:
        http: Injected HTTP client for making requests
        request: Request containing sourced_id and optional query parameters

    Returns:
        TimebackGetClassResponse containing the class data
    """
    log.debug(f"Request: {request}")
    # Extract query params if provided
    params: Dict[str, Any] = {}
    if request.query_params:
        params = request.query_params.to_query_dict()
    log.debug(f"Params: {params}")
    log.debug(f"Sourced ID: {request.sourced_id}")
    data = http.get(
        f"/ims/oneroster/rostering/v1p2/classes/{request.sourced_id}", params=params
    )
    log.debug(f"Raw Data: {data}")
    return TimebackGetClassResponse.model_validate(data)

