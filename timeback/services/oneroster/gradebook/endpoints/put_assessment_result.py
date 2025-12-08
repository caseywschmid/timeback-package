"""Put Assessment Result endpoint for OneRoster Gradebook.

PUT /ims/oneroster/gradebook/v1p2/assessmentResults/{sourcedId}

Updates or creates an assessment result with the given sourcedId.
"""

from typing import Any, Dict

from timeback.http import HttpClient
from timeback.models.request import TimebackPutAssessmentResultRequest
from timeback.models.response import TimebackPutAssessmentResultResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="DEBUG")


def put_assessment_result(
    http: HttpClient, request: TimebackPutAssessmentResultRequest
) -> TimebackPutAssessmentResultResponse:
    """Update or create an assessment result.

    PUT /ims/oneroster/gradebook/v1p2/assessmentResults/{sourcedId}

    Args:
        http: Injected HTTP client for making requests
        request: Request containing sourced_id and assessment result data

    Returns:
        TimebackPutAssessmentResultResponse containing the updated/created assessment result
    """
    # Exclude sourced_id from body since it's used in the URL path
    body: Dict[str, Any] = request.model_dump(exclude_none=True, exclude={'sourced_id'}, by_alias=True)
    log.debug(f"PUT body: {body}")
    log.debug(f"Sourced ID: {request.sourced_id}")
    
    data: Dict[str, Any] = http.put(
        f"/ims/oneroster/gradebook/v1p2/assessmentResults/{request.sourced_id}", json=body
    )
    
    log.debug(f"Raw Data: {data}")
    return TimebackPutAssessmentResultResponse.model_validate(data)

