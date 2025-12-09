"""Put Assessment Line Item endpoint for OneRoster Gradebook.

PUT /ims/oneroster/gradebook/v1p2/assessmentLineItems/{sourcedId}
"""

from typing import Any, Dict
from timeback.http import HttpClient
from timeback.models.request import TimebackPutAssessmentLineItemRequest
from timeback.models.response import TimebackPutAssessmentLineItemResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="DEBUG")


def put_assessment_line_item(
    http: HttpClient, request: TimebackPutAssessmentLineItemRequest
) -> TimebackPutAssessmentLineItemResponse:
    """Update or create an assessment line item.

    PUT /ims/oneroster/gradebook/v1p2/assessmentLineItems/{sourcedId}
    """
    body: Dict[str, Any] = request.model_dump(exclude_none=True, exclude={'sourced_id'}, by_alias=True)
    log.debug(f"PUT body: {body}")
    log.debug(f"Sourced ID: {request.sourced_id}")
    
    data: Dict[str, Any] = http.put(
        f"/ims/oneroster/gradebook/v1p2/assessmentLineItems/{request.sourced_id}", json=body
    )
    
    log.debug(f"Raw Data: {data}")
    return TimebackPutAssessmentLineItemResponse.model_validate(data)

