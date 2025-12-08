"""Update Grading Period endpoint for OneRoster Rostering.

PUT /ims/oneroster/rostering/v1p2/gradingPeriods/{sourcedId}
"""

from typing import Any, Dict
from timeback.http import HttpClient
from timeback.models.request import TimebackUpdateGradingPeriodRequest
from timeback.models.response import TimebackUpdateGradingPeriodResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="DEBUG")


def update_grading_period(
    http: HttpClient, request: TimebackUpdateGradingPeriodRequest
) -> TimebackUpdateGradingPeriodResponse:
    """Update an existing grading period.

    PUT /ims/oneroster/rostering/v1p2/gradingPeriods/{sourcedId}
    """
    body: Dict[str, Any] = {
        "academicSession": request.academic_session.model_dump(by_alias=True, exclude_none=True)
    }
    log.debug(f"PUT body: {body}")
    log.debug(f"Sourced ID: {request.sourced_id}")

    data: Dict[str, Any] = http.put(
        f"/ims/oneroster/rostering/v1p2/gradingPeriods/{request.sourced_id}", json=body
    )

    log.debug(f"Raw Data: {data}")
    return TimebackUpdateGradingPeriodResponse.model_validate(data)

