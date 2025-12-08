"""Get Teachers for Class endpoint for OneRoster Rostering.

GET /ims/oneroster/rostering/v1p2/classes/{classSourcedId}/teachers
"""

from typing import Any, Dict
from timeback.http import HttpClient
from timeback.models.request import TimebackGetTeachersForClassRequest
from timeback.models.response import TimebackGetAllUsersResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def get_teachers_for_class(
    http: HttpClient, request: TimebackGetTeachersForClassRequest
) -> TimebackGetAllUsersResponse:
    """Fetch teachers for a specific class.

    GET /ims/oneroster/rostering/v1p2/classes/{classSourcedId}/teachers
    """
    path = f"/ims/oneroster/rostering/v1p2/classes/{request.class_sourced_id}/teachers"

    query: Dict[str, Any] = {}
    if request.query_params:
        query = request.query_params.to_query_dict()

    data: Dict[str, Any] = http.get(path, params=query)
    log.debug(f"Raw Data: {data}")
    return TimebackGetAllUsersResponse.model_validate(data)

