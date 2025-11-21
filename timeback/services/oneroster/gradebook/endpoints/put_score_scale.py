"""Put Score Scale endpoint for OneRoster Gradebook.

PUT /ims/oneroster/gradebook/v1p2/scoreScales/{sourcedId}

Updates or creates a score scale with the given sourcedId.
"""

from typing import Any, Dict

from timeback.http import HttpClient
from timeback.models.request import TimebackPutScoreScaleRequest
from timeback.models.response import TimebackPutScoreScaleResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="DEBUG")


def put_score_scale(
    http: HttpClient, request: TimebackPutScoreScaleRequest
) -> TimebackPutScoreScaleResponse:
    """Update or create a score scale.

    PUT /ims/oneroster/gradebook/v1p2/scoreScales/{sourcedId}

    Args:
        http: Injected HTTP client for making requests
        request: Request containing sourced_id and score scale data

    Returns:
        TimebackPutScoreScaleResponse containing the updated/created score scale
    """
    # Exclude sourced_id from body since it's used in the URL path
    # Use by_alias=True to get "scoreScale" instead of "score_scale"
    body: Dict[str, Any] = request.model_dump(exclude_none=True, exclude={'sourced_id'}, by_alias=True)
    log.debug(f"PUT body: {body}")
    log.debug(f"Sourced ID: {request.sourced_id}")
    
    data: Dict[str, Any] = http.put(
        f"/ims/oneroster/gradebook/v1p2/scoreScales/{request.sourced_id}", json=body
    )
    
    log.debug(f"Raw Data: {data}")
    return TimebackPutScoreScaleResponse.model_validate(data)
