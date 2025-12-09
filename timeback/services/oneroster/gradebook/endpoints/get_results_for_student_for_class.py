"""Get Results for Student for Class endpoint for OneRoster Gradebook.

GET /ims/oneroster/gradebook/v1p2/classes/{classSourcedId}/students/{studentSourcedId}/results

Builds the full path and query params, performs the HTTP GET via the injected
`HttpClient`, and parses the response into `TimebackGetAllResultsResponse`.
"""

from typing import Any, Dict

from timeback.http import HttpClient
from timeback.models.response import TimebackGetAllResultsResponse
from timeback.models.request import TimebackGetResultsForStudentForClassRequest
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def get_results_for_student_for_class(
    http: HttpClient,
    request: TimebackGetResultsForStudentForClassRequest,
) -> TimebackGetAllResultsResponse:
    """Fetch a paginated list of results for a specific student and class.

    GET /ims/oneroster/gradebook/v1p2/classes/{classSourcedId}/students/{studentSourcedId}/results

    Args:
        http: Injected HTTP client for making requests
        request: Request containing class_sourced_id, student_sourced_id, and optional query parameters

    Returns:
        TimebackGetAllResultsResponse containing paginated list of results
    """
    path = f"/ims/oneroster/gradebook/v1p2/classes/{request.class_sourced_id}/students/{request.student_sourced_id}/results"

    query: Dict[str, Any] = {}
    if request.query_params:
        query = request.query_params.to_query_dict()

    data: Dict[str, Any] = http.get(path, params=query)
    log.debug(f"Raw Data: {data}")
    return TimebackGetAllResultsResponse.model_validate(data)

