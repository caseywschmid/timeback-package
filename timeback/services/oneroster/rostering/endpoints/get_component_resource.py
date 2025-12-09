"""Get Component Resource endpoint for OneRoster Rostering.

GET /ims/oneroster/rostering/v1p2/courses/component-resources/{sourcedId}
"""

from typing import Any, Dict
from timeback.http import HttpClient
from timeback.models.request import TimebackGetComponentResourceRequest
from timeback.models.response import TimebackGetComponentResourceResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="DEBUG")


def get_component_resource(
    http: HttpClient, request: TimebackGetComponentResourceRequest
) -> TimebackGetComponentResourceResponse:
    """Fetch a single component resource by sourcedId.

    GET /ims/oneroster/rostering/v1p2/courses/component-resources/{sourcedId}
    """
    params: Dict[str, Any] = {}
    if request.query_params:
        params = request.query_params.to_query_dict()

    log.debug(f"Sourced ID: {request.sourced_id}")

    data = http.get(
        f"/ims/oneroster/rostering/v1p2/courses/component-resources/{request.sourced_id}", params=params
    )

    log.debug(f"Raw Data: {data}")
    return TimebackGetComponentResourceResponse.model_validate(data)

