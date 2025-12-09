"""Update Component Resource endpoint for OneRoster Rostering.

PUT /ims/oneroster/rostering/v1p2/courses/component-resources/{sourcedId}
"""

from typing import Any, Dict
from timeback.http import HttpClient
from timeback.models.request import TimebackUpdateComponentResourceRequest
from timeback.models.response import TimebackUpdateComponentResourceResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="DEBUG")


def update_component_resource(
    http: HttpClient, request: TimebackUpdateComponentResourceRequest
) -> TimebackUpdateComponentResourceResponse:
    """Update an existing component resource.

    PUT /ims/oneroster/rostering/v1p2/courses/component-resources/{sourcedId}
    """
    body: Dict[str, Any] = {
        "componentResource": request.componentResource.model_dump(by_alias=True, exclude_none=True)
    }
    log.debug(f"PUT body: {body}")
    log.debug(f"Sourced ID: {request.sourced_id}")

    data: Dict[str, Any] = http.put(
        f"/ims/oneroster/rostering/v1p2/courses/component-resources/{request.sourced_id}", json=body
    )

    log.debug(f"Raw Data: {data}")
    return TimebackUpdateComponentResourceResponse.model_validate(data)

