"""Get Term endpoint for OneRoster Rostering.

GET /ims/oneroster/rostering/v1p2/terms/{sourcedId}
"""

from typing import Any, Dict
from timeback.http import HttpClient
from timeback.models.request import TimebackGetTermRequest
from timeback.models.response import TimebackGetTermResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="DEBUG")


def get_term(
    http: HttpClient, request: TimebackGetTermRequest
) -> TimebackGetTermResponse:
    """Fetch a single term by sourcedId.

    GET /ims/oneroster/rostering/v1p2/terms/{sourcedId}
    """
    params: Dict[str, Any] = {}
    if request.query_params:
        params = request.query_params.to_query_dict()

    log.debug(f"Sourced ID: {request.sourced_id}")

    data = http.get(
        f"/ims/oneroster/rostering/v1p2/terms/{request.sourced_id}", params=params
    )

    log.debug(f"Raw Data: {data}")
    return TimebackGetTermResponse.model_validate(data)

