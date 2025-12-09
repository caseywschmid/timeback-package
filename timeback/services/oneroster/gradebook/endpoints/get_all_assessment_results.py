"""Get All Assessment Results endpoint for OneRoster Gradebook.

GET /ims/oneroster/gradebook/v1p2/assessmentResults

Builds the full path and query params, performs the HTTP GET via the injected
`HttpClient`, and parses the response into `TimebackGetAllAssessmentResultsResponse`.
"""

from typing import Any, Dict

from timeback.http import HttpClient
from timeback.models.response import TimebackGetAllAssessmentResultsResponse
from timeback.models.request import TimebackGetAllAssessmentResultsRequest
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def get_all_assessment_results(
    http: HttpClient,
    request: TimebackGetAllAssessmentResultsRequest,
) -> TimebackGetAllAssessmentResultsResponse:
    """Fetch a paginated list of assessment results.

    GET /ims/oneroster/gradebook/v1p2/assessmentResults

    Args:
        http: Injected HTTP client for making requests
        request: Request containing optional query parameters

    Returns:
        TimebackGetAllAssessmentResultsResponse containing paginated list of assessment results
    """
    path = "/ims/oneroster/gradebook/v1p2/assessmentResults"

    query: Dict[str, Any] = {}
    if request.query_params:
        query = request.query_params.to_query_dict()

    data: Dict[str, Any] = http.get(path, params=query)
    log.debug(f"Raw Data: {data}")
    return TimebackGetAllAssessmentResultsResponse.model_validate(data)

