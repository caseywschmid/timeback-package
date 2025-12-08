"""Get All Demographics endpoint for OneRoster Rostering.

GET /ims/oneroster/rostering/v1p2/demographics
"""

from typing import Any, Dict
from timeback.http import HttpClient
from timeback.models.request import TimebackGetAllDemographicsRequest
from timeback.models.response import TimebackGetAllDemographicsResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def get_all_demographics(
    http: HttpClient, request: TimebackGetAllDemographicsRequest
) -> TimebackGetAllDemographicsResponse:
    """Fetch all demographics (paginated list).

    GET /ims/oneroster/rostering/v1p2/demographics
    """
    path = "/ims/oneroster/rostering/v1p2/demographics"

    query: Dict[str, Any] = {}
    if request.query_params:
        query = request.query_params.to_query_dict()

    data: Dict[str, Any] = http.get(path, params=query)
    log.debug(f"Raw Data: {data}")
    return TimebackGetAllDemographicsResponse.model_validate(data)

