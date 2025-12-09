"""Create Org endpoint for OneRoster Rostering.

POST /ims/oneroster/rostering/v1p2/orgs
"""

from typing import Any, Dict
from timeback.http import HttpClient
from timeback.models.request import TimebackCreateOrgRequest
from timeback.models.response import TimebackCreateOrgResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="DEBUG")


def create_org(
    http: HttpClient, request: TimebackCreateOrgRequest
) -> TimebackCreateOrgResponse:
    """Create a new org.

    POST /ims/oneroster/rostering/v1p2/orgs
    """
    body: Dict[str, Any] = {"org": request.org.model_dump(by_alias=True, exclude_none=True)}
    log.debug(f"POST body: {body}")

    data: Dict[str, Any] = http.post("/ims/oneroster/rostering/v1p2/orgs", json=body)

    log.debug(f"Raw Data: {data}")
    return TimebackCreateOrgResponse.model_validate(data)

