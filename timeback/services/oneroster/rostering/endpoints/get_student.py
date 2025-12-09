"""Get Student endpoint for OneRoster Rostering.

GET /ims/oneroster/rostering/v1p2/students/{sourcedId}
"""

from typing import Any, Dict
from timeback.http import HttpClient
from timeback.models.request import TimebackGetStudentRequest
from timeback.models.response import TimebackGetUserResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="DEBUG")


def get_student(
    http: HttpClient, request: TimebackGetStudentRequest
) -> TimebackGetUserResponse:
    """Fetch a single student by sourcedId.

    GET /ims/oneroster/rostering/v1p2/students/{sourcedId}
    """
    params: Dict[str, Any] = {}
    if request.query_params:
        params = request.query_params.to_query_dict()

    log.debug(f"Sourced ID: {request.sourced_id}")

    data = http.get(
        f"/ims/oneroster/rostering/v1p2/students/{request.sourced_id}", params=params
    )

    log.debug(f"Raw Data: {data}")
    return TimebackGetUserResponse.model_validate(data)

