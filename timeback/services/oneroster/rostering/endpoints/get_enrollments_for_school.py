"""Get Enrollments for School endpoint for OneRoster Rostering.

GET /ims/oneroster/rostering/v1p2/schools/{schoolSourcedId}/enrollments
"""

from typing import Any, Dict
from timeback.http import HttpClient
from timeback.models.request import TimebackGetEnrollmentsForSchoolRequest
from timeback.models.response import TimebackGetAllEnrollmentsResponse  # Reuse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def get_enrollments_for_school(
    http: HttpClient, request: TimebackGetEnrollmentsForSchoolRequest
) -> TimebackGetAllEnrollmentsResponse:
    """Fetch enrollments for a specific school.

    GET /ims/oneroster/rostering/v1p2/schools/{schoolSourcedId}/enrollments
    """
    path = f"/ims/oneroster/rostering/v1p2/schools/{request.school_sourced_id}/enrollments"

    query: Dict[str, Any] = {}
    if request.query_params:
        query = request.query_params.to_query_dict()

    data: Dict[str, Any] = http.get(path, params=query)
    log.debug(f"Raw Data: {data}")
    return TimebackGetAllEnrollmentsResponse.model_validate(data)

