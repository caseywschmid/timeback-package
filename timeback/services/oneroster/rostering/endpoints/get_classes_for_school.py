"""Get Classes for School endpoint for OneRoster Rostering.

GET /ims/oneroster/rostering/v1p2/schools/{schoolSourcedId}/classes

Fetches all classes for a specific school with pagination support.
"""

from typing import Any, Dict

from timeback.http import HttpClient
from timeback.models.response import TimebackGetAllClassesResponse
from timeback.models.request import TimebackGetClassesForSchoolRequest
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def get_classes_for_school(
    http: HttpClient,
    request: TimebackGetClassesForSchoolRequest,
) -> TimebackGetAllClassesResponse:
    """Fetch a paginated list of classes for a specific school.

    GET /ims/oneroster/rostering/v1p2/schools/{schoolSourcedId}/classes

    Args:
        http: Injected HTTP client for making requests
        request: Request containing school_sourced_id and optional query parameters

    Returns:
        TimebackGetAllClassesResponse containing paginated list of classes
    """
    path = f"/ims/oneroster/rostering/v1p2/schools/{request.school_sourced_id}/classes"

    query: Dict[str, Any] = {}
    if request.query_params:
        query = request.query_params.to_query_dict()

    log.debug(f"Path: {path}")
    log.debug(f"Query params: {query}")
    data: Dict[str, Any] = http.get(path, params=query)
    log.debug(f"Raw Data: {data}")
    return TimebackGetAllClassesResponse.model_validate(data)

