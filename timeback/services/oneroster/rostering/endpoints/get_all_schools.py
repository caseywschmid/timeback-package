"""Get All Schools endpoint for OneRoster Rostering.

GET /ims/oneroster/rostering/v1p2/schools

Fetches a paginated list of schools (organizations).
"""

from typing import Any, Dict

from timeback.http import HttpClient
from timeback.models.request import TimebackGetAllSchoolsRequest
from timeback.models.response import TimebackGetAllSchoolsResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="DEBUG")


def get_all_schools(
    http: HttpClient, request: TimebackGetAllSchoolsRequest
) -> TimebackGetAllSchoolsResponse:
    """Fetch a paginated list of schools.

    GET /ims/oneroster/rostering/v1p2/schools

    Args:
        http: Injected HTTP client for making requests
        request: Request containing optional query parameters

    Returns:
        TimebackGetAllSchoolsResponse containing the schools list and pagination info
    """
    # Extract query params if provided
    params: Dict[str, Any] = {}
    if request.query_params:
        params = request.query_params.to_query_dict()
    
    log.debug(f"Params: {params}")
    
    data = http.get(
        "/ims/oneroster/rostering/v1p2/schools",
        params=params,
    )
    
    log.debug(f"Raw Data: {data}")
    return TimebackGetAllSchoolsResponse.model_validate(data)
