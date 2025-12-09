"""Create Score Scale endpoint for OneRoster Gradebook.

POST /ims/oneroster/gradebook/v1p2/scoreScales

Creates a new score scale and returns the allocated sourcedId.
"""

from typing import Any, Dict

from timeback.http import HttpClient
from timeback.models.request import TimebackCreateScoreScaleRequest
from timeback.models.response import TimebackCreateScoreScaleResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="DEBUG")


def create_score_scale(
    http: HttpClient, request: TimebackCreateScoreScaleRequest
) -> TimebackCreateScoreScaleResponse:
    """Create a new score scale.

    POST /ims/oneroster/gradebook/v1p2/scoreScales

    Args:
        http: Injected HTTP client for making requests
        request: Request containing score scale data to create

    Returns:
        TimebackCreateScoreScaleResponse containing sourcedId mapping
    """
    body: Dict[str, Any] = request.model_dump(by_alias=True, exclude_none=True)
    log.debug(f"POST body: {body}")
    
    data: Dict[str, Any] = http.post(
        "/ims/oneroster/gradebook/v1p2/scoreScales", json=body
    )
    
    log.debug(f"Raw Data: {data}")
    resp = TimebackCreateScoreScaleResponse.model_validate(data)
    return resp
