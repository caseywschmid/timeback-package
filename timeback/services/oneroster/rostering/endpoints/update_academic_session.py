"""Update Academic Session endpoint for OneRoster Rostering.

PUT /ims/oneroster/rostering/v1p2/academicSessions/{sourcedId}
"""

from typing import Any, Dict
from timeback.http import HttpClient
from timeback.models.request import TimebackUpdateAcademicSessionRequest
from timeback.models.response import TimebackUpdateAcademicSessionResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="DEBUG")


def update_academic_session(
    http: HttpClient, request: TimebackUpdateAcademicSessionRequest
) -> TimebackUpdateAcademicSessionResponse:
    """Update an existing academic session.

    PUT /ims/oneroster/rostering/v1p2/academicSessions/{sourcedId}
    """
    body: Dict[str, Any] = {
        "academicSession": request.academicSession.model_dump(by_alias=True, exclude_none=True)
    }
    log.debug(f"PUT body: {body}")
    log.debug(f"Sourced ID: {request.sourced_id}")

    data: Dict[str, Any] = http.put(
        f"/ims/oneroster/rostering/v1p2/academicSessions/{request.sourced_id}", json=body
    )

    log.debug(f"Raw Data: {data}")
    return TimebackUpdateAcademicSessionResponse.model_validate(data)

