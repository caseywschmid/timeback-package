"""Get Line Item endpoint for OneRoster Gradebook.

GET /ims/oneroster/gradebook/v1p2/lineItems/{sourcedId}

Fetches a single line item by its sourcedId.
"""

from typing import Any, Dict

from timeback.http import HttpClient
from timeback.models.request import TimebackGetLineItemRequest
from timeback.models.response import TimebackGetLineItemResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="DEBUG")


def get_line_item(
    http: HttpClient, request: TimebackGetLineItemRequest
) -> TimebackGetLineItemResponse:
    """Fetch a single line item by sourcedId.

    GET /ims/oneroster/gradebook/v1p2/lineItems/{sourcedId}

    Args:
        http: Injected HTTP client for making requests
        request: Request containing sourced_id and optional query parameters

    Returns:
        TimebackGetLineItemResponse containing the line item data
    """
    # Extract query params if provided
    params: Dict[str, Any] = {}
    if request.query_params:
        params = request.query_params.to_query_dict()
    
    log.debug(f"Params: {params}")
    log.debug(f"Sourced ID: {request.sourced_id}")
    
    data = http.get(
        f"/ims/oneroster/gradebook/v1p2/lineItems/{request.sourced_id}", params=params
    )
    
    log.debug(f"Raw Data: {data}")
    return TimebackGetLineItemResponse.model_validate(data)

