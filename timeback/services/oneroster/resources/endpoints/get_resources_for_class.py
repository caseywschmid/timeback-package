"""Get Resources for Class endpoint for OneRoster Resources.

GET /ims/oneroster/resources/v1p2/classes/{classSourcedId}/resources
"""

from typing import Any, Dict
from timeback.http import HttpClient
from timeback.models.request import TimebackGetResourcesForClassRequest
from timeback.models.response import TimebackGetAllResourcesResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def get_resources_for_class(
    http: HttpClient,
    request: TimebackGetResourcesForClassRequest,
) -> TimebackGetAllResourcesResponse:
    """Fetch resources for a specific class.

    GET /ims/oneroster/resources/v1p2/classes/{classSourcedId}/resources
    """
    path = f"/ims/oneroster/resources/v1p2/classes/{request.class_sourced_id}/resources"

    query: Dict[str, Any] = {}
    if request.query_params:
        query = request.query_params.to_query_dict()

    data: Dict[str, Any] = http.get(path, params=query)
    log.debug(f"Raw Data: {data}")
    return TimebackGetAllResourcesResponse.model_validate(data)

