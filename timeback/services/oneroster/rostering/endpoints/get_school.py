"""Get School endpoint for OneRoster Rostering.

GET /ims/oneroster/rostering/v1p2/schools/{sourcedId}

Fetches a specific school by sourcedId.
"""

from typing import Any, Dict

from timeback.http import HttpClient
from timeback.models.response import TimebackGetSchoolResponse
from timeback.models.request import TimebackGetSchoolRequest
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def get_school(http: HttpClient, request: TimebackGetSchoolRequest) -> TimebackGetSchoolResponse:
    """Fetch a single school by sourcedId.

    GET /ims/oneroster/rostering/v1p2/schools/{sourcedId}

    Args:
        http: Injected HTTP client for making requests
        request: Request containing sourced_id and optional query parameters

    Returns:
        TimebackGetSchoolResponse containing the school data
    """
    log.debug(f"Request: {request}")
    # Extract query params if provided
    params: Dict[str, Any] = {}
    if request.query_params:
        params = request.query_params.to_query_dict()
    log.debug(f"Params: {params}")
    log.debug(f"Sourced ID: {request.sourced_id}")
    data = http.get(
        f"/ims/oneroster/rostering/v1p2/schools/{request.sourced_id}", params=params
    )
    log.debug(f"Raw Data: {data}")
    return TimebackGetSchoolResponse.model_validate(data)

