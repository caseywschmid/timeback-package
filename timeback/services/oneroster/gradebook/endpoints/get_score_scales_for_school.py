"""Get Score Scales for School endpoint for OneRoster Gradebook.

GET /ims/oneroster/gradebook/v1p2/schools/{sourcedId}/scoreScales

Fetches score scales for a specific school.
"""

from typing import Any, Dict

from timeback.http import HttpClient
from timeback.models.request import TimebackGetScoreScalesForSchoolRequest
from timeback.models.response import TimebackGetScoreScalesForSchoolResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="DEBUG")


def get_score_scales_for_school(
    http: HttpClient, request: TimebackGetScoreScalesForSchoolRequest
) -> TimebackGetScoreScalesForSchoolResponse:
    """Fetch score scales for a specific school.

    GET /ims/oneroster/gradebook/v1p2/schools/{sourcedId}/scoreScales

    Args:
        http: Injected HTTP client for making requests
        request: Request containing sourced_id and optional query parameters

    Returns:
        TimebackGetScoreScalesForSchoolResponse containing the score scales
    """
    # Extract query params if provided
    params: Dict[str, Any] = {}
    if request.query_params:
        params = request.query_params.to_query_dict()
    
    log.debug(f"Params: {params}")
    log.debug(f"School Sourced ID: {request.sourced_id}")
    
    data = http.get(
        f"/ims/oneroster/gradebook/v1p2/schools/{request.sourced_id}/scoreScales",
        params=params,
    )
    
    log.debug(f"Raw Data: {data}")
    return TimebackGetScoreScalesForSchoolResponse.model_validate(data)
