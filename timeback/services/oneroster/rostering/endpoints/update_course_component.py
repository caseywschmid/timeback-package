"""Update Course Component endpoint for OneRoster Rostering.

PUT /ims/oneroster/rostering/v1p2/courses/components/{sourcedId}
"""

from typing import Any, Dict
from timeback.http import HttpClient
from timeback.models.request import TimebackUpdateCourseComponentRequest
from timeback.models.response import TimebackUpdateCourseComponentResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="DEBUG")


def update_course_component(
    http: HttpClient, request: TimebackUpdateCourseComponentRequest
) -> TimebackUpdateCourseComponentResponse:
    """Update an existing course component.

    PUT /ims/oneroster/rostering/v1p2/courses/components/{sourcedId}
    """
    body: Dict[str, Any] = {
        "courseComponent": request.courseComponent.model_dump(by_alias=True, exclude_none=True)
    }
    log.debug(f"PUT body: {body}")
    log.debug(f"Sourced ID: {request.sourced_id}")

    data: Dict[str, Any] = http.put(
        f"/ims/oneroster/rostering/v1p2/courses/components/{request.sourced_id}", json=body
    )

    log.debug(f"Raw Data: {data}")
    return TimebackUpdateCourseComponentResponse.model_validate(data)

