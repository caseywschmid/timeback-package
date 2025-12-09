"""Create Component Resource endpoint for OneRoster Rostering.

POST /ims/oneroster/rostering/v1p2/courses/component-resources
"""

from typing import Any, Dict
from timeback.http import HttpClient
from timeback.models.request import TimebackCreateComponentResourceRequest
from timeback.models.response import TimebackCreateComponentResourceResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="DEBUG")


def create_component_resource(
    http: HttpClient, request: TimebackCreateComponentResourceRequest
) -> TimebackCreateComponentResourceResponse:
    """Create a new component resource.

    POST /ims/oneroster/rostering/v1p2/courses/component-resources
    """
    body: Dict[str, Any] = {
        "componentResource": request.componentResource.model_dump(by_alias=True, exclude_none=True)
    }
    log.debug(f"POST body: {body}")

    data: Dict[str, Any] = http.post("/ims/oneroster/rostering/v1p2/courses/component-resources", json=body)

    log.debug(f"Raw Data: {data}")
    return TimebackCreateComponentResourceResponse.model_validate(data)

