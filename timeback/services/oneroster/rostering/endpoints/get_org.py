"""Get Org endpoint for OneRoster Rostering.

GET /ims/oneroster/rostering/v1p2/orgs/{sourcedId}
"""

from typing import Any, Dict
from timeback.http import HttpClient
from timeback.models.request import TimebackGetOrgRequest
from timeback.models.response import TimebackGetOrgResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="DEBUG")


def get_org(
    http: HttpClient, request: TimebackGetOrgRequest
) -> TimebackGetOrgResponse:
    """Fetch a single org by sourcedId.

    GET /ims/oneroster/rostering/v1p2/orgs/{sourcedId}
    """
    params: Dict[str, Any] = {}
    if request.query_params:
        params = request.query_params.to_query_dict()

    log.debug(f"Sourced ID: {request.sourced_id}")

    data = http.get(
        f"/ims/oneroster/rostering/v1p2/orgs/{request.sourced_id}", params=params
    )

    log.debug(f"Raw Data: {data}")
    return TimebackGetOrgResponse.model_validate(data)

