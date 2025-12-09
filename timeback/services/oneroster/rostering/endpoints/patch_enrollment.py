"""Partially Update Enrollment endpoint for OneRoster Rostering.

PATCH /ims/oneroster/rostering/v1p2/enrollments/{sourcedId}
"""

from typing import Any, Dict
from timeback.http import HttpClient
from timeback.models.request import TimebackPatchEnrollmentRequest
from timeback.models.response import TimebackUpdateEnrollmentResponse  # Reuse response
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="DEBUG")


def patch_enrollment(
    http: HttpClient, request: TimebackPatchEnrollmentRequest
) -> TimebackUpdateEnrollmentResponse:
    """Partially update an existing enrollment with metadata merging.

    PATCH /ims/oneroster/rostering/v1p2/enrollments/{sourcedId}
    """
    body: Dict[str, Any] = {
        "enrollment": request.enrollment.model_dump(by_alias=True, exclude_none=True)
    }
    log.debug(f"PATCH body: {body}")
    log.debug(f"Sourced ID: {request.sourced_id}")

    data: Dict[str, Any] = http.patch(
        f"/ims/oneroster/rostering/v1p2/enrollments/{request.sourced_id}", json=body
    )

    log.debug(f"Raw Data: {data}")
    return TimebackUpdateEnrollmentResponse.model_validate(data)

