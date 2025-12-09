"""Get Courses for School endpoint for OneRoster Rostering.

GET /ims/oneroster/rostering/v1p2/schools/{schoolSourcedId}/courses
"""

from typing import Any, Dict
from timeback.http import HttpClient
from timeback.models.request import TimebackGetCoursesForSchoolRequest
from timeback.models.response import TimebackGetAllCoursesResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def get_courses_for_school(
    http: HttpClient, request: TimebackGetCoursesForSchoolRequest
) -> TimebackGetAllCoursesResponse:
    """Fetch all courses for a specific school (paginated list).

    GET /ims/oneroster/rostering/v1p2/schools/{schoolSourcedId}/courses
    """
    path = f"/ims/oneroster/rostering/v1p2/schools/{request.school_sourced_id}/courses"

    query: Dict[str, Any] = {}
    if request.query_params:
        query = request.query_params.to_query_dict()

    data: Dict[str, Any] = http.get(path, params=query)
    log.debug(f"Raw Data: {data}")
    return TimebackGetAllCoursesResponse.model_validate(data)

