"""Get All Grading Periods endpoint for OneRoster Rostering.

GET /ims/oneroster/rostering/v1p2/gradingPeriods
"""

from typing import Any, Dict
from timeback.http import HttpClient
from timeback.models.request import TimebackGetAllGradingPeriodsRequest
from timeback.models.response import TimebackGetAllTermsResponse  # Reuse - same structure
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def get_all_grading_periods(
    http: HttpClient, request: TimebackGetAllGradingPeriodsRequest
) -> TimebackGetAllTermsResponse:
    """Fetch all grading periods (paginated list).

    GET /ims/oneroster/rostering/v1p2/gradingPeriods

    Note: Grading periods are a type of academic session, so the response
    uses the same model as terms (TimebackGetAllTermsResponse).
    """
    path = "/ims/oneroster/rostering/v1p2/gradingPeriods"

    query: Dict[str, Any] = {}
    if request.query_params:
        query = request.query_params.to_query_dict()

    data: Dict[str, Any] = http.get(path, params=query)
    log.debug(f"Raw Data: {data}")
    return TimebackGetAllTermsResponse.model_validate(data)

