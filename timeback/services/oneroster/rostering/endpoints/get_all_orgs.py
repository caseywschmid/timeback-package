"""Get All Orgs endpoint for OneRoster Rostering.

GET /ims/oneroster/rostering/v1p2/orgs
"""

from typing import Any, Dict
from timeback.http import HttpClient
from timeback.models.request import TimebackGetAllOrgsRequest
from timeback.models.response import TimebackGetAllOrgsResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def get_all_orgs(
    http: HttpClient, request: TimebackGetAllOrgsRequest
) -> TimebackGetAllOrgsResponse:
    """Fetch all orgs (paginated list).

    GET /ims/oneroster/rostering/v1p2/orgs
    """
    path = "/ims/oneroster/rostering/v1p2/orgs"

    query: Dict[str, Any] = {}
    if request.query_params:
        query = request.query_params.to_query_dict()

    data: Dict[str, Any] = http.get(path, params=query)
    log.debug(f"Raw Data: {data}")
    return TimebackGetAllOrgsResponse.model_validate(data)

