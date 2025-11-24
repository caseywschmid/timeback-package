"""Create Class endpoint for OneRoster Rostering.

POST /ims/oneroster/rostering/v1p2/classes

Creates a new class.
"""

from typing import Dict, Any

from timeback.http import HttpClient
from timeback.models.request import TimebackCreateClassRequest
from timeback.models.response import TimebackCreateClassResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="DEBUG")


def create_class(http: HttpClient, request: TimebackCreateClassRequest) -> TimebackCreateClassResponse:
    """Create a new class.

    POST /ims/oneroster/rostering/v1p2/classes

    Args:
        http: Injected HTTP client for making requests
        request: Request containing class data to create

    Returns:
        TimebackCreateClassResponse containing sourcedIdPairs mapping
    """
    body: Dict[str, Any] = request.model_dump(exclude_none=True, by_alias=True)
    log.debug(f"POST body: {body}")
    data: Dict[str, Any] = http.post(
        "/ims/oneroster/rostering/v1p2/classes", json=body
    )
    log.debug(f"Raw Data: {data}")
    resp = TimebackCreateClassResponse.model_validate(data)
    return resp

