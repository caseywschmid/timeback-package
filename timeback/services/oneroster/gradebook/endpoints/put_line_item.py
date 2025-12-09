"""Put Line Item endpoint for OneRoster Gradebook.

PUT /ims/oneroster/gradebook/v1p2/lineItems/{sourcedId}

Updates or creates a line item with the given sourcedId.
"""

from typing import Any, Dict

from timeback.http import HttpClient
from timeback.models.request import TimebackPutLineItemRequest
from timeback.models.response import TimebackPutLineItemResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="DEBUG")


def put_line_item(
    http: HttpClient, request: TimebackPutLineItemRequest
) -> TimebackPutLineItemResponse:
    """Update or create a line item.

    PUT /ims/oneroster/gradebook/v1p2/lineItems/{sourcedId}

    Args:
        http: Injected HTTP client for making requests
        request: Request containing sourced_id and line item data

    Returns:
        TimebackPutLineItemResponse containing the updated/created line item
    """
    # Exclude sourced_id from body since it's used in the URL path
    # Use by_alias=True to get "lineItem" instead of potentially snake_case
    body: Dict[str, Any] = request.model_dump(exclude_none=True, exclude={'sourced_id'}, by_alias=True)
    log.debug(f"PUT body: {body}")
    log.debug(f"Sourced ID: {request.sourced_id}")
    
    data: Dict[str, Any] = http.put(
        f"/ims/oneroster/gradebook/v1p2/lineItems/{request.sourced_id}", json=body
    )
    
    log.debug(f"Raw Data: {data}")
    return TimebackPutLineItemResponse.model_validate(data)

