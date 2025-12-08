"""Create Course endpoint for OneRoster Rostering.

POST /ims/oneroster/rostering/v1p2/courses
"""

from typing import Any, Dict
from timeback.http import HttpClient
from timeback.models.request import TimebackCreateCourseRequest
from timeback.models.response import TimebackCreateCourseResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="DEBUG")


def create_course(
    http: HttpClient, request: TimebackCreateCourseRequest
) -> TimebackCreateCourseResponse:
    """Create a new course.

    POST /ims/oneroster/rostering/v1p2/courses
    """
    body: Dict[str, Any] = {
        "course": request.course.model_dump(by_alias=True, exclude_none=True)
    }
    log.debug(f"POST body: {body}")

    data: Dict[str, Any] = http.post("/ims/oneroster/rostering/v1p2/courses", json=body)

    log.debug(f"Raw Data: {data}")
    return TimebackCreateCourseResponse.model_validate(data)

