"""Create Grading Period endpoint for OneRoster Rostering.

POST /ims/oneroster/rostering/v1p2/gradingPeriods
"""

from typing import Any, Dict
from timeback.http import HttpClient
from timeback.models.request import TimebackCreateGradingPeriodRequest
from timeback.models.response import TimebackCreateGradingPeriodResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="DEBUG")


def create_grading_period(
    http: HttpClient, request: TimebackCreateGradingPeriodRequest
) -> TimebackCreateGradingPeriodResponse:
    """Create a new grading period.

    POST /ims/oneroster/rostering/v1p2/gradingPeriods
    """
    body: Dict[str, Any] = {
        "academicSession": request.academic_session.model_dump(by_alias=True, exclude_none=True)
    }
    log.debug(f"POST body: {body}")

    data: Dict[str, Any] = http.post("/ims/oneroster/rostering/v1p2/gradingPeriods", json=body)

    log.debug(f"Raw Data: {data}")
    return TimebackCreateGradingPeriodResponse.model_validate(data)

