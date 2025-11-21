"""Create Line Items for School endpoint for OneRoster Gradebook.

POST /ims/oneroster/gradebook/v1p2/schools/{sourcedId}/lineItems

Creates new line items for a specific school and returns the allocated sourcedIds.
"""

from typing import Any, Dict, List

from timeback.http import HttpClient
from timeback.models.request import TimebackCreateLineItemsForSchoolRequest
from timeback.models.response import TimebackCreateLineItemsForSchoolResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="DEBUG")


def create_line_items_for_school(
    http: HttpClient, request: TimebackCreateLineItemsForSchoolRequest
) -> TimebackCreateLineItemsForSchoolResponse:
    """Create new line items for a specific school.

    POST /ims/oneroster/gradebook/v1p2/schools/{sourcedId}/lineItems

    Args:
        http: Injected HTTP client for making requests
        request: Request containing school_sourced_id and lineItems array

    Returns:
        TimebackCreateLineItemsForSchoolResponse containing sourcedId mapping
    """
    # Build the body with lineItems array
    # Convert each line item to dict using model_dump
    line_items_list: List[Dict[str, Any]] = [
        line_item.model_dump(exclude_none=True, by_alias=True) for line_item in request.lineItems
    ]
    body: Dict[str, Any] = {"lineItems": line_items_list}
    
    log.debug(f"POST body: {body}")
    log.debug(f"School Sourced ID: {request.school_sourced_id}")
    
    data: Dict[str, Any] = http.post(
        f"/ims/oneroster/gradebook/v1p2/schools/{request.school_sourced_id}/lineItems",
        json=body
    )
    
    log.debug(f"Raw Data: {data}")
    resp = TimebackCreateLineItemsForSchoolResponse.model_validate(data)
    return resp

