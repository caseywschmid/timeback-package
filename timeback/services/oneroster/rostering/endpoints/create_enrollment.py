"""Create Enrollment endpoint for OneRoster Rostering.

POST /ims/oneroster/rostering/v1p2/enrollments
"""

from typing import Any, Dict
from timeback.http import HttpClient
from timeback.models.request import TimebackCreateEnrollmentRequest
from timeback.models.response import TimebackCreateEnrollmentResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="DEBUG")


def create_enrollment(
    http: HttpClient, request: TimebackCreateEnrollmentRequest
) -> TimebackCreateEnrollmentResponse:
    """Create a new enrollment.

    POST /ims/oneroster/rostering/v1p2/enrollments
    """
    body: Dict[str, Any] = {
        "enrollment": request.enrollment.model_dump(by_alias=True, exclude_none=True)
    }
    log.debug(f"POST body: {body}")

    data: Dict[str, Any] = http.post("/ims/oneroster/rostering/v1p2/enrollments", json=body)

    log.debug(f"Raw Data: {data}")
    return TimebackCreateEnrollmentResponse.model_validate(data)

