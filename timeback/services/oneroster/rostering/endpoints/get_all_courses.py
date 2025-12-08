"""Get All Courses endpoint for OneRoster Rostering.

GET /ims/oneroster/rostering/v1p2/courses
"""

from typing import Any, Dict
from timeback.http import HttpClient
from timeback.models.request import TimebackGetAllCoursesRequest
from timeback.models.response import TimebackGetAllCoursesResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def get_all_courses(
    http: HttpClient, request: TimebackGetAllCoursesRequest
) -> TimebackGetAllCoursesResponse:
    """Fetch all courses (paginated list).

    GET /ims/oneroster/rostering/v1p2/courses
    """
    path = "/ims/oneroster/rostering/v1p2/courses"

    query: Dict[str, Any] = {}
    if request.query_params:
        query = request.query_params.to_query_dict()

    data: Dict[str, Any] = http.get(path, params=query)
    log.debug(f"Raw Data: {data}")
    return TimebackGetAllCoursesResponse.model_validate(data)

