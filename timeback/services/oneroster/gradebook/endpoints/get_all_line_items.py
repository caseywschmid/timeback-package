"""Get All Line Items endpoint for OneRoster Gradebook.

GET /ims/oneroster/gradebook/v1p2/lineItems

Builds the full path and query params, performs the HTTP GET via the injected
`HttpClient`, and parses the response into `TimebackGetAllLineItemsResponse`.
"""

from typing import Any, Dict

from timeback.http import HttpClient
from timeback.models.response import TimebackGetAllLineItemsResponse
from timeback.models.request import TimebackGetAllLineItemsRequest
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def get_all_line_items(
    http: HttpClient,
    request: TimebackGetAllLineItemsRequest,
) -> TimebackGetAllLineItemsResponse:
    """Fetch a paginated list of line items.

    GET /ims/oneroster/gradebook/v1p2/lineItems

    Args:
        http: Injected HTTP client for making requests
        request: Request containing optional query parameters

    Returns:
        TimebackGetAllLineItemsResponse containing paginated list of line items
    """
    path = "/ims/oneroster/gradebook/v1p2/lineItems"

    query: Dict[str, Any] = {}
    if request.query_params:
        query = request.query_params.to_query_dict()

    data: Dict[str, Any] = http.get(path, params=query)
    log.debug(f"Raw Data: {data}")
    return TimebackGetAllLineItemsResponse.model_validate(data)

