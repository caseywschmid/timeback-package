"""Update Demographic endpoint for OneRoster Rostering.

PUT /ims/oneroster/rostering/v1p2/demographics/{sourcedId}
"""

from typing import Any, Dict
from timeback.http import HttpClient
from timeback.models.request import TimebackUpdateDemographicRequest
from timeback.models.response import TimebackUpdateDemographicResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="DEBUG")


def update_demographic(
    http: HttpClient, request: TimebackUpdateDemographicRequest
) -> TimebackUpdateDemographicResponse:
    """Update an existing demographic.

    PUT /ims/oneroster/rostering/v1p2/demographics/{sourcedId}
    """
    body: Dict[str, Any] = {
        "demographics": request.demographics.model_dump(by_alias=True, exclude_none=True)
    }
    log.debug(f"PUT body: {body}")
    log.debug(f"Sourced ID: {request.sourced_id}")

    data: Dict[str, Any] = http.put(
        f"/ims/oneroster/rostering/v1p2/demographics/{request.sourced_id}", json=body
    )

    log.debug(f"Raw Data: {data}")
    return TimebackUpdateDemographicResponse.model_validate(data)

