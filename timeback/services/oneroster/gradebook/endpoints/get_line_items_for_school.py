"""Get Line Items for School endpoint for OneRoster Gradebook.

GET /ims/oneroster/gradebook/v1p2/schools/{sourcedId}/lineItems

Builds the full path and query params, performs the HTTP GET via the injected
`HttpClient`, and parses the response into `TimebackGetAllLineItemsResponse`.
"""

from typing import Any, Dict

from timeback.http import HttpClient
from timeback.models.response import TimebackGetAllLineItemsResponse
from timeback.models.request import TimebackGetLineItemsForSchoolRequest
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def get_line_items_for_school(
    http: HttpClient,
    request: TimebackGetLineItemsForSchoolRequest,
) -> TimebackGetAllLineItemsResponse:
    """Fetch a paginated list of line items for a specific school.

    GET /ims/oneroster/gradebook/v1p2/schools/{sourcedId}/lineItems

    Args:
        http: Injected HTTP client for making requests
        request: Request containing school_sourced_id and optional query parameters

    Returns:
        TimebackGetAllLineItemsResponse containing paginated list of line items
    """
    path = f"/ims/oneroster/gradebook/v1p2/schools/{request.school_sourced_id}/lineItems"

    query: Dict[str, Any] = {}
    if request.query_params:
        query = request.query_params.to_query_dict()

    data: Dict[str, Any] = http.get(path, params=query)
    log.debug(f"Raw Data: {data}")
    return TimebackGetAllLineItemsResponse.model_validate(data)

