"""Add Student to Class endpoint for OneRoster Rostering.

POST /ims/oneroster/rostering/v1p2/classes/{classSourcedId}/students
"""

from typing import Any, Dict
from timeback.http import HttpClient
from timeback.models.request import TimebackAddStudentToClassRequest
from timeback.models.response import TimebackAddStudentToClassResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="DEBUG")


def add_student_to_class(
    http: HttpClient, request: TimebackAddStudentToClassRequest
) -> TimebackAddStudentToClassResponse:
    """Add a student to a class.

    POST /ims/oneroster/rostering/v1p2/classes/{classSourcedId}/students
    """
    body: Dict[str, Any] = {"student": request.student.model_dump(by_alias=True)}
    log.debug(f"POST body: {body}")
    log.debug(f"Class sourced ID: {request.class_sourced_id}")

    data: Dict[str, Any] = http.post(
        f"/ims/oneroster/rostering/v1p2/classes/{request.class_sourced_id}/students",
        json=body
    )

    log.debug(f"Raw Data: {data}")
    return TimebackAddStudentToClassResponse.model_validate(data)

