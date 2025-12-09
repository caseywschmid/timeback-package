"""Get Classes for User endpoint for OneRoster Rostering.

GET /ims/oneroster/rostering/v1p2/users/{userSourcedId}/classes
"""

from typing import Any, Dict
from timeback.http import HttpClient
from timeback.models.request import TimebackGetClassesForUserRequest
from timeback.models.response import TimebackGetAllClassesResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def get_classes_for_user(
    http: HttpClient, request: TimebackGetClassesForUserRequest
) -> TimebackGetAllClassesResponse:
    """Fetch classes for a specific user.

    GET /ims/oneroster/rostering/v1p2/users/{userSourcedId}/classes
    """
    path = f"/ims/oneroster/rostering/v1p2/users/{request.user_sourced_id}/classes"

    query: Dict[str, Any] = {}
    if request.query_params:
        query = request.query_params.to_query_dict()

    data: Dict[str, Any] = http.get(path, params=query)
    log.debug(f"Raw Data: {data}")
    return TimebackGetAllClassesResponse.model_validate(data)

