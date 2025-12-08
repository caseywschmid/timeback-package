"""Get All Assessment Line Items endpoint for OneRoster Gradebook.

GET /ims/oneroster/gradebook/v1p2/assessmentLineItems

Builds the full path and query params, performs the HTTP GET via the injected
`HttpClient`, and parses the response into `TimebackGetAllAssessmentLineItemsResponse`.
"""

from typing import Any, Dict

from timeback.http import HttpClient
from timeback.models.response import TimebackGetAllAssessmentLineItemsResponse
from timeback.models.request import TimebackGetAllAssessmentLineItemsRequest
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def get_all_assessment_line_items(
    http: HttpClient,
    request: TimebackGetAllAssessmentLineItemsRequest,
) -> TimebackGetAllAssessmentLineItemsResponse:
    """Fetch a paginated list of assessment line items.

    GET /ims/oneroster/gradebook/v1p2/assessmentLineItems

    Args:
        http: Injected HTTP client for making requests
        request: Request containing optional query parameters

    Returns:
        TimebackGetAllAssessmentLineItemsResponse containing paginated list of assessment line items
    """
    path = "/ims/oneroster/gradebook/v1p2/assessmentLineItems"

    query: Dict[str, Any] = {}
    if request.query_params:
        query = request.query_params.to_query_dict()

    data: Dict[str, Any] = http.get(path, params=query)
    log.debug(f"Raw Data: {data}")
    return TimebackGetAllAssessmentLineItemsResponse.model_validate(data)

