"""Delete Result endpoint for OneRoster Gradebook.

DELETE /ims/oneroster/gradebook/v1p2/results/{sourcedId}

Soft deletes a result by its sourcedId.
"""

from typing import Optional, Dict, Any

from timeback.http import HttpClient
from timeback.models.request import TimebackDeleteResultRequest
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="DEBUG")


def delete_result(
    http: HttpClient, request: TimebackDeleteResultRequest
) -> Optional[Dict[str, Any]]:
    """Delete a result.

    DELETE /ims/oneroster/gradebook/v1p2/results/{sourcedId}

    Args:
        http: Injected HTTP client for making requests
        request: Request containing sourced_id

    Returns:
        Optional[Dict[str, Any]]: Raw provider response (None for no-content)
    """
    log.debug(f"Deleting result: {request.sourced_id}")
    
    return http.delete(
        f"/ims/oneroster/gradebook/v1p2/results/{request.sourced_id}"
    )

