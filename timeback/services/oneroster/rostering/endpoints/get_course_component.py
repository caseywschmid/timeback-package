"""Get Course Component endpoint for OneRoster Rostering.

GET /ims/oneroster/rostering/v1p2/courses/components/{sourcedId}
"""

from typing import Any, Dict
from timeback.http import HttpClient
from timeback.models.request import TimebackGetCourseComponentRequest
from timeback.models.response import TimebackGetCourseComponentResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="DEBUG")


def get_course_component(
    http: HttpClient, request: TimebackGetCourseComponentRequest
) -> TimebackGetCourseComponentResponse:
    """Fetch a single course component by sourcedId.

    GET /ims/oneroster/rostering/v1p2/courses/components/{sourcedId}
    """
    params: Dict[str, Any] = {}
    if request.query_params:
        params = request.query_params.to_query_dict()

    log.debug(f"Sourced ID: {request.sourced_id}")

    data = http.get(
        f"/ims/oneroster/rostering/v1p2/courses/components/{request.sourced_id}", params=params
    )

    log.debug(f"Raw Data: {data}")
    return TimebackGetCourseComponentResponse.model_validate(data)

