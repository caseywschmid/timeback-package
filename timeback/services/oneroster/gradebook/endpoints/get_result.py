"""Get Result endpoint for OneRoster Gradebook.

GET /ims/oneroster/gradebook/v1p2/results/{sourcedId}

Fetches a single result by its sourcedId.
"""

from typing import Any, Dict

from timeback.http import HttpClient
from timeback.models.request import TimebackGetResultRequest
from timeback.models.response import TimebackGetResultResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="DEBUG")


def get_result(
    http: HttpClient, request: TimebackGetResultRequest
) -> TimebackGetResultResponse:
    """Fetch a single result by sourcedId.

    GET /ims/oneroster/gradebook/v1p2/results/{sourcedId}

    Args:
        http: Injected HTTP client for making requests
        request: Request containing sourced_id and optional query parameters

    Returns:
        TimebackGetResultResponse containing the result data
    """
    # Extract query params if provided
    params: Dict[str, Any] = {}
    if request.query_params:
        params = request.query_params.to_query_dict()
    
    log.debug(f"Params: {params}")
    log.debug(f"Sourced ID: {request.sourced_id}")
    
    data = http.get(
        f"/ims/oneroster/gradebook/v1p2/results/{request.sourced_id}", params=params
    )
    
    log.debug(f"Raw Data: {data}")
    return TimebackGetResultResponse.model_validate(data)

