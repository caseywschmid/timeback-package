"""Get Score Scale endpoint for OneRoster Gradebook.

GET /ims/oneroster/gradebook/v1p2/scoreScales/{sourcedId}

Fetches a single score scale by its sourcedId.
"""

from typing import Any, Dict

from timeback.http import HttpClient
from timeback.models.request import TimebackGetScoreScaleRequest
from timeback.models.response import TimebackGetScoreScaleResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="DEBUG")


def get_score_scale(
    http: HttpClient, request: TimebackGetScoreScaleRequest
) -> TimebackGetScoreScaleResponse:
    """Fetch a single score scale by sourcedId.

    GET /ims/oneroster/gradebook/v1p2/scoreScales/{sourcedId}

    Args:
        http: Injected HTTP client for making requests
        request: Request containing sourced_id and optional query parameters

    Returns:
        TimebackGetScoreScaleResponse containing the score scale data
    """
    # Extract query params if provided
    params: Dict[str, Any] = {}
    if request.query_params:
        params = request.query_params.to_query_dict()
    
    log.debug(f"Params: {params}")
    log.debug(f"Sourced ID: {request.sourced_id}")
    
    data = http.get(
        f"/ims/oneroster/gradebook/v1p2/scoreScales/{request.sourced_id}", params=params
    )
    
    log.debug(f"Raw Data: {data}")
    return TimebackGetScoreScaleResponse.model_validate(data)
