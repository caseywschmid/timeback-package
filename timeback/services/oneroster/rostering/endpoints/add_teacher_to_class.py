"""Add Teacher to Class endpoint for OneRoster Rostering.

POST /ims/oneroster/rostering/v1p2/classes/{classSourcedId}/teachers
"""

from typing import Any, Dict
from timeback.http import HttpClient
from timeback.models.request import TimebackAddTeacherToClassRequest
from timeback.models.response import TimebackAddTeacherToClassResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="DEBUG")


def add_teacher_to_class(
    http: HttpClient, request: TimebackAddTeacherToClassRequest
) -> TimebackAddTeacherToClassResponse:
    """Add a teacher to a class.

    POST /ims/oneroster/rostering/v1p2/classes/{classSourcedId}/teachers
    """
    body: Dict[str, Any] = {"teacher": request.teacher.model_dump(by_alias=True)}
    log.debug(f"POST body: {body}")
    log.debug(f"Class sourced ID: {request.class_sourced_id}")

    data: Dict[str, Any] = http.post(
        f"/ims/oneroster/rostering/v1p2/classes/{request.class_sourced_id}/teachers",
        json=body
    )

    log.debug(f"Raw Data: {data}")
    return TimebackAddTeacherToClassResponse.model_validate(data)

