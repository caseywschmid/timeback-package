"""Get All Teachers endpoint for OneRoster Rostering.

GET /ims/oneroster/rostering/v1p2/teachers
"""

from typing import Any, Dict
from timeback.http import HttpClient
from timeback.models.request import TimebackGetAllTeachersRequest
from timeback.models.response import TimebackGetAllUsersResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def get_all_teachers(
    http: HttpClient, request: TimebackGetAllTeachersRequest
) -> TimebackGetAllUsersResponse:
    """Fetch all teachers (paginated list).

    GET /ims/oneroster/rostering/v1p2/teachers
    """
    path = "/ims/oneroster/rostering/v1p2/teachers"

    query: Dict[str, Any] = {}
    if request.query_params:
        query = request.query_params.to_query_dict()

    data: Dict[str, Any] = http.get(path, params=query)
    log.debug(f"Raw Data: {data}")
    return TimebackGetAllUsersResponse.model_validate(data)

