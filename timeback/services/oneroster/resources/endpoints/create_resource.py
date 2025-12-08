"""Create Resource endpoint for OneRoster Resources.

POST /ims/oneroster/resources/v1p2/resources
"""

from typing import Any, Dict
from timeback.http import HttpClient
from timeback.models.request import TimebackCreateResourceRequest
from timeback.models.response import TimebackCreateResourceResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="DEBUG")


def create_resource(
    http: HttpClient, request: TimebackCreateResourceRequest
) -> TimebackCreateResourceResponse:
    """Create a new resource.

    POST /ims/oneroster/resources/v1p2/resources
    """
    body: Dict[str, Any] = request.model_dump(exclude_none=True, by_alias=True)
    log.debug(f"POST body: {body}")
    
    data: Dict[str, Any] = http.post(
        "/ims/oneroster/resources/v1p2/resources", json=body
    )
    
    log.debug(f"Raw Data: {data}")
    return TimebackCreateResourceResponse.model_validate(data)

