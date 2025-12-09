"""Update Course endpoint for OneRoster Rostering.

PUT /ims/oneroster/rostering/v1p2/courses/{sourcedId}
"""

from typing import Any, Dict
from timeback.http import HttpClient
from timeback.models.request import TimebackUpdateCourseRequest
from timeback.models.response import TimebackUpdateCourseResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="DEBUG")


def update_course(
    http: HttpClient, request: TimebackUpdateCourseRequest
) -> TimebackUpdateCourseResponse:
    """Update an existing course.

    PUT /ims/oneroster/rostering/v1p2/courses/{sourcedId}
    """
    body: Dict[str, Any] = {
        "course": request.course.model_dump(by_alias=True, exclude_none=True)
    }
    log.debug(f"PUT body: {body}")
    log.debug(f"Sourced ID: {request.sourced_id}")

    data: Dict[str, Any] = http.put(
        f"/ims/oneroster/rostering/v1p2/courses/{request.sourced_id}", json=body
    )

    log.debug(f"Raw Data: {data}")
    return TimebackUpdateCourseResponse.model_validate(data)

