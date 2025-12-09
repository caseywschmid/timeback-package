"""Update Org endpoint for OneRoster Rostering.

PUT /ims/oneroster/rostering/v1p2/orgs/{sourcedId}
"""

from typing import Any, Dict
from timeback.http import HttpClient
from timeback.models.request import TimebackUpdateOrgRequest
from timeback.models.response import TimebackUpdateOrgResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="DEBUG")


def update_org(
    http: HttpClient, request: TimebackUpdateOrgRequest
) -> TimebackUpdateOrgResponse:
    """Update an existing org.

    PUT /ims/oneroster/rostering/v1p2/orgs/{sourcedId}
    """
    body: Dict[str, Any] = {"org": request.org.model_dump(by_alias=True, exclude_none=True)}
    log.debug(f"PUT body: {body}")
    log.debug(f"Sourced ID: {request.sourced_id}")

    data: Dict[str, Any] = http.put(
        f"/ims/oneroster/rostering/v1p2/orgs/{request.sourced_id}", json=body
    )

    log.debug(f"Raw Data: {data}")
    return TimebackUpdateOrgResponse.model_validate(data)

