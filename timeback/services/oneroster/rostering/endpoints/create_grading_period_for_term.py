"""Create Grading Period for Term endpoint for OneRoster Rostering.

POST /ims/oneroster/rostering/v1p2/terms/{termSourcedId}/gradingPeriods
"""

from typing import Any, Dict
from timeback.http import HttpClient
from timeback.models.request import TimebackCreateGradingPeriodForTermRequest
from timeback.models.response import TimebackCreateGradingPeriodResponse  # Reuse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="DEBUG")


def create_grading_period_for_term(
    http: HttpClient, request: TimebackCreateGradingPeriodForTermRequest
) -> TimebackCreateGradingPeriodResponse:
    """Create a new grading period for a specific term.

    POST /ims/oneroster/rostering/v1p2/terms/{termSourcedId}/gradingPeriods
    """
    body: Dict[str, Any] = {
        "academicSession": request.academic_session.model_dump(by_alias=True, exclude_none=True)
    }
    log.debug(f"POST body: {body}")
    log.debug(f"Term sourced ID: {request.term_sourced_id}")

    data: Dict[str, Any] = http.post(
        f"/ims/oneroster/rostering/v1p2/terms/{request.term_sourced_id}/gradingPeriods",
        json=body
    )

    log.debug(f"Raw Data: {data}")
    return TimebackCreateGradingPeriodResponse.model_validate(data)

