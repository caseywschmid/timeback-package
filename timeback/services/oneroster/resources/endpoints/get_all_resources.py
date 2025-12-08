"""Get All Resources endpoint for OneRoster Resources.

GET /ims/oneroster/resources/v1p2/resources
"""

from typing import Any, Dict
from timeback.http import HttpClient
from timeback.models.response import TimebackGetAllResourcesResponse
from timeback.models.request import TimebackGetAllResourcesRequest
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def get_all_resources(
    http: HttpClient,
    request: TimebackGetAllResourcesRequest,
) -> TimebackGetAllResourcesResponse:
    """Fetch a paginated list of resources.

    GET /ims/oneroster/resources/v1p2/resources
    """
    path = "/ims/oneroster/resources/v1p2/resources"

    query: Dict[str, Any] = {}
    if request.query_params:
        query = request.query_params.to_query_dict()

    data: Dict[str, Any] = http.get(path, params=query)
    log.debug(f"Raw Data: {data}")
    return TimebackGetAllResourcesResponse.model_validate(data)

