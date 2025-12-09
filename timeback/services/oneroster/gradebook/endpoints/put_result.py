"""Put Result endpoint for OneRoster Gradebook.

PUT /ims/oneroster/gradebook/v1p2/results/{sourcedId}

Updates or creates a result with the given sourcedId.
"""

from typing import Any, Dict

from timeback.http import HttpClient
from timeback.models.request import TimebackPutResultRequest
from timeback.models.response import TimebackPutResultResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="DEBUG")


def put_result(
    http: HttpClient, request: TimebackPutResultRequest
) -> TimebackPutResultResponse:
    """Update or create a result.

    PUT /ims/oneroster/gradebook/v1p2/results/{sourcedId}

    Args:
        http: Injected HTTP client for making requests
        request: Request containing sourced_id and result data

    Returns:
        TimebackPutResultResponse containing the updated/created result
    """
    # Exclude sourced_id from body since it's used in the URL path
    # Use by_alias=True to get "result" instead of potentially snake_case
    body: Dict[str, Any] = request.model_dump(exclude_none=True, exclude={'sourced_id'}, by_alias=True)
    log.debug(f"PUT body: {body}")
    log.debug(f"Sourced ID: {request.sourced_id}")
    
    data: Dict[str, Any] = http.put(
        f"/ims/oneroster/gradebook/v1p2/results/{request.sourced_id}", json=body
    )
    
    log.debug(f"Raw Data: {data}")
    return TimebackPutResultResponse.model_validate(data)

