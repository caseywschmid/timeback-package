"""Post Results for Academic Session for Class endpoint for OneRoster Gradebook.

POST /ims/oneroster/gradebook/v1p2/classes/{classSourcedId}/academicSessions/{academicSessionSourcedId}/results

Creates new results for a specific academic session and class and returns the allocated sourcedIds.
"""

from typing import Any, Dict, List

from timeback.http import HttpClient
from timeback.models.request import TimebackPostResultsForAcademicSessionForClassRequest
from timeback.models.response import TimebackPostResultsForAcademicSessionForClassResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="DEBUG")


def post_results_for_academic_session_for_class(
    http: HttpClient, request: TimebackPostResultsForAcademicSessionForClassRequest
) -> TimebackPostResultsForAcademicSessionForClassResponse:
    """Create new results for a specific academic session and class.

    POST /ims/oneroster/gradebook/v1p2/classes/{classSourcedId}/academicSessions/{academicSessionSourcedId}/results

    Args:
        http: Injected HTTP client for making requests
        request: Request containing class_sourced_id, academic_session_sourced_id, and results array

    Returns:
        TimebackPostResultsForAcademicSessionForClassResponse containing sourcedId mapping
    """
    # Build the body with results array
    # Convert each result to dict using model_dump
    results_list: List[Dict[str, Any]] = [
        result.model_dump(exclude_none=True, by_alias=True) for result in request.results
    ]
    body: Dict[str, Any] = {"results": results_list}
    
    log.debug(f"POST body: {body}")
    log.debug(f"Class Sourced ID: {request.class_sourced_id}")
    log.debug(f"Academic Session Sourced ID: {request.academic_session_sourced_id}")
    
    data: Dict[str, Any] = http.post(
        f"/ims/oneroster/gradebook/v1p2/classes/{request.class_sourced_id}/academicSessions/{request.academic_session_sourced_id}/results",
        json=body
    )
    
    log.debug(f"Raw Data: {data}")
    resp = TimebackPostResultsForAcademicSessionForClassResponse.model_validate(data)
    return resp

