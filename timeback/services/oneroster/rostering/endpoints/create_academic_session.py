"""Create Academic Session endpoint for OneRoster Rostering.

POST /ims/oneroster/rostering/v1p2/academicSessions
"""

from typing import Any, Dict
from timeback.http import HttpClient
from timeback.models.request import TimebackCreateAcademicSessionRequest
from timeback.models.response import TimebackCreateAcademicSessionResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="DEBUG")


def create_academic_session(
    http: HttpClient, request: TimebackCreateAcademicSessionRequest
) -> TimebackCreateAcademicSessionResponse:
    """Create a new academic session.

    POST /ims/oneroster/rostering/v1p2/academicSessions
    """
    body: Dict[str, Any] = {
        "academicSession": request.academicSession.model_dump(by_alias=True, exclude_none=True)
    }
    log.debug(f"POST body: {body}")

    data: Dict[str, Any] = http.post("/ims/oneroster/rostering/v1p2/academicSessions", json=body)

    log.debug(f"Raw Data: {data}")
    return TimebackCreateAcademicSessionResponse.model_validate(data)

