"""Create Demographic endpoint for OneRoster Rostering.

POST /ims/oneroster/rostering/v1p2/demographics
"""

from typing import Any, Dict
from timeback.http import HttpClient
from timeback.models.request import TimebackCreateDemographicRequest
from timeback.models.response import TimebackCreateDemographicResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="DEBUG")


def create_demographic(
    http: HttpClient, request: TimebackCreateDemographicRequest
) -> TimebackCreateDemographicResponse:
    """Create a new demographic.

    POST /ims/oneroster/rostering/v1p2/demographics
    """
    body: Dict[str, Any] = {
        "demographics": request.demographics.model_dump(by_alias=True, exclude_none=True)
    }
    log.debug(f"POST body: {body}")

    data: Dict[str, Any] = http.post("/ims/oneroster/rostering/v1p2/demographics", json=body)

    log.debug(f"Raw Data: {data}")
    return TimebackCreateDemographicResponse.model_validate(data)

