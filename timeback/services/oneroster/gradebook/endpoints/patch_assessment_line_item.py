"""Patch Assessment Line Item endpoint for OneRoster Gradebook.

PATCH /ims/oneroster/gradebook/v1p2/assessmentLineItems/{sourcedId}
"""

from typing import Any, Dict
from timeback.http import HttpClient
from timeback.models.request import TimebackPatchAssessmentLineItemRequest
from timeback.models.response import TimebackPatchAssessmentLineItemResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="DEBUG")


def patch_assessment_line_item(
    http: HttpClient, request: TimebackPatchAssessmentLineItemRequest
) -> TimebackPatchAssessmentLineItemResponse:
    """Partially update an assessment line item.

    PATCH /ims/oneroster/gradebook/v1p2/assessmentLineItems/{sourcedId}
    """
    body: Dict[str, Any] = request.model_dump(exclude_none=True, exclude={'sourced_id'}, by_alias=True)
    log.debug(f"PATCH body: {body}")
    log.debug(f"Sourced ID: {request.sourced_id}")
    
    data: Dict[str, Any] = http.patch(
        f"/ims/oneroster/gradebook/v1p2/assessmentLineItems/{request.sourced_id}", json=body
    )
    
    log.debug(f"Raw Data: {data}")
    return TimebackPatchAssessmentLineItemResponse.model_validate(data)

