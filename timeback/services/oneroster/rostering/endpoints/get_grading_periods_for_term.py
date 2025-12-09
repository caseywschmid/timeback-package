"""Get Grading Periods for Term endpoint for OneRoster Rostering.

GET /ims/oneroster/rostering/v1p2/terms/{termSourcedId}/gradingPeriods
"""

from typing import Any, Dict
from timeback.http import HttpClient
from timeback.models.request import TimebackGetGradingPeriodsForTermRequest
from timeback.models.response import TimebackGetAllTermsResponse  # Reuse - same structure
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def get_grading_periods_for_term(
    http: HttpClient, request: TimebackGetGradingPeriodsForTermRequest
) -> TimebackGetAllTermsResponse:
    """Fetch grading periods for a specific term.

    GET /ims/oneroster/rostering/v1p2/terms/{termSourcedId}/gradingPeriods
    """
    path = f"/ims/oneroster/rostering/v1p2/terms/{request.term_sourced_id}/gradingPeriods"

    query: Dict[str, Any] = {}
    if request.query_params:
        query = request.query_params.to_query_dict()

    data: Dict[str, Any] = http.get(path, params=query)
    log.debug(f"Raw Data: {data}")
    return TimebackGetAllTermsResponse.model_validate(data)

