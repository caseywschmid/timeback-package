"""Get Teachers for School endpoint for OneRoster Rostering.

GET /ims/oneroster/rostering/v1p2/schools/{schoolSourcedId}/teachers
"""

from typing import Any, Dict
from timeback.http import HttpClient
from timeback.models.request import TimebackGetTeachersForSchoolRequest
from timeback.models.response import TimebackGetAllUsersResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def get_teachers_for_school(
    http: HttpClient, request: TimebackGetTeachersForSchoolRequest
) -> TimebackGetAllUsersResponse:
    """Fetch teachers for a specific school.

    GET /ims/oneroster/rostering/v1p2/schools/{schoolSourcedId}/teachers
    """
    path = f"/ims/oneroster/rostering/v1p2/schools/{request.school_sourced_id}/teachers"

    query: Dict[str, Any] = {}
    if request.query_params:
        query = request.query_params.to_query_dict()

    data: Dict[str, Any] = http.get(path, params=query)
    log.debug(f"Raw Data: {data}")
    return TimebackGetAllUsersResponse.model_validate(data)

