"""Create Result endpoint for OneRoster Gradebook.

POST /ims/oneroster/gradebook/v1p2/results

Creates a new result and returns the allocated sourcedId.
"""

from typing import Any, Dict

from timeback.http import HttpClient
from timeback.models.request import TimebackCreateResultRequest
from timeback.models.response import TimebackCreateResultResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="DEBUG")


def create_result(
    http: HttpClient, request: TimebackCreateResultRequest
) -> TimebackCreateResultResponse:
    """Create a new result.

    POST /ims/oneroster/gradebook/v1p2/results

    Args:
        http: Injected HTTP client for making requests
        request: Request containing result data to create

    Returns:
        TimebackCreateResultResponse containing sourcedId mapping
    """
    body: Dict[str, Any] = request.model_dump(exclude_none=True)
    log.debug(f"POST body: {body}")
    
    data: Dict[str, Any] = http.post(
        "/ims/oneroster/gradebook/v1p2/results", json=body
    )
    
    log.debug(f"Raw Data: {data}")
    resp = TimebackCreateResultResponse.model_validate(data)
    return resp

