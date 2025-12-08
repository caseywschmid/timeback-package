"""Get Terms for School endpoint for OneRoster Rostering.

GET /ims/oneroster/rostering/v1p2/schools/{schoolSourcedId}/terms
"""

from typing import Any, Dict
from timeback.http import HttpClient
from timeback.models.request import TimebackGetTermsForSchoolRequest
from timeback.models.response import TimebackGetAllTermsResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def get_terms_for_school(
    http: HttpClient, request: TimebackGetTermsForSchoolRequest
) -> TimebackGetAllTermsResponse:
    """Fetch terms for a specific school.

    GET /ims/oneroster/rostering/v1p2/schools/{schoolSourcedId}/terms
    """
    path = f"/ims/oneroster/rostering/v1p2/schools/{request.school_sourced_id}/terms"

    query: Dict[str, Any] = {}
    if request.query_params:
        query = request.query_params.to_query_dict()

    data: Dict[str, Any] = http.get(path, params=query)
    log.debug(f"Raw Data: {data}")
    return TimebackGetAllTermsResponse.model_validate(data)

