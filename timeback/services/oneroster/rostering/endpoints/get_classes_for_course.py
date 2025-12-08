"""Get Classes for Course endpoint for OneRoster Rostering.

GET /ims/oneroster/rostering/v1p2/courses/{courseSourcedId}/classes
"""

from typing import Any, Dict
from timeback.http import HttpClient
from timeback.models.request import TimebackGetClassesForCourseRequest
from timeback.models.response import TimebackGetAllClassesResponse  # Reuse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def get_classes_for_course(
    http: HttpClient, request: TimebackGetClassesForCourseRequest
) -> TimebackGetAllClassesResponse:
    """Fetch classes for a specific course.

    GET /ims/oneroster/rostering/v1p2/courses/{courseSourcedId}/classes
    """
    path = f"/ims/oneroster/rostering/v1p2/courses/{request.course_sourced_id}/classes"

    query: Dict[str, Any] = {}
    if request.query_params:
        query = request.query_params.to_query_dict()

    data: Dict[str, Any] = http.get(path, params=query)
    log.debug(f"Raw Data: {data}")
    return TimebackGetAllClassesResponse.model_validate(data)

