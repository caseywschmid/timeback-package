"""Create Result for Line Item endpoint for OneRoster Gradebook.

POST /ims/oneroster/gradebook/v1p2/lineItems/{sourcedId}/results

Creates new results for a specific line item and returns the allocated sourcedIds.
"""

from typing import Any, Dict, List

from timeback.http import HttpClient
from timeback.models.request import TimebackCreateResultForLineItemRequest
from timeback.models.response import TimebackCreateResultForLineItemResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="DEBUG")


def create_result_for_line_item(
    http: HttpClient, request: TimebackCreateResultForLineItemRequest
) -> TimebackCreateResultForLineItemResponse:
    """Create new results for a specific line item.

    POST /ims/oneroster/gradebook/v1p2/lineItems/{sourcedId}/results

    Args:
        http: Injected HTTP client for making requests
        request: Request containing line_item_sourced_id and results array

    Returns:
        TimebackCreateResultForLineItemResponse containing sourcedId mapping
    """
    # Build the body with results array
    # Convert each result to dict using model_dump
    results_list: List[Dict[str, Any]] = [
        result.model_dump(exclude_none=True, by_alias=True) for result in request.results
    ]
    body: Dict[str, Any] = {"results": results_list}
    
    log.debug(f"POST body: {body}")
    log.debug(f"Line Item Sourced ID: {request.line_item_sourced_id}")
    
    data: Dict[str, Any] = http.post(
        f"/ims/oneroster/gradebook/v1p2/lineItems/{request.line_item_sourced_id}/results",
        json=body
    )
    
    log.debug(f"Raw Data: {data}")
    resp = TimebackCreateResultForLineItemResponse.model_validate(data)
    return resp

