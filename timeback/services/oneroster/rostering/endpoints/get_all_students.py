"""Get All Students endpoint for OneRoster Rostering.

GET /ims/oneroster/rostering/v1p2/students
"""

from typing import Any, Dict
from timeback.http import HttpClient
from timeback.models.request import TimebackGetAllStudentsRequest
from timeback.models.response import TimebackGetAllUsersResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def get_all_students(
    http: HttpClient, request: TimebackGetAllStudentsRequest
) -> TimebackGetAllUsersResponse:
    """Fetch all students (paginated list).

    GET /ims/oneroster/rostering/v1p2/students
    """
    path = "/ims/oneroster/rostering/v1p2/students"

    query: Dict[str, Any] = {}
    if request.query_params:
        query = request.query_params.to_query_dict()

    data: Dict[str, Any] = http.get(path, params=query)
    log.debug(f"Raw Data: {data}")
    return TimebackGetAllUsersResponse.model_validate(data)

