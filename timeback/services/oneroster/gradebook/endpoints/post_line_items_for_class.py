"""Post Line Items for Class endpoint for OneRoster Gradebook.

POST /ims/oneroster/gradebook/v1p2/classes/{classSourcedId}/lineItems

Creates new line items for a specific class and returns the allocated sourcedIds.
"""

from typing import Any, Dict, List

from timeback.http import HttpClient
from timeback.models.request import TimebackPostLineItemsForClassRequest
from timeback.models.response import TimebackPostLineItemsForClassResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="DEBUG")


def post_line_items_for_class(
    http: HttpClient, request: TimebackPostLineItemsForClassRequest
) -> TimebackPostLineItemsForClassResponse:
    """Create new line items for a specific class.

    POST /ims/oneroster/gradebook/v1p2/classes/{classSourcedId}/lineItems

    Args:
        http: Injected HTTP client for making requests
        request: Request containing class_sourced_id and lineItems array

    Returns:
        TimebackPostLineItemsForClassResponse containing sourcedId mapping
    """
    # Build the body with lineItems array
    # Convert each line item to dict using model_dump
    line_items_list: List[Dict[str, Any]] = [
        line_item.model_dump(exclude_none=True, by_alias=True) for line_item in request.lineItems
    ]
    body: Dict[str, Any] = {"lineItems": line_items_list}
    
    log.debug(f"POST body: {body}")
    log.debug(f"Class Sourced ID: {request.class_sourced_id}")
    
    data: Dict[str, Any] = http.post(
        f"/ims/oneroster/gradebook/v1p2/classes/{request.class_sourced_id}/lineItems",
        json=body
    )
    
    log.debug(f"Raw Data: {data}")
    resp = TimebackPostLineItemsForClassResponse.model_validate(data)
    return resp

