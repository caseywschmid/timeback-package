"""Get Teacher endpoint for OneRoster Rostering.

GET /ims/oneroster/rostering/v1p2/teachers/{sourcedId}
"""

from typing import Any, Dict
from timeback.http import HttpClient
from timeback.models.request import TimebackGetTeacherRequest
from timeback.models.response import TimebackGetUserResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="DEBUG")


def get_teacher(
    http: HttpClient, request: TimebackGetTeacherRequest
) -> TimebackGetUserResponse:
    """Fetch a single teacher by sourcedId.

    GET /ims/oneroster/rostering/v1p2/teachers/{sourcedId}
    """
    params: Dict[str, Any] = {}
    if request.query_params:
        params = request.query_params.to_query_dict()

    log.debug(f"Sourced ID: {request.sourced_id}")

    data = http.get(
        f"/ims/oneroster/rostering/v1p2/teachers/{request.sourced_id}", params=params
    )

    log.debug(f"Raw Data: {data}")
    return TimebackGetUserResponse.model_validate(data)

