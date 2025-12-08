"""Get Grading Period endpoint for OneRoster Rostering.

GET /ims/oneroster/rostering/v1p2/gradingPeriods/{sourcedId}
"""

from typing import Any, Dict
from timeback.http import HttpClient
from timeback.models.request import TimebackGetGradingPeriodRequest
from timeback.models.response import TimebackGetTermResponse  # Reuse - same structure
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="DEBUG")


def get_grading_period(
    http: HttpClient, request: TimebackGetGradingPeriodRequest
) -> TimebackGetTermResponse:
    """Fetch a single grading period by sourcedId.

    GET /ims/oneroster/rostering/v1p2/gradingPeriods/{sourcedId}
    """
    params: Dict[str, Any] = {}
    if request.query_params:
        params = request.query_params.to_query_dict()

    log.debug(f"Sourced ID: {request.sourced_id}")

    data = http.get(
        f"/ims/oneroster/rostering/v1p2/gradingPeriods/{request.sourced_id}", params=params
    )

    log.debug(f"Raw Data: {data}")
    return TimebackGetTermResponse.model_validate(data)

