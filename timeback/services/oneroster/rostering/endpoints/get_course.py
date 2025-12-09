"""Get Course endpoint for OneRoster Rostering.

GET /ims/oneroster/rostering/v1p2/courses/{sourcedId}
"""

from typing import Any, Dict
from timeback.http import HttpClient
from timeback.models.request import TimebackGetCourseRequest
from timeback.models.response import TimebackGetCourseResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="DEBUG")


def get_course(
    http: HttpClient, request: TimebackGetCourseRequest
) -> TimebackGetCourseResponse:
    """Fetch a single course by sourcedId.

    GET /ims/oneroster/rostering/v1p2/courses/{sourcedId}
    """
    params: Dict[str, Any] = {}
    if request.query_params:
        params = request.query_params.to_query_dict()

    log.debug(f"Sourced ID: {request.sourced_id}")

    data = http.get(
        f"/ims/oneroster/rostering/v1p2/courses/{request.sourced_id}", params=params
    )

    log.debug(f"Raw Data: {data}")
    return TimebackGetCourseResponse.model_validate(data)

