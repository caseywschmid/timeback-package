"""Get Demographic endpoint for OneRoster Rostering.

GET /ims/oneroster/rostering/v1p2/demographics/{sourcedId}
"""

from typing import Any, Dict
from timeback.http import HttpClient
from timeback.models.request import TimebackGetDemographicRequest
from timeback.models.response import TimebackGetDemographicResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="DEBUG")


def get_demographic(
    http: HttpClient, request: TimebackGetDemographicRequest
) -> TimebackGetDemographicResponse:
    """Fetch a single demographic by sourcedId.

    GET /ims/oneroster/rostering/v1p2/demographics/{sourcedId}
    """
    params: Dict[str, Any] = {}
    if request.query_params:
        params = request.query_params.to_query_dict()

    log.debug(f"Sourced ID: {request.sourced_id}")

    data = http.get(
        f"/ims/oneroster/rostering/v1p2/demographics/{request.sourced_id}", params=params
    )

    log.debug(f"Raw Data: {data}")
    return TimebackGetDemographicResponse.model_validate(data)

