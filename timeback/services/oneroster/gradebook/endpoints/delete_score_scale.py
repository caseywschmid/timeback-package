"""Delete Score Scale endpoint for OneRoster Gradebook.

DELETE /ims/oneroster/gradebook/v1p2/scoreScales/{sourcedId}

Soft deletes a score scale by its sourcedId.
"""

from typing import Optional, Dict, Any

from timeback.http import HttpClient
from timeback.models.request import TimebackDeleteScoreScaleRequest
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="DEBUG")


def delete_score_scale(
    http: HttpClient, request: TimebackDeleteScoreScaleRequest
) -> Optional[Dict[str, Any]]:
    """Delete a score scale.

    DELETE /ims/oneroster/gradebook/v1p2/scoreScales/{sourcedId}

    Args:
        http: Injected HTTP client for making requests
        request: Request containing sourced_id

    Returns:
        Optional[Dict[str, Any]]: Raw provider response (None for no-content)
    """
    log.debug(f"Deleting score scale: {request.sourced_id}")
    
    return http.delete(
        f"/ims/oneroster/gradebook/v1p2/scoreScales/{request.sourced_id}"
    )
