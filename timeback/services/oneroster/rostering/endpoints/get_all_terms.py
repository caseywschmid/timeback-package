"""Get All Terms endpoint for OneRoster Rostering.

GET /ims/oneroster/rostering/v1p2/terms
"""

from typing import Any, Dict
from timeback.http import HttpClient
from timeback.models.request import TimebackGetAllTermsRequest
from timeback.models.response import TimebackGetAllTermsResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def get_all_terms(
    http: HttpClient, request: TimebackGetAllTermsRequest
) -> TimebackGetAllTermsResponse:
    """Fetch all terms (paginated list).

    GET /ims/oneroster/rostering/v1p2/terms
    """
    path = "/ims/oneroster/rostering/v1p2/terms"

    query: Dict[str, Any] = {}
    if request.query_params:
        query = request.query_params.to_query_dict()

    data: Dict[str, Any] = http.get(path, params=query)
    log.debug(f"Raw Data: {data}")
    return TimebackGetAllTermsResponse.model_validate(data)

