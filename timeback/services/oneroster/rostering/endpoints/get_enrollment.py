"""Get Enrollment endpoint for OneRoster Rostering.

GET /ims/oneroster/rostering/v1p2/enrollments/{sourcedId}
"""

from typing import Any, Dict
from timeback.http import HttpClient
from timeback.models.request import TimebackGetEnrollmentRequest
from timeback.models.response import TimebackGetEnrollmentResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="DEBUG")


def get_enrollment(
    http: HttpClient, request: TimebackGetEnrollmentRequest
) -> TimebackGetEnrollmentResponse:
    """Fetch a single enrollment by sourcedId.

    GET /ims/oneroster/rostering/v1p2/enrollments/{sourcedId}
    """
    params: Dict[str, Any] = {}
    if request.query_params:
        params = request.query_params.to_query_dict()

    log.debug(f"Sourced ID: {request.sourced_id}")

    data = http.get(
        f"/ims/oneroster/rostering/v1p2/enrollments/{request.sourced_id}", params=params
    )

    log.debug(f"Raw Data: {data}")
    return TimebackGetEnrollmentResponse.model_validate(data)

