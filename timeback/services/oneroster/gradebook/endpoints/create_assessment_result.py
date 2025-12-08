"""Create Assessment Result endpoint for OneRoster Gradebook.

POST /ims/oneroster/gradebook/v1p2/assessmentResults

Creates a new assessment result and returns the allocated sourcedId.
"""

from typing import Any, Dict

from timeback.http import HttpClient
from timeback.models.request import TimebackCreateAssessmentResultRequest
from timeback.models.response import TimebackCreateAssessmentResultResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="DEBUG")


def create_assessment_result(
    http: HttpClient, request: TimebackCreateAssessmentResultRequest
) -> TimebackCreateAssessmentResultResponse:
    """Create a new assessment result.

    POST /ims/oneroster/gradebook/v1p2/assessmentResults

    Args:
        http: Injected HTTP client for making requests
        request: Request containing assessment result data to create

    Returns:
        TimebackCreateAssessmentResultResponse containing sourcedId mapping
    """
    body: Dict[str, Any] = request.model_dump(exclude_none=True)
    log.debug(f"POST body: {body}")
    
    data: Dict[str, Any] = http.post(
        "/ims/oneroster/gradebook/v1p2/assessmentResults", json=body
    )
    
    log.debug(f"Raw Data: {data}")
    resp = TimebackCreateAssessmentResultResponse.model_validate(data)
    return resp

