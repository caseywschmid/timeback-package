"""Get All Component Resources endpoint for OneRoster Rostering.

GET /ims/oneroster/rostering/v1p2/courses/component-resources
"""

from typing import Any, Dict
from timeback.http import HttpClient
from timeback.models.request import TimebackGetAllComponentResourcesRequest
from timeback.models.response import TimebackGetAllComponentResourcesResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def get_all_component_resources(
    http: HttpClient, request: TimebackGetAllComponentResourcesRequest
) -> TimebackGetAllComponentResourcesResponse:
    """Fetch all component resources (paginated list).

    GET /ims/oneroster/rostering/v1p2/courses/component-resources
    """
    path = "/ims/oneroster/rostering/v1p2/courses/component-resources"

    query: Dict[str, Any] = {}
    if request.query_params:
        query = request.query_params.to_query_dict()

    data: Dict[str, Any] = http.get(path, params=query)
    log.debug(f"Raw Data: {data}")
    return TimebackGetAllComponentResourcesResponse.model_validate(data)

