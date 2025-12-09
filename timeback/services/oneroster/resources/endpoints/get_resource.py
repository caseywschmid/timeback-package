"""Get Resource endpoint for OneRoster Resources.

GET /ims/oneroster/resources/v1p2/resources/{sourcedId}
"""

from typing import Any, Dict
from timeback.http import HttpClient
from timeback.models.request import TimebackGetResourceRequest
from timeback.models.response import TimebackGetResourceResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="DEBUG")


def get_resource(
    http: HttpClient, request: TimebackGetResourceRequest
) -> TimebackGetResourceResponse:
    """Fetch a single resource by sourcedId.

    GET /ims/oneroster/resources/v1p2/resources/{sourcedId}
    """
    params: Dict[str, Any] = {}
    if request.query_params:
        params = request.query_params.to_query_dict()
    
    log.debug(f"Params: {params}")
    log.debug(f"Sourced ID: {request.sourced_id}")
    
    data = http.get(
        f"/ims/oneroster/resources/v1p2/resources/{request.sourced_id}", params=params
    )
    
    log.debug(f"Raw Data: {data}")
    return TimebackGetResourceResponse.model_validate(data)

