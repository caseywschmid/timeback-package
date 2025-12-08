"""Get All Enrollments endpoint for OneRoster Rostering.

GET /ims/oneroster/rostering/v1p2/enrollments
"""

from typing import Any, Dict
from timeback.http import HttpClient
from timeback.models.request import TimebackGetAllEnrollmentsRequest
from timeback.models.response import TimebackGetAllEnrollmentsResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def get_all_enrollments(
    http: HttpClient, request: TimebackGetAllEnrollmentsRequest
) -> TimebackGetAllEnrollmentsResponse:
    """Fetch all enrollments (paginated list).

    GET /ims/oneroster/rostering/v1p2/enrollments
    """
    path = "/ims/oneroster/rostering/v1p2/enrollments"

    query: Dict[str, Any] = {}
    if request.query_params:
        query = request.query_params.to_query_dict()

    data: Dict[str, Any] = http.get(path, params=query)
    log.debug(f"Raw Data: {data}")
    return TimebackGetAllEnrollmentsResponse.model_validate(data)

