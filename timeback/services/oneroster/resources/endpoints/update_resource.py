"""Update Resource endpoint for OneRoster Resources.

PUT /ims/oneroster/resources/v1p2/resources/{sourcedId}
"""

from typing import Any, Dict
from timeback.http import HttpClient
from timeback.models.request import TimebackUpdateResourceRequest
from timeback.models.response import TimebackUpdateResourceResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="DEBUG")


def update_resource(
    http: HttpClient, request: TimebackUpdateResourceRequest
) -> TimebackUpdateResourceResponse:
    """Update a resource.

    PUT /ims/oneroster/resources/v1p2/resources/{sourcedId}
    """
    body: Dict[str, Any] = request.model_dump(exclude_none=True, exclude={'sourced_id'}, by_alias=True)
    log.debug(f"PUT body: {body}")
    log.debug(f"Sourced ID: {request.sourced_id}")
    
    data: Dict[str, Any] = http.put(
        f"/ims/oneroster/resources/v1p2/resources/{request.sourced_id}", json=body
    )
    
    log.debug(f"Raw Data: {data}")
    return TimebackUpdateResourceResponse.model_validate(data)

