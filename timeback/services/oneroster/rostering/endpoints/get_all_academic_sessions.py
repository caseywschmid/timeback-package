"""Get All Academic Sessions endpoint for OneRoster Rostering.

GET /ims/oneroster/rostering/v1p2/academicSessions
"""

from typing import Any, Dict
from timeback.http import HttpClient
from timeback.models.request import TimebackGetAllAcademicSessionsRequest
from timeback.models.response import TimebackGetAllAcademicSessionsResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def get_all_academic_sessions(
    http: HttpClient, request: TimebackGetAllAcademicSessionsRequest
) -> TimebackGetAllAcademicSessionsResponse:
    """Fetch all academic sessions (paginated list).

    GET /ims/oneroster/rostering/v1p2/academicSessions
    """
    path = "/ims/oneroster/rostering/v1p2/academicSessions"

    query: Dict[str, Any] = {}
    if request.query_params:
        query = request.query_params.to_query_dict()

    data: Dict[str, Any] = http.get(path, params=query)
    log.debug(f"Raw Data: {data}")
    return TimebackGetAllAcademicSessionsResponse.model_validate(data)

