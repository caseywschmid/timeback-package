"""Delete Line Item endpoint for OneRoster Gradebook.

DELETE /ims/oneroster/gradebook/v1p2/lineItems/{sourcedId}

Soft deletes a line item by its sourcedId.
"""

from typing import Optional, Dict, Any

from timeback.http import HttpClient
from timeback.models.request import TimebackDeleteLineItemRequest
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="DEBUG")


def delete_line_item(
    http: HttpClient, request: TimebackDeleteLineItemRequest
) -> Optional[Dict[str, Any]]:
    """Delete a line item.

    DELETE /ims/oneroster/gradebook/v1p2/lineItems/{sourcedId}

    Args:
        http: Injected HTTP client for making requests
        request: Request containing sourced_id

    Returns:
        Optional[Dict[str, Any]]: Raw provider response (None for no-content)
    """
    log.debug(f"Deleting line item: {request.sourced_id}")
    
    return http.delete(
        f"/ims/oneroster/gradebook/v1p2/lineItems/{request.sourced_id}"
    )

