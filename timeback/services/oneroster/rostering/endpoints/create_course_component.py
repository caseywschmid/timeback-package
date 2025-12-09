"""Create Course Component endpoint for OneRoster Rostering.

POST /ims/oneroster/rostering/v1p2/courses/components
"""

from typing import Any, Dict
from timeback.http import HttpClient
from timeback.models.request import TimebackCreateCourseComponentRequest
from timeback.models.response import TimebackCreateCourseComponentResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="DEBUG")


def create_course_component(
    http: HttpClient, request: TimebackCreateCourseComponentRequest
) -> TimebackCreateCourseComponentResponse:
    """Create a new course component.

    POST /ims/oneroster/rostering/v1p2/courses/components
    """
    body: Dict[str, Any] = {
        "courseComponent": request.courseComponent.model_dump(by_alias=True, exclude_none=True)
    }
    log.debug(f"POST body: {body}")

    data: Dict[str, Any] = http.post("/ims/oneroster/rostering/v1p2/courses/components", json=body)

    log.debug(f"Raw Data: {data}")
    return TimebackCreateCourseComponentResponse.model_validate(data)

