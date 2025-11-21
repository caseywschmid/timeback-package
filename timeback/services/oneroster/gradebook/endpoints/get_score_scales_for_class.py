"""Get Score Scales for Class endpoint for OneRoster Gradebook.

GET /ims/oneroster/gradebook/v1p2/classes/{sourcedId}/scoreScales

Builds the full path and query params, performs the HTTP GET via the injected
`HttpClient`, and parses the response into `TimebackGetScoreScalesForSchoolResponse`.
"""

from typing import Any, Dict

from timeback.http import HttpClient
from timeback.models.response import TimebackGetScoreScalesForSchoolResponse
from timeback.models.request import TimebackGetScoreScalesForClassRequest
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def get_score_scales_for_class(
    http: HttpClient,
    request: TimebackGetScoreScalesForClassRequest,
) -> TimebackGetScoreScalesForSchoolResponse:
    """Fetch a paginated list of score scales for a specific class.

    GET /ims/oneroster/gradebook/v1p2/classes/{sourcedId}/scoreScales

    Args:
        http: Injected HTTP client for making requests
        request: Request containing class_sourced_id and optional query parameters

    Returns:
        TimebackGetScoreScalesForSchoolResponse containing paginated list of score scales
    """
    path = f"/ims/oneroster/gradebook/v1p2/classes/{request.class_sourced_id}/scoreScales"

    query: Dict[str, Any] = {}
    if request.query_params:
        query = request.query_params.to_query_dict()

    data: Dict[str, Any] = http.get(path, params=query)
    log.debug(f"Raw Data: {data}")
    return TimebackGetScoreScalesForSchoolResponse.model_validate(data)

