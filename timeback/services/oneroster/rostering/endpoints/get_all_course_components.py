"""Get All Course Components endpoint for OneRoster Rostering.

GET /ims/oneroster/rostering/v1p2/courses/components
"""

from typing import Any, Dict
from timeback.http import HttpClient
from timeback.models.request import TimebackGetAllCourseComponentsRequest
from timeback.models.response import TimebackGetAllCourseComponentsResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def get_all_course_components(
    http: HttpClient, request: TimebackGetAllCourseComponentsRequest
) -> TimebackGetAllCourseComponentsResponse:
    """Fetch all course components (paginated list).

    GET /ims/oneroster/rostering/v1p2/courses/components
    """
    path = "/ims/oneroster/rostering/v1p2/courses/components"

    query: Dict[str, Any] = {}
    if request.query_params:
        query = request.query_params.to_query_dict()

    data: Dict[str, Any] = http.get(path, params=query)
    log.debug(f"Raw Data: {data}")
    return TimebackGetAllCourseComponentsResponse.model_validate(data)

