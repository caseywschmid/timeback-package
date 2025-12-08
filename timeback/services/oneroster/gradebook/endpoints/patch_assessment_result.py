"""Patch Assessment Result endpoint for OneRoster Gradebook.

PATCH /ims/oneroster/gradebook/v1p2/assessmentResults/{sourcedId}

Partially updates an assessment result with metadata merging support.
"""

from typing import Any, Dict

from timeback.http import HttpClient
from timeback.models.request import TimebackPatchAssessmentResultRequest
from timeback.models.response import TimebackPatchAssessmentResultResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="DEBUG")


def patch_assessment_result(
    http: HttpClient, request: TimebackPatchAssessmentResultRequest
) -> TimebackPatchAssessmentResultResponse:
    """Partially update an assessment result.

    PATCH /ims/oneroster/gradebook/v1p2/assessmentResults/{sourcedId}

    Args:
        http: Injected HTTP client for making requests
        request: Request containing sourced_id and partial assessment result data

    Returns:
        TimebackPatchAssessmentResultResponse containing the updated assessment result
    """
    # Exclude sourced_id from body since it's used in the URL path
    body: Dict[str, Any] = request.model_dump(exclude_none=True, exclude={'sourced_id'}, by_alias=True)
    log.debug(f"PATCH body: {body}")
    log.debug(f"Sourced ID: {request.sourced_id}")
    
    data: Dict[str, Any] = http.patch(
        f"/ims/oneroster/gradebook/v1p2/assessmentResults/{request.sourced_id}", json=body
    )
    
    log.debug(f"Raw Data: {data}")
    return TimebackPatchAssessmentResultResponse.model_validate(data)

