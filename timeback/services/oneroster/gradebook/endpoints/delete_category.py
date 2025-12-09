"""Delete Category endpoint for OneRoster Gradebook.

DELETE /ims/oneroster/gradebook/v1p2/categories/{sourcedId}

Performs a soft delete on a specific category (sets status to 'tobedeleted').
"""

from typing import Optional, Dict, Any
from timeback.http import HttpClient
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="DEBUG")


def delete_category(http: HttpClient, sourced_id: str) -> Optional[Dict[str, Any]]:
    """Soft delete a category (sets status to 'tobedeleted').

    DELETE /ims/oneroster/gradebook/v1p2/categories/{sourcedId}
    
    Args:
        http: Injected HTTP client for making requests
        sourced_id: The sourcedId of the category to delete
    
    Returns:
        Optional[Dict[str, Any]]: Raw provider response (None for 204 No Content)
    """
    log.debug(f"Deleting category: {sourced_id}")
    return http.delete(f"/ims/oneroster/gradebook/v1p2/categories/{sourced_id}")

