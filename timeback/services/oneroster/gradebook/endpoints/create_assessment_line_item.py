"""Create Assessment Line Item endpoint for OneRoster Gradebook.

POST /ims/oneroster/gradebook/v1p2/assessmentLineItems
"""

from typing import Any, Dict
from timeback.http import HttpClient
from timeback.models.request import TimebackCreateAssessmentLineItemRequest
from timeback.models.response import TimebackCreateAssessmentLineItemResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="DEBUG")


def create_assessment_line_item(
    http: HttpClient, request: TimebackCreateAssessmentLineItemRequest
) -> TimebackCreateAssessmentLineItemResponse:
    """Create a new assessment line item.

    POST /ims/oneroster/gradebook/v1p2/assessmentLineItems
    """
    body: Dict[str, Any] = request.model_dump(exclude_none=True, by_alias=True)
    log.debug(f"POST body: {body}")
    
    data: Dict[str, Any] = http.post(
        "/ims/oneroster/gradebook/v1p2/assessmentLineItems", json=body
    )
    
    log.debug(f"Raw Data: {data}")
    return TimebackCreateAssessmentLineItemResponse.model_validate(data)

