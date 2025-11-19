"""Get All Score Scales endpoint for OneRoster Gradebook.

GET /ims/oneroster/gradebook/v1p2/scoreScales

Builds the full path and query params, performs the HTTP GET via the injected
`HttpClient`, and parses the response into `TimebackGetAllScoreScalesResponse`.
"""

from typing import Any, Dict

from timeback.http import HttpClient
from timeback.models.response import TimebackGetAllScoreScalesResponse
from timeback.models.request import TimebackGetAllScoreScalesRequest
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def get_all_score_scales(
    http: HttpClient,
    request: TimebackGetAllScoreScalesRequest,
) -> TimebackGetAllScoreScalesResponse:
    """Fetch a paginated list of score scales.

    GET /ims/oneroster/gradebook/v1p2/scoreScales

    Args:
        http: Injected HTTP client for making requests
        request: Request containing optional query parameters

    Returns:
        TimebackGetAllScoreScalesResponse containing paginated list of score scales
    """
    path = "/ims/oneroster/gradebook/v1p2/scoreScales"

    query: Dict[str, Any] = {}
    if request.query_params:
        query = request.query_params.to_query_dict()

    data: Dict[str, Any] = http.get(path, params=query)
    log.debug(f"Raw Data: {data}")
    return TimebackGetAllScoreScalesResponse.model_validate(data)
