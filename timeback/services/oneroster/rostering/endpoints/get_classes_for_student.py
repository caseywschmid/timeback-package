"""Get Classes for Student endpoint for OneRoster Rostering.

GET /ims/oneroster/rostering/v1p2/students/{studentSourcedId}/classes
"""

from typing import Any, Dict
from timeback.http import HttpClient
from timeback.models.request import TimebackGetClassesForStudentRequest
from timeback.models.response import TimebackGetAllClassesResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def get_classes_for_student(
    http: HttpClient, request: TimebackGetClassesForStudentRequest
) -> TimebackGetAllClassesResponse:
    """Fetch classes for a specific student.

    GET /ims/oneroster/rostering/v1p2/students/{studentSourcedId}/classes
    """
    path = f"/ims/oneroster/rostering/v1p2/students/{request.student_sourced_id}/classes"

    query: Dict[str, Any] = {}
    if request.query_params:
        query = request.query_params.to_query_dict()

    data: Dict[str, Any] = http.get(path, params=query)
    log.debug(f"Raw Data: {data}")
    return TimebackGetAllClassesResponse.model_validate(data)

