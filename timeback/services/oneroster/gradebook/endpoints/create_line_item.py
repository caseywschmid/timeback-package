"""Create Line Item endpoint for OneRoster Gradebook.

POST /ims/oneroster/gradebook/v1p2/lineItems

Creates a new line item and returns the allocated sourcedId.
"""

from typing import Any, Dict

from timeback.http import HttpClient
from timeback.models.request import TimebackCreateLineItemRequest
from timeback.models.response import TimebackCreateLineItemResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="DEBUG")


def create_line_item(
    http: HttpClient, request: TimebackCreateLineItemRequest
) -> TimebackCreateLineItemResponse:
    """Create a new line item.

    POST /ims/oneroster/gradebook/v1p2/lineItems

    Args:
        http: Injected HTTP client for making requests
        request: Request containing line item data to create

    Returns:
        TimebackCreateLineItemResponse containing sourcedId mapping
    """
    body: Dict[str, Any] = request.model_dump(exclude_none=True)
    log.debug(f"POST body: {body}")
    
    data: Dict[str, Any] = http.post(
        "/ims/oneroster/gradebook/v1p2/lineItems", json=body
    )
    
    log.debug(f"Raw Data: {data}")
    resp = TimebackCreateLineItemResponse.model_validate(data)
    return resp

