"""Get Assessment Line Item endpoint for OneRoster Gradebook.

GET /ims/oneroster/gradebook/v1p2/assessmentLineItems/{sourcedId}
"""

from typing import Any, Dict
from timeback.http import HttpClient
from timeback.models.request import TimebackGetAssessmentLineItemRequest
from timeback.models.response import TimebackGetAssessmentLineItemResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="DEBUG")


def get_assessment_line_item(
    http: HttpClient, request: TimebackGetAssessmentLineItemRequest
) -> TimebackGetAssessmentLineItemResponse:
    """Fetch a single assessment line item by sourcedId.

    GET /ims/oneroster/gradebook/v1p2/assessmentLineItems/{sourcedId}
    """
    params: Dict[str, Any] = {}
    if request.query_params:
        params = request.query_params.to_query_dict()
    
    log.debug(f"Params: {params}")
    log.debug(f"Sourced ID: {request.sourced_id}")
    
    data = http.get(
        f"/ims/oneroster/gradebook/v1p2/assessmentLineItems/{request.sourced_id}", params=params
    )
    
    log.debug(f"Raw Data: {data}")
    return TimebackGetAssessmentLineItemResponse.model_validate(data)

